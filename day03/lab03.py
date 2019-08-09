import string
## 1. write tests in lab03_tests.py
## 2. then code for the following functions

## Raising errors is more common when developing ------------------------

## These functions all take a single string as an argument.
## Presumably your code won't work for an int
## raise a built-in (or custom!) exception if fed an int

## make all characters capitalized
def shout(txt):
	try:
		result = txt.upper()
	except AttributeError:
		print("Be Sure To Only Enter A String")
	return txt.upper()


## reverse all characters in string
def reverse(txt):
	if type(txt)!=str:
		raise TypeError("Be Sure To Only Enter A String")
	result=""
	for i in txt:
		result=i+result
	return result


## reverse word order in string
def reversewords(txt):
	if type(txt)!=str:
		raise TypeError("Be Sure To Only Enter A String")
	result=""
	for word in txt.split():
		result=word+" "+result
	return result


## reverses letters in each word
def reversewordletters(txt):
	if type(txt)!=str:
		raise TypeError("Be Sure To Only Enter A String")
	result=""
	for word in txt.split():
		result+=reverse(word)+ " "
	return result


## change text to piglatin.. google it!
def piglatin(txt):
	if type(txt)!=str:
		raise TypeError("Be Sure To Only Enter A String")
	vowels=['a','e','i','o','u','y']
	result=""
	for word in txt.split():
		newWord=""
		infront=""
		for i in range(0,len(word)):
			if word[i].lower() in vowels:
				infront+='ay'
				newWord=word[i:]
				newWord+=infront
				break
			infront+=word[i]
		result+=newWord + " "
	return result[:-1]



## Try/catch is more common when using
## someone else's code, scraping, etc. -----------------------------------

## Loop over this string and apply the reverse() function.
## Should throw errors if your exceptions are being raised!
## Write a try/catch to handle this.
string_list = ["hi", "hello there", 5, "hope this works", 100, "will it?"]

for i in string_list:
	try:
		print(reverse(i))
	except:
		continue
