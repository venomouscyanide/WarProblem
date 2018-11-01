from math import ceil
def defend_planet(defendor_army,attacker_army):
	'''
	The primary function that helps calculate
	the weapons needed by the defender to be deployed
	Also helps determine if the batte is winnable or not
	'''

	'''
	the lists that contain the defenders and attackers 
	weapons(army) number. ie number of weapons deployed
	and the number of weapon capacity they have
	'''
	weapon_capacity_def=[]
	weapon_in_battle_def=[]

	weapon_capacity_att=[]
	weapon_in_battle_att=[]

	'''
	populate the weapon lists from the repective classes
	'''
	weapon_capacity_def=defendor_army.get_weapon_count(True,False)
	weapon_in_battle_def=defendor_army.get_weapon_count(False,True)

	weapon_capacity_att=attacker_army.get_weapon_count(True,False)
	weapon_in_battle_att=attacker_army.get_weapon_count(False,True)

	'''
	keep a copy of the original defender's army capacity
	'''
	org_def_battle=[x for x in weapon_capacity_def]

	'''
	flag list is used to keep track of the weapons that need
	help to match the number deployed by the attackers

	set to 1 if that particular weapon needs to borrow 
	set to 0 if the weapon by itself can match the attacker
	'''
	flag=[0 for x in range(4)]

	'''
	apply Rule#1
	'''
	to_defend=[ceil(x/2) if x%2!=0 else int(x/2) for x in weapon_in_battle_att]
	
	for i in range(4):
		if(weapon_capacity_def[i]>=to_defend[i]):#the defender weapon number is enough
			weapon_in_battle_def[i]=to_defend[i] 
			weapon_capacity_def[i]-=to_defend[i]

		elif(weapon_capacity_def[i]<to_defend[i]):#defender weapon needs help(needs to borrow)
			weapon_in_battle_def[i]=weapon_capacity_def[i]#all go in
			weapon_capacity_def[i]=0 #nothing will be left as all go in
			flag[i]=1 #it needs help to get even

	for i in range(4):
		if(flag[i]==1):
			#to get the count of the number of defender's weapon by which it falls short 
			needed=to_defend[i]-org_def_battle[i]
			try:
				#borrow from the left. QTY X2 because the weapon on the left is of lower value
				if(weapon_capacity_def[i-1]>0 and weapon_capacity_def[i-1]>=needed*2 and (i-1>=0)):
					weapon_capacity_def[i-1]-=needed*2
					weapon_in_battle_def[i-1]+=needed*2
					needed=0#defender wins the war
			except:
				pass

			try:
				#borrow from the right. QTY /2 because the weapon on the right is of greater value
				if(weapon_capacity_def[i+1]>0 and weapon_capacity_def[i+1]>=ceil(needed/2) and needed>0):
						weapon_capacity_def[i+1]-=ceil(needed/2)
						weapon_in_battle_def[i+1]+=ceil(needed/2)
						needed=0#defender wins the war
			except:
				pass

			try:
				#special scenari where the weapons needs borrowing from both the left and the right
				if(weapon_capacity_def[i-1]>0 and weapon_capacity_def[i+1]>0 and (i-1>=0) and needed>0):
					needed-=ceil(weapon_capacity_def[i-1]/2)#take everything from left
					weapon_in_battle_def[i-1]+=weapon_capacity_def[i-1]
					weapon_capacity_def[i-1]=0
					if(weapon_capacity_def[i+1]>=ceil(needed/2)):#there is enough on the right
						weapon_capacity_def[i+1]-=ceil(needed/2)
						weapon_in_battle_def[i+1]+=ceil(needed/2)
						needed=0#defender wins the war
					else:#there is not enough on the right to match
						weapon_in_battle_def[i+1]+=weapon_capacity_def[i+1]
						weapon_capacity_def[i+1]=0
			except:
					pass
	if(needed>0):
		'''
		is there is still deficit of weapons defender loses
		'''
		weapon_in_battle_def.append(False)
		return(weapon_in_battle_def)
	else:
		'''
		defender wins when the weapon numbers are matched
		'''
		weapon_in_battle_def.append(True)
		return(weapon_in_battle_def)
