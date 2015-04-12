#Andy Zimmelman
#simple function that prints out
def my_function():
	print "hello from the first function"
my_function()

#simple function that adds two numbers
def sum_numbers(a, b):
        return a + b
x = sum_numbers(4, 2)

print x

def name_greeting(userName, greeting):
        print "Hello, %s , from my 3rd ever function!, I wish you %s" %(userName, greeting)
                
name_greeting("Andy", "good luck")

#build_sentence: string -> string
#consumes: string (info) returns info, then "is a benefit of functions!"

def build_sentence(info):
        print "%s is a benefit of functions!" %(info)
build_sentence("this")

#basic class named MyClass
class MyClass:
        variable = "joooo"

        def function(self):
                print "This is a message inside of the class 'MyClass'"
myobjectx = MyClass()

#to access the variable inside of the newly created object
myobjectx.variable

#print myobject
print myobjectx.variable

#define a Vehicle class
class Vehicle:
        #properties of the Vehicle Class
        name = ""
        kind = "car"
        color = ""
        value = 100.00
        #function description(self) describes the car name, kind, color, and value
        def description(self):
                description_string = "%s is a %s %s worth %.2f." %(self.name, self.kind, self.color, self.value)
                return description_string

#define 2 cars, car1 and car2
        #car1 is Fer, convertible, red, $60,000
        #car2 is Jump, van, blue, $10,000

car1 = Vehicle()
car2 = Vehicle()

car1.name = "Fer"
car1.kind = "convertible"
car1.color = "red"
car1.value = 60000

car2.name = "Jump"
car2.kind = "van"
car2.color = "blue"
car2.value = 10000

#print car1 and car2
print car1.description()
print car2.description()

#dictionaries
#data type similar to arrays, but works with keys and values
##instead of indexes

#database of phonenumbers could be stored using a dictionary
phonebook = {}
phonebook["John"] = 5555551002
phonebook["Andy"] = 5555551000
phonebook["James"] = 5554567890

#alternitavely
phonebook = {
        "John" : 5555551002,
        "Andy" : 5555551000,
        "James" : 5554567890
}

#dictionaries can be iterated over, just like a list
##however, it doesn't keep the order of the values stored in it

#syntax to iterate
#for name, number in phonebook.iteritems():
      #  print "Phone number of %s is %d" %(name, number)

#to remove an index use either
del phonebook["John"]
#or
phonebook.pop("James")

#to phonebook, add Jake with the number 938273443
        #and remove andy from the phonebook
phonebook["Jake"] = 938273443
phonebook.pop("Andy")


if "Jake" in phonebook:
        print "Jake is listed in the phonebook."
if "Andy" not in phonebook:
        print "Andy is not listed in the phonebook."

#import the library
import urllib

#use the library by
#urlib.urlopen(...)

dir(urllib)

#here is a simple generator function
##returns 7 random integers
import random

def lottery():
        #returns 6 numbers between 1 and 50
        for i in xrange(6):
                yield random.randint(1, 50)
        #returns a 7th number between 1 and 20
        yield random.randint(1, 20)
for random_number in lottery():
        print "And the next number is... %d!" % random_number

#write a generator function that returns the Fibonacci series
def fibonacci():
        a, b = 1, 1
        while 1:
                yield a
                a, b = b, a + b

#testing code
import types
if type(fibonacci()) == types.GeneratorType:
        print "Good, the Fibonacci function is a generator."

        counter = 0
        for n in fibonacci():
                print n
                counter += 1
                if counter == 10:
                        break

#list comprehensions
##creates a new list based on another list in a single line
###if we need to create a list of integers which specify the length of
####each word in a certain sentence, but only if the word is not "the"

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
        if word != "the":
                word_lengths.append(len(word))

#using a list comprehension, this is a simplified version
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]

#using list comprehension
#create new list called newlist out of numbers
#newlist should only contain positive numbers from the list

numbers = [1, 4, -3, -2, 2]
newlist = [int(pos) for pos in numbers if pos > 0]

#multi argument func
def multargfunc(first, second, third, *therest):
        print "This is the first, %s " % first
        print "This is the second, %s" % second
        print "This is the third, %s" % third
        print "These are the rest in a list, %s" % list(therest)

#therest variable is a list of variables
#it receives all args which were given to the "multargfunc"
##after the first three args.
#if you call multargfunc(1,2,3,4,5)
multargfunc(1, 2, 3, 4, 5)

#it's possible to send func args by keyword
#so the order of the args doesn't matter
#uses the following syntax
def bar(first, second, third, **options):
        if options.get("action") == "sum":
                print "The sum is: %d" % (first + second + third)
        if options.get("number") == "first":
                return first
result = bar(1, 2, 3, action = "sum", number = "first")
print "Result: %d" % result

#create a foo func and a bar func
#both receives 3 or more args
##foo must return amount of extra args received
###barbar must return True if args w/ keyworkd "magicnumber"
####is worth 7; otherwise, false

def foo(x, y, z, *therest):
        return len(therest)


def barbar(a, b, c, **ayy):
        return ayy["magicnumber"] == 7
        
#regular expressions regexp, regex, or re
##tool for matching patterns in text
### in python, we have the "re" module

#the applications for regex's are wide-spread, but fairly complex
##regex's possibly as last resort because of complexity

#example regex "r"^(From|To}Cc).*?python-list@python.org"
##caret ^: matches text at the beginning of a line
##(From|To|Cc): line has to start with a word separated by |
##| : OR operator regex will match if line starts w/ any words in the group
##.*? : un-greedily match any number of char, except new line \n char
### this un-greed part means to match as few repetitions as possible
##. : any non=newline char
##* : repeat 0 or more times
##? : makes it un-greedy

