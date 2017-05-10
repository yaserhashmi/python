'''str = "Hello world!"
print str
print str[0]
print str[2]
print str[2:5]
print str[2:]
print str*2
print str + "TEST"


file = open("main.txt","r+")
file.write("This is the official document, Related to python")
file.close()

print(file)



for x in range(0, 5):
    print(x)

import keyword
print(keyword.kwlist)

count = 0
while(count<3):
    count = count + 1
    print ("the count is:")

#printing the list in reverse
l = ["one","two","three","four"]
for i in l:
    c = l.pop()
    print c

i = 10
while(i>0):
    i -= 1
    print(i)

i = 0
while(i<10):
    i += 1
    print (i)

a = "good work"
for i in a:
    print(i)

for j in range(0,10):
    print j'''

x = "welcome to the python programming"
print x[2:5]
print x[5]
print x[2:25:2]
print x[-5:-3]

#reverse list
list = [1,2,3,4,5,6]
list.reverse()
print (list)

l = [1,2,3,4,5]
p = l[::-1]
print (p)

#rev str
str = "yaserhashmi"
for i in reversed(str):
    print(i)

var = 15
str = "var as string = %s" %(var)
print str

#substitute and template
from string import Template
students = [('ram',90),('sham',60),('rohan',75)]
t = Template("Hi $name u got $marks marks")
for i in students:
    print (t.substitute(name = i[0],marks = i[1]))

#functions
def checkDev(a,b):
    if a%b ==0:
        print("a is divisible by b:")
    else:
        print ("not divisible by b:")
checkDev(10,7)

#odd numbers
x = [1,2,3,4,5,6,7,8,9,10]
for i in x:
    if i%2 == 0:
        print("given number is even:")
    else:
        print ("given number is odd:")

#transpose of matrix nested loop
m = [[1,2],[3,4],[5,6]]
r = [[0,0,0],[0,0,0]]
for i in range(len(m)):
    for j in range(len(m[0])):
        r[j][i] = m[i][j]

for x in r:
    print x



