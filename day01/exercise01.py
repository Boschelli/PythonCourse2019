## Fibonacci sequence
## X_[i] = X_[i-1] + X_[i-2], where X_1 = 1, X_2 = 1
## 1,1,2,3,5,8,....

## Write a for loop, while loop, or function (or all three!) to create a
## list of the first 10 numbers of the fibonacci sequence


## Very Ineffectient For Loop For Fibonacci Sequence
fib=[]
for i in range(0,10):
    if i <= 1:
        fib.append(i)
    else:
        fib.append(fib[i-2]+fib[i-1])
        #fib.append(fib[i+1]+fib[i])
print(fib)



"""return true if there is no e in 'word', else false"""
def has_no_e(word):
    for i in word:
        if i == 'e':
            return False
    return True



"""return true if there is e in 'word', else false"""
def has_e(word):
    for i in word:
        if i == 'e':
            return True
    return False


"""return true if word1 contains only letters from word2, else false"""
def uses_only(word1, word2):
    for i in word1:
        if i not in word2:
            return False
    return True
uses_only('Cat','Caterpillar')

"""return true if word1 uses all the letters in word2, else false"""
def uses_all(word1, word2):
    for i in word2:
        if i not in word1:
            return False
    return True
uses_all("Caterpillar","Cat")

"""true/false is the word in alphabetical order?"""
def is_abecedarian(word):
    word_list=[i for i in word]
    for i in (range(0,len(word_list)-1)):
        if word_list[i] > word_list[i+1]:
            return False
    return True
is_abecedarian('cat')
