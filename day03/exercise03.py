## Write a function that counts how many vowels are in a word
## Raise a TypeError with an informative message if 'word' is passed as an integer
## When done, run the test file in the terminal and see your results.
def count_vowels(word):
    vowels=['a','e','i','o','u']
    numVowels=0
    if type(word)!= str:
        raise TypeError("Object Passed Is Not A String")
    for letter in word.lower():
        if letter.isalpha() != True:
            raise TypeError("Object Passed Contained No Letters")
        if letter in vowels:
            numVowels+=1
    return numVowels
