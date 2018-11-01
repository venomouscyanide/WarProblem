#Set2Problem1

from math import ceil
from Planets.lengaburu import Lengaburu
from Planets.falicornia import Falicornia
from Defence.defence_function import defend_planet

#
if __name__=="__main__":
	'''
	driver function to defend one planet 
	from the attacking planet
	'''
	falcone_army_input=input().rstrip().split()
	falcone_army_integers=[]

	for i in range(len(falcone_army_input)):
		try:
			if(int(falcone_army_input[i])>=0):
				falcone_army_integers.append(int(falcone_army_input[i]))
		except:
			pass

	falcone_army=Falicornia(falcone_army_integers[0],falcone_army_integers[1],falcone_army_integers[2],falcone_army_integers[3])
	
	shah_army=Lengaburu()

	'''
	preparing is nothing but getting the armies deployed 
	and in capacity to a list for ease of usage
	'''
	shah_army.prepare()
	falcone_army.prepare()
	
	shah_deployed=[]
	shah_deployed=defend_planet(shah_army,falcone_army)
	if(shah_deployed[-1]==True):
		result="wins"
	else:
		result="loses"
	'''
	finally print out the amount deployed by shah(Defender)
	and the war result
	'''
	print("Lengaburu deploys {a} H, {b} E, {c} AT, {d} SG and {e}".format(a=shah_deployed[0],b=shah_deployed[1],c=shah_deployed[2],d=shah_deployed[3],e=result))
	#print(shah_army.printele())
