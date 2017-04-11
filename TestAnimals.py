import unittest 
from animals import *

class TestTheAnimals(unittest.TestCase):

# In the test class's setUpClass() method, create an instance of Animal and Dog.
	@classmethod
	def setUpClass(self):
		self.animal = Animal('Buddy', 'Panda')
		self.angus = Dog('Angus')
		# print(dir(self.animal))

	

# Ensure Animal object has the correct name property.
	def test_animal_name_property_has_correct_value(self):
		self.assertEqual(self.animal.name, 'Buddy')

# Ensure Dog object has the correct species property
	def test_animal_species_property_has_correct_value(self):
		self.assertEqual(self.animal.species, 'Panda')

# Set a species and verify that the object property of species has the correct value.
	def test_dog_species_property_has_correct_value(self):
		self.assertEqual(self.angus.species, 'Dog')		

# Ensure invoking the walk() method set the correct speed on the both objects.
	def test_walk_method_sets_speed(self):
		legs = 4		
		self.animal.set_legs(legs)
		self.animal.walk()

		self.angus.set_legs(legs)
		self.angus.walk()

		self.assertEqual(self.animal.speed, 0.4)
		self.assertEqual(self.angus.speed, 0.8)

# Ensure self.animal is instance of Animal Class
	def test_animal_is_correct_type(self):
		self.assertIsInstance(self.animal, Animal)
	
# Ensure the dog object angus is an instance of Dog Class.
	def test_dog_is_correct_type(self):
		self.assertIsInstance(self.angus, Dog)