#exception handling: exceptions handle errors
#suppose you're iterating over a list, and want to iterate over 20 numbs
##but list isn't made of 20 numbers
###after reaches the end of list, instead of having error message
####rest of the numbers be interpreted as another number "0"
def do_stuff_with_number(n):
        print n
the_list = (1,2,3,4,5)

for i in range(20):
        try:
                do_stuff_with_number(the_list[i])
        except IndexError: # Raised when accessing a non-existing index of a list
               do_stuff_with_number(0) 
#another example of excep. handling
#if not an integer, print out "Oops! That isn't a valid number"

while True:
        try:
                x = int(raw_input("Please input a number: "))
                break
        except ValueError:
                print "Oops! That isn't a valid number"

#sets: lists w/ no duplicate entries
##func to collect a list of words used in a paragraph
print set("my name is Jeff and Jeff is my name.".split())

#sets are powerful in python since they have the ability to calculate the
##differences and intersections between other sets
###a list of participants in events A and B:
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])
##find out which members attended both events
a.intersection(b)
#set(['John'])
b.intersection(a)
#set(['John'])

#to find out which persons attended only one of the events
##use "symmetric_difference" method:
a.symmetric_difference(b)
#set(['Jill', 'Jake', 'Eric'])
b.symmetric_difference(a)
#set(['Jill','Jake','Eric'])

#to find out which members attended only one event and not the other
##use the "difference" method:
a.difference(b)
#set(['Jake', 'Eric'])
b.difference(a)
#set(['Jill'])

#to receive a list of all participants, use the "union" method:
a.union(b)
#set(['Jill', 'Jake', 'John', 'Eric'])

#use given lists to print out a set containing all the participants from event A
##that did not attend even B

import json
#two basic formats for JSON data; either in a string or the object data struct.
##Object Datastructure: lists and dictionaries nested inside eachother
###it allows one to use python methods(for lists and dictionaries) to:
#### add, list, search, and remove elements from the datastructure.
##String Format: mainly used to pass the data into another program or
###load into a datastructure

#to encode a data structure to JSON, use the "dumps" method
## Object -> String

json_string = json.dumps([1,2,3,"a","b","c"])

#to load JSON back into a data structure, use the "loads" method.
##it takes a string and turns it back into the json object data structure:

print json.loads(json_string)


#python propreitary data serialization method "pickle" or "cPickle" = faster
import cPickle
pickled_string = cPickle.dumps([1,2,3,"a","b","c"])
print cPickle.loads(pickled_string)

#adds given name and salary pair to salaries_json, and returns it
def add_employee(salaries_json, name, salary):
        salaries = json.loads(salaries_json)
        salaries[name] = salary

        return json.dumps(salaries)
salaries = '{"Andy" : 4000, "Julie" : 3000 }'
new_salaries = add_employee(salaries, "Me", 8000)
decoded_salaries = json.loads(new_salaries)
print decoded_salaries["Andy"]
print decoded_salaries["Julie"]
print decoded_salaries["Me"]

from functools import partial

#partial funcs allow one to derive a func with x params to a func w/ fewer
##params and fixed values set for the more limited func.

#from functools, import partial def multiply(x,y): return x*y
###create a new func that multiplies by 2


#python code for learnpython nigga

#code introspection: the ability to examine classes 
##functions and keywords to know what they are,
###what they do, and what they know

#some funcs and utilities for code introspection
#help()
#dir()
#hasattr()
#id()
#type()
#repr()
#callable()
#issubclass()
#isinstance()
#__doc__
#__name__

#Decorators
#allows for simple modifications to callable objects like:
##funcs, methods, or classes
#functions:

#@Decorator
#def functions(arg):
	#return "Return"
#
#is == to
#def function(arg):
#	return "Return"
#function = decorator(function) #passes the func to decorator; reassigns to funcitons

#a decorator is just another function which takes a functions
##and returns one
#example
def repeater(old_function):
	def new_function(*args, **kwds): 
		#See learnpython.org/page/Multiple%20Function%20Arguments for how *args and **kwds works
		old_function(*args, **kwds) #we run the old funciton
		old_function(*args, **kwds) #we do it twice
	return new_function #have to return new function to assign the value to it

@repeater
def Multiply(x, y):
	print x * y

Multiply(2,3)
#6
#6

#to change the output
def Double_Out(old_function):
	def new_function(*args, **kwds):
		return 2*old_function(*args, **kwds) #modify the return value
	return new_function

#change input
def Double_In(old_function):
	def new_function(arg): #only works if old func has 1 arg
		return old_function(arg*2) #modify the arg passed
	return new_function

#do checking
#def Check(old_function):
#	def new_function(arg):
#		if arg<0: raise ValueError, "Negative Argument" #causes error
#		old_function(arg)
#	return new_function
#
#	#multiply the output by a variable amount
#	def Multiply(multiplier):
#		def Multiply_Generator(old_function):
#			def new_function(*args, **kwds):
#				return multiplier*old_function(*args, **kwds)
#			return new_function
#		return Multiply_Generator #returns the new Multiply_Generator

#@Multiply(3) #Multiply is not a generator, but Multiply(3) is
#def Num(num):
#	return num
#

#decorator factory, returns a decorator that decorates the func w/ one
##arg. 
#factory should take one arg, a type, and return a decorator that makes
##a function that should check if the input is the correct type
#if it is wrong, print "Bad Type" as an error
def type_check(correct_type):
    def check(old_function):
        def new_function(arg):
            if (isinstance(arg, correct_type)):
                return old_function(arg)
            else:
                print "Bad Type"
        return new_function
    return check

@type_check(int)
def times2(num):
    return num*2

print times2(2)
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print first_letter('Hello World')
first_letter(['Not', 'A', 'String'])


