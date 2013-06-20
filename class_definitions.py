# Example for my intro to programming course.
# Object-oriented approach to solving the age-old sequence logic puzzle about
# the fox, the goose, and the corn.
# The farmer has to get all three across the river on a small boat, in which
# he can only fit one item.
# He can't leave the fox and the goose by themselves or the fox will eat the
# goose.  He can't leave the goose alone with the corn or the goose will eat
# all the corn.  How does he get all three across the river, one at a time?
# 
# Here I'll define five classes.
# fox goose corn river boat
class Goose:
	"""
	A goose.  Just an arbitrary representation of a goose who likes corn.
	"""
	def __init__(self):
		self.legs = 2
		self.hungry = True
		
class Fox:
	"""
	A fox.  Just an arbitrary representation of a fox who will eat your goose
	if you leave the two alone.
	"""
	def __init__(self):
		self.legs = 4
		self.hungry = True