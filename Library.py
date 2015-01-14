# This program is showing the hierarchy of classes using a 
# library as an example with shelves and books

class Library(object):
	# Adds a shelf
	def addShelf(self, newShelf):
		self.shelves.append(newShelf)
	# Lets the user know what library they are in
	def showLibrary(self):
		print "The contents of the library is: \n"
		# Loops through the shelves displaying contents
		for x in self.shelves:
			x.display()
	# The library knows what books it contains
	def nameLibrary(self):
		print "These items are in the %s" % (self.name)
	# Initializes the library
	def __init__ (self, name):
		self.name = name
		self.shelves =  []
	
class Shelf(object):
	# Shelf initializer. The shelves start out empty 
	def __init__(self, number):
		self.number = number
		self.books = []
	# Adds books to the shelf
	def add(self, newBook):
		self.books.append(newBook)
	# Displays the contents of the shelf
	def showContents(self):
		print "The contents of the shelf is/are: %s" % (self.number)


class Book(object):
	# Initializes the book class
	def __init__ (self, title, author):
		self.title = title
		self.author = author
		self.shelf = None
	#This function adds the book onto the shelf and the book will
	#know what shelf it is on. If there is no shelf, it builds one.
	def enshelf(self, newShelf):
		if newShelf in theLibrary.shelves:
			newShelf.add(self)
			self.shelf = newShelf
			print"This book has been placed on the shelf numbered: %s" % (self.shelf.number)
		#This will let the user know that they didn't build 
		#a shelf to put the book on..
		else: 
			print "You need to build the shelf before you can put books on it"
	#Unshelf removes the book from the shelf. 
	#If there is only one book on the shelf, it removes the shelf.
	def unshelf(self):
		self.shelf.remove(self)
		print "This book has been removed from the shelf: %s" % (self.shelf.number)
		self.shelf = None

	#This displays the books on the shelves.
	def bookList(self):
		print "Title: ", self.title
		print "Author: ", self.author
		if self.shelf:
			print "located on shelf: %s" % (self.shelf.number)
		else: print "This book is not on the shelf"



#A couple tests to show that the library indeed works.
theLibrary = Library("West Seattle Library")
theLibrary.nameLibrary()
s1 = Shelf("1")
theLibrary.addShelf(s1)
b1 = Book("The Big Bad Wolf and his Addiction to Asparagus pt2", "Bob Saget")
b1.enshelf(s1)
b1.bookList()


s2 = Shelf("2")
theLibrary.addShelf(s2)
b2 = Book("How to steer a Steer", "One Eye'd Joe")
b2.enshelf(s2)
b2.bookList()



