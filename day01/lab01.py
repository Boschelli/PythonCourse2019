## Trick and explanation of base conversion
## http://www.purplemath.com/modules/base_why.htm

"""convert positive integer to base 2"""
##Needs To Be Reversed
def binarify(num):
    q=num
    result=""
    result2=""
    while(q>=1):
        result+=str(q%2)
        q=int(q/2)
    for i in result:
        result2= i + result2
    return (result2)

binarify(5)

"""convert positive integer to a string in any base"""
##Needs To Be Reversed
def int_to_base(num, base):
    q=num
    result=""
    result2=""
    while(q>=1):
        result+=str(q%base)
        q=int(q/base)
    for i in result:
        result2= i + result2
    return (result2)
int_to_base(5,2)

"""take a string-formatted number and its base and return the base-10 integer"""
##Required Flipped Formatted Strings
def base_to_int(string, base):
    result=0
    k=len(string)-1
    for i in string:
        result+=(int(i)*(base**k))
        k-=1
    return result
base_to_int("10",2)


"""add two numbers of different bases and return the sum"""
def flexibase_add(str1, str2, base1, base2):
    num1=base_to_int(str1,int(base1))
    num2=base_to_int(str2,int(base2))
    return(num1+num2)
flexibase_add('101','1111','2','2')

"""multiply two numbers of different bases and return the product"""
def flexibase_multiply(str1, str2, base1, base2):
    num1=base_to_int(str1,int(base1))
    num2=base_to_int(str2,int(base2))
    return(num1*num2)
flexibase_multiply('10','1111','10','2')


"""given an integer, return the Roman numeral version"""
def romanify(num):
    q=num
    result=""
    while(q/1000>=1):
        result+="M"
        q=q-1000
    while(q/500>=1):
        result+="D"
        q=q-500
    while(q/100>=1):
        result+="C"
        q=q-100
    while(q/50>=1):
        result+="L"
        q=q-50
    while(q/10>=1):
        result+="X"
        q=q-10
    while(q/5>=1):
        result+="V"
        q=q-5
    while(q/1>=1):
        result+="I"
        q=q-1
    return result

romanify(5990)


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
