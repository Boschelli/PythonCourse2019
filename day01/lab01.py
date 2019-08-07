## Trick and explanation of base conversion
## http://www.purplemath.com/modules/base_why.htm

"""convert positive integer to base 2"""

def binarify(num):
    # Unnecessary variable assignment
    q=num
    # Creates results
    result=""
    # Creates flipped results
    result2=""
    # Loops until residual is less than 1
    while(q>=1):
        # Adds modulo to result string
        result+=str(q%2)
        # Divides number by 2
        q=int(q/2)
    #Flips results
    for i in result:
        result2= i + result2
    return (result2)

# Function test
binarify(5)

"""convert positive integer to a string in any base"""

def int_to_base(num, base):
    # Unnecessary variable assignment
    q=num
    # Creates results
    result=""
    # Creates flipped results
    result2=""
    # Loops until residual is less than 1
    while(q>=1):
        # Adds modulo to result string
        result+=str(q%base)
        # Divides number by desired base
        q=int(q/base)
    # Flips results
    for i in result:
        result2= i + result2
    return (result2)

# Function test
int_to_base(5,2)

"""take a string-formatted number and its base and return the base-10 integer"""
##Required Flipped Formatted Strings
def base_to_int(string, base):
    # Creates results
    result=0
    # Sets exponent and adjusts for zero-th power
    k=len(string)-1
    # Loops through characters and multiplies them against exponent
    for i in string:
        result+=(int(i)*(base**k))
        # Decreases exponent
        k-=1
    return result

#Function Test
base_to_int("10",2)


"""add two numbers of different bases and return the sum"""
def flexibase_add(str1, str2, base1, base2):
    # Converts first number to base 10
    num1=base_to_int(str1,int(base1))
    # Converts second number to base 10
    num2=base_to_int(str2,int(base2))
    # Returns sum
    return(num1+num2)

#Function Test
flexibase_add('101','1111','2','2')

"""multiply two numbers of different bases and return the product"""
def flexibase_multiply(str1, str2, base1, base2):
    # Converts first number to base 10
    num1=base_to_int(str1,int(base1))
    # Converts second number to base 10
    num2=base_to_int(str2,int(base2))
    # Returns sum
    return(num1*num2)

#Function Test
flexibase_multiply('10','1111','10','2')


"""given an integer, return the Roman numeral version"""
def romanify(num):
    # Initiates result string
    result=""
    # The number of times each numeral goes into a number
    m=0

    # Finds the max number of times 1000 goes into the number
    m=num//1000
    # Subtracts the maximum number of times
    num-=(1000*m)
    # Adds the appropriate number of Roman Numerals
    result+=("M"*m)

    # See Comments for 1000
    m=num//500
    num-=(500*m)
    result+=("D"*m)

    # See Comments for 1000
    m=num//100
    num-=(100*m)
    result+=("C"*m)

    # See Comments for 1000
    m=num//50
    num-=(50*m)
    result+=("L"*m)

    # See Comments for 1000
    m=num//10
    num-=(10*m)
    result+=("X"*m)

    # See Comments for 1000
    m=num//5
    num-=(5*m)
    result+=("V"*m)

    # See Comments for 1000
    m=num//1
    num-=(1*m)
    result+=("I"*m)

    # Returns results
    return result

# Function test
romanify(12367)


# Copyright (c) 2014 Matt Dickenson
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
