#QUESTION 1 :
print("QUESTION 1")
string=input("ENTER A STRING:")
find=input("ENTER THE WORD/CHARACTER:")
print("THE NO. OF OCCURENCES OF ",find," IN ",string," = ",string.count(find))

#QUESTION 2:
print("QUESTION 2")
day=int(input("ENTER  DAY"))
month=int(input("ENTER MONTH"))
year=int(input("ENTER YEAR"))
if (day<1 or day>31)&(month<1 or month>12)&(year<1800 or year>2025):
    print("INVALID DATE OR YEAR OR MONTH")
elif day==31 and month==12 :
    print("NEXT DATE = 1/1/",year+1)
elif day==31 and month in [1,3,5,7,8,10] :
    print("NEXT DATE = 1/",month+1,'/',year)
elif day==30 and month not in [1,3,5,7,8,10]:
    print("NEXT DATE = 1/",month+1,"/",year)
elif day==28 and month==2:
    if year%100==0 & year&400==0:
        print("NEXT DATE = 29/2/",year)
    elif year%4==0:
        print("NEXT DATE = 29/2/",year)
    else :
        print("NEXT DATE = 1/3/",year)
else :
    print("NEXT DATE = ",day+1,"/",month,"/",year)
#QUESTION 3:
print("QUESTION 3")
L=[3,9,10]
N=[]
for i in L:
    N.append((i,i**2))
print(N)    
#QUESTION 4:
print("QUESTION 4")
usergrade=int(input("ENTER GRADE POINT :-"))
if usergrade==4:
    print("Your Grade is 'D' and Poor performance" )
elif usergrade==5:
    print("Your Grade is 'C' and Below Average performance")
elif usergrade==6:
    print("Your Grade is 'C+' and Average performance")
elif usergrade==7:
    print("Your Grade is 'B' and Good performance")    
elif usergrade==8:
    print("Your Grade is 'B+' and Very Good performance")    
elif usergrade==9:
    print("Your Grade is 'A' and Excellent performance")
elif usergrade==10:
    print("Your Grade is 'A+' and Outstanding performance")
else:
    print("INVALID GRADE POINT")

#QUESTION 5:
print("QUESTION 5")
n=6
for i in range(n):
    for j in range(i):
        print(' ',end='')
    for j in range(2*(n-i)-1):
        print(chr(65+j),end='')
    print()    

#QUESTION 6:
print("QUESTION 6")    
D={}    
while True :
    S=int(input("ENTER SID:"))
    N=input("ENTER NAME:")
    D[S]=N
    U=input("DO YOU WANT TO ENTER MORE DATA? 'Y'(YES) or 'N'(NO)")
    if U=='Y':
        continue
    else :
        break
for i in D:
    print("SID = ",i,"NAME = ",D[i])
s=list(D.values())
s.sort()
print("sorted dictionary names= ",s)
l=list(D.keys())
l.sort()
print("sorted dictionary sid= ",l)
F=int(input("ENTER SID"))
print("SID = ",F," NAME = ",D[F])

    
#QUESTION 7:
print("QUESTION 7")

nterms = int(input("ENTER NO. OF TERMS "))
n1, n2 = 0, 1
c= 0
Sum=0
if nterms <= 0:
    print("INVALID INPUT")
elif nterms == 1:
    print("Fibonacci sequence")
    print(n1)
    print("AVERAGE = ",n1)
else:
    print("Fibonacci sequence:")
    while c < nterms:
        print(n1)
        nth = n1 + n2
        Sum+=n1
        n1 = n2
        n2 = nth
        c += 1
    print("AVERAGE = ",Sum/nterms)    


#QUESTION 8:
print("QUESTION 8")    
set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}
seta= set1.symmetric_difference(set2)
print("a part =",seta)
setb= set3.symmetric_difference(seta)
print("b part =",setb)
integer={1,2,3,4,5,6,7,8,9,10}
setd=integer.symmetric_difference(set1)
print("d part =",setd)
setx=set1.union(set2)
setz=setx.union(set3)
sete=setz.symmetric_difference(integer)
setE=set()
for i in sete:
    if i<=10:
        setE.add(i)
print("e part =",setE)



    





















































































































































    
    
