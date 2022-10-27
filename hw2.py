import sys
import math
import string

def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e=[0]*26
    s=[0]*26
    
    

    with open('e.txt',encoding='utf-8') as f:
        for line in f:
            #strip: removes the newline character
            #split: split the string on space character
            char,prob=line.strip().split(" ")
            #ord('E') gives the ASCII (integer) value of character 'E'
            #we then subtract it from 'A' to give array index
            #This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')]=float(prob)
    f.close()

    with open('s.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    f.close()

    return (e,s)

def shred(filename):
    #Using a dictionary here. You may change this to any data structure of
    #your choice such as lists (X=[]) etc. for the assignment
    d = dict.fromkeys(string.ascii_uppercase, 0)
    with open(filename,encoding='utf-8') as f:
        for line in f:
            line.strip().split(" ")
            for c in line:
                if c.isalpha():
                    if c.islower():
                        c = c.upper()
                    d[c] = d[c] + 1
                    
        f.close()
        print("Q1")
        for i in d: 
            print(i, ' ', d[i])
            
    return d

def q2():
    print('Q2')
    x = alphaCount['A']*math.log(e[0])
    print('%.4f'%x)
    y = alphaCount['A']*math.log(s[0])
    print('%.4f'%y)

def logDomain(alphaCount):
    fe = 0
    fs = 0
    h = 0
    i = 0
    for j in alphaCount:
        fe = fe + (alphaCount[j] * math.log(e[h]))
        h = h + 1
    fe = fe + math.log(0.6)
    h = 0
    for j in alphaCount:
        fs = fs + (alphaCount[j] * math.log(s[h]))
        h = h + 1
    fs = fs + math.log(0.4)
    print("Q3")
    print('%.4f'%fe)
    print('%.4f'%fs)
    
    return fe, fs

def q4(fe, fs):
    if fs - fe >= 100:
        print(0.0000)
        return
    if fs - fe <= -100:
        print(1.0000)
        return
    
    pyex = 1/(1+(math.e**(fs-fe)))
    print("Q4")
    print('%.4f'%pyex)
    return

alphaCount = shred('letter.txt')
e, s = get_parameter_vectors()
q2()
fe, fs = logDomain(alphaCount)
q4(fe, fs)