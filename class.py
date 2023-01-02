class Banana:
	"A tasty tropical fruit"
	food_group = 'fruit'
	colors = [
		'green', 'green-yellow', 
		'yellow', 'brown spotted', 'black'
		]

	def peel(self):
		self.peeled = True

	def set_color(self,color):
		if color in self.colors:
			self.color = color
		else:
			raise ValueError(f'A banana cannot be {color}')

	# class method and static method

	def check_color(cls, color):
		"""Test a color string to see if it is valid"""
		return color in cls.colors

	def make_greenie(cls):
		"""Create a green banana object"""
		banana = cls()
		banana.set_color('green')
		return banana

	def estimate_calories(num_bananas):
		"""Given 'num_bananas', estimate the number of calories"""
		return num_bananas * 105

	# Magic attributes and methods
	def __str__(self):
			return f'A {self.color} {self.__class__.__name__}'

	# initialized method
	def __init__(self, color='green'):
		if not self.check_color(color):
			raise ValueError(
				f'A {self.__class__.__name__} cannot be {color}'
				)
		else:
			self.color = color



# make an object (instance) of the Banana class
my_banana = Banana()
my_banana.set_color("yellow")
my_banana.peel()

# look at the attributes of my_banana
print(
	f"Food group of my_banana is {my_banana.food_group}\n",
	f"The color of my_banana is {my_banana.color}\n",
	f"Is my_banana peeled? {my_banana.peeled}\n"
	)


# check if red is valid color using classmethod, check_color
Banana.check_color = classmethod(Banana.check_color)
color = 'red'
print(f"Can a banana be {color} ? {Banana.check_color('red')}\n")


# make a green banana using make_greenie function
Banana.make_greenie = classmethod(Banana.make_greenie)
green_banana = Banana.make_greenie()
print(f'The color of the green_banana is {green_banana.color}\n')


# Calculate the calories of 3 bananas
print(f"The total calories of 3 bananas is {Banana.estimate_calories(3)}\n")



# Using __class__ attribute to retrieve its class, and then using the class object's __name__ attribute to get the class name

info_of_my_banana = my_banana.__str__()
print(info_of_my_banana, '\n')


print(my_banana, '\n')

# make a new banana withouth passing color parameter
my_new_banana = Banana()

print(my_new_banana)