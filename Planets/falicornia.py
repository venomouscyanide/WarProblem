class Falicornia:
	
	def __init__(self,horses=0,elephants=0,armoured_tanks=0,sling_guns=0):
		'''
		provide the maximum values of the 
		weapons of Falicornia in this class
		'''
		self.__horses=300
		self.__elephants=200
		self.__armoured_tanks=40
		self.__sling_guns=20
		self.__attack_horse=horses
		self.__attack_elephants=elephants
		self.__attack_armoured_tanks=armoured_tanks
		self.__attack_sling_guns=sling_guns

	def prepare(self):
		'''
		prepare the weapons before battle
		'''
		self.weapon_capacity=[]
		self.weapon_in_battle=[]
		self.weapon_capacity.extend([self.__horses,self.__elephants,self.__armoured_tanks,self.__sling_guns])
		self.weapon_in_battle.extend([self.__attack_horse,self.__attack_elephants,self.__attack_armoured_tanks,self.__attack_sling_guns])

	def get_weapon_count(self,capacity,out_for_battle):	
		'''
		return the values of max weapons
		and the currently deployed weapons
		'''	
		if capacity==True:
			return self.weapon_capacity

		if out_for_battle==True:
			return self.weapon_in_battle
