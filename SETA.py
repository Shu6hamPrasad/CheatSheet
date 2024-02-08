lines.txt
A BOY IS PLAYING OUTSIDE
THE PLAYGROUND IS BIG
BANYAN TREE IS IN THE GROUND

answer 1(a):
r1=[]
def ablines():
 fh=open("C:\\Users\\Pankaj Sir\\Desktop\\lines.txt",'r')
 r1=fh.readlines()
 for i in r1:
if i[0]=="A" or i[0]=="B":
print(i)
ablines()

answer 1(b):
stack = []
def push(val):
 stack.append(val)
 print(val, "added to stack.")
def pop():
 if len(stack) <= 0:
return "No elements in stack."
 else:
return stack.pop()
num=int(input("Enter the number of element to be inserted on stack: "))
for i in range(0,num):
 val=int(input("Enter the value to be inserted on the stack"))
 push(val)
num1=int(input("Enter the number of element to be poped from the stack: "))
for i in range(0,num1):
 del1=pop()
 print("Element pop from the stack are:",del1)

answer 2:
import mysql.connector as c
con1=c.connect(host="localhost",user="root",passwd="root",database="school")
mycursor= con1.cursor()
mycursor.execute("select * from student where percentage>90")# statement1
data=mycursor.fetchall()
for i in data:
 print(i)
mycursor.execute("select * from student order by percentage desc")# statement2
data2=mycursor.fetchall()
for i in data2:
 print(i)
mycursor.execute("update student set percentage=90 where sid='s1' ")# statement3
data3=mycursor.fetchall()
for i in data3:
 print(i)
mycursor.execute("select max(percentage) from student")#statement4
data4=mycursor.fetchall()
for i in data4:
 print(i)
con1.commit()
