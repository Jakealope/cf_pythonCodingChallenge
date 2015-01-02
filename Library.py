

class Library(object):

	def addShelf(self, newShelf):
		self.shelves.append(newShelf)

	def showLibrary(self):
		print "The contents of the library is: \n"
		for x in self.shelves:
			x.display()
	def nameLibrary(self):
		print "These items are in the %s" % (self.name)

	def __init__ (self, name):
		self.name = name
		self.shelves =  []
	
class Shelf(object):
	def __init__(self, number):
		self.number = number
		self.books = []

	def add(self, newBook):
		self.books.append(newBook)

	def showContents(self):
		print "The contents of the shelf is/are: %s" % (self.number)


class Book(object):

	def __init__ (self, title, author):
		self.title = title
		self.author = author
		self.shelf = None

	def enshelf(self, newShelf):
		if newShelf in theLibrary.shelves:
			newShelf.add(self)
			self.shelf = newShelf
			print"This book has been placed on the shelf numbered: %s" % (self.shelf.number)

		else: 
			print "You need to build the shelf before you can put books on it"

	def unshelf(self):
		self.shelf.remove(self)
		print "This book has been removed from the shelf: %s" % (self.shelf.number)
		self.shelf = None


	def bookList(self):
		print "Title: ", self.title
		print "Author: ", self.author
		if self.shelf:
			print "located on shelf: %s" % (self.shelf.number)
		else: print "This book is not on the shelf"




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



