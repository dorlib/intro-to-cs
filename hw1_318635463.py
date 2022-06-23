#Skeleton file for HW1 - Spring 2022 - extended intro to CS

#Add your implementation to this file

#you may NOT change the signature of the existing functions.
#you can add new functions if needed.

#Change the name of the file to include your ID number (hw1_ID.py).

#Question 4a
def replace(text, alphabet, new_alphabet):
    t = text
    newText = ""
    numOfDigits = len(t)
    
    for i in range(numOfDigits):
        if t[i] not in alphabet:
            newText += t[i]
        if t[i] in alphabet:
            j = alphabet.find(t[i])
            newText += new_alphabet[j]
        
    return newText
          

#Question 4b
def is_pal(text):
    t = text
    i = 0
    control = True

    while i < len(t):
        if t[i] == " ":
            t = t.replace(" ","")
        if t[i] == ".":
            t = t.replace(".","")
        i = i + 1
            
    numOfDigits = len(t)
    
    for i in range(numOfDigits):
        if i > (numOfDigits -i -1):
            return control
        elif t[i] != t[numOfDigits-i-1]:
            control = False
            return control
    return control
            

#Question 4c
def num_different_letters(text):
    chars = "abcdefghijklmnopqrstuvwxyz"
    sum = 0
    i = 0
    while i < len(chars):
        if chars[i] in text:
            sum = sum + 1
            i += 1
        else:
            i += 1
    return sum 

#Question 4d
def most_frequent(text):
    lst = []
    sums = []
    i = 0
    
    while i < len(text):
        lst.append(text[i])
        i += 1
        
    counts = []
    for i in range(len(lst)):
        s = 0
        for j in range(len(lst)):
            if lst[i] == lst[j]:
                s += 1
        sums.append(s)

    max = 0
    for i in range(len(lst)):
        if sums[i] > max:
            max = sums[i]

    c = []
    for i in range(len(lst)):
        s = 0
        for j in range(len(lst)):
            if lst[i] == lst[j]:
                s += 1
        c.append(s)

    letter = ""
    for i in range(len(lst)):
        if c[i] == max:
            letter = lst[i]
    
    return letter

    
#Question 4e
def kth_order(text, k):
    lst = []
    sums = []
    i = 0
    
    while i < len(text):
        lst.append(text[i])
        i += 1

    counts = []
    for i in range(len(lst)):
        s = 0
        for j in range(len(lst)):
            if lst[i] == lst[j]:
                s += 1
        sums.append(s)

    newsums = []
    for i in range(len(sums)):
        if sums[i] in newsums:
            pass
        else:
            newsums.append(sums[i])
    newsums.sort(reverse = True)
      
    c = []
    for i in range(len(lst)):
        s = 0
        for j in range(len(lst)):
            if lst[i] == lst[j]:
                s += 1
        c.append(s)
      
    kth = newsums[k-1]
    letter = ""
    for i in range(len(lst)):
        if c[i] == kth:
            letter = lst[i]
    
    return letter

#Question 5
def calc(expression):

    if expression == "":
        return ""
    
    lst = expression.split("'")
    lst.pop(0)
    lst.pop(len(lst)-1)

    str = lst[0]
 
    for i in range(1,(len(lst)//2)+1):
        if lst[2*i-1] == '*':
            str *= int(lst[2*i])
        if lst[2*i-1] == '+':
            str += lst[2*i]
        if lst[2*i-1] == '-':
            sum = 0
            for j in range(len(str)):
                if str[j] == lst[2*i]:
                    sum += 1
            for k in range(len(str)-sum):
                if str[k] == lst[2*i]:
                    str = str.replace(str[j],"")
                    
    return(str)


########
# Tester
########

def test():
    #testing Q4
    if replace("hello world", "abcde fghijkl", "1234567890xyz") != "95zzo6worz4":
        print("error in replace - 1")
    if replace("abcd123", "1", "x") != "abcdx23":
        print("error in replace - 2")

    if not is_pal("go dog"):
        print("error in is_pal - 1")
    if is_pal("anda"):
        print("error in is_pal - 2")
        
    if num_different_letters("aa bb cccc dd ee fghijklmnopqrstuvwxyz") != 26:
        print("error in num_different_letters - 1")
    if num_different_letters("aaa98765432100000000") != 1:
        print("error in num_different_letters - 2")

    if most_frequent("abcdee") != "e":
        print("error in most_frequent - 1")
    if most_frequent("x11x22x33x") != "x":
        print("error in most_frequent - 2")

    if kth_order("aaaabbbccd", 3) != "c":
        print("error in kth_order - 1")
    if kth_order("abcdabcaba", 1) != "a":
        print("error in kth_order - 2")

    #testing Q5
    if calc("'123321'*'2'") != "123321123321":
        print("error in calc - 1")
    if calc("'Hi there '*'3'+'you2'") != "Hi there Hi there Hi there you2":
        print("error in calc - 2")
    if calc("'hi+fi'*'2'*'2'") != "hi+fihi+fihi+fihi+fi":
        print("error in calc - 3")
    if calc("'a'*'2'+'b'*'2'") != "aabaab":
        print("error in calc - 4")
    if calc("'a'*'2'+'b'*'2'-'b'") != "aaaa":
        print("error in calc - 5")
    if calc("'a'*'2'+'b'*'2'-'c'") != "aabaab":
        print("error in calc - 6")
