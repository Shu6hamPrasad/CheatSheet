#prog 1(i)
def countlines():
 f=open("C:\\Users\\Pankaj Sir\\Desktop\\data.txt","r")
 count=0
 data=f.readlines()
 for d in data:
if d[0]== "#":
count=count+1
 print("Number of lines starting with #= ",count)
f.close()
countlines()


#prog1(ii-a)
import pickle
def create_record():
 f=open("C:\\Users\\Pankaj Sir\\Desktop\\hospital.dat","wb")
 Patientid=int(input("Enter Patient id: "))
 Patient_Name=input("Enter Name of Patient:")
 Disease= input("Enter Disease:")
 record=[Patientid,Patient_Name, Disease]
 pickle.dump(record,f)
f.close()
create_record()

#prog 1(ii-b)
import pickle
def display_record():
 f=open("C:\\Users\\Pankaj Sir\\Desktop\\hospital.dat","rb")
 try:
while True:
rec=pickle.load(f)
if rec[2]=="fever" or rec[2]=="cough":
print(rec)
 except EOFError:
f.close()
display_record()

Answer2:
#Statement 1 – con1.cursor()
#Statement 2 – mycursor.execute(query)
#Statement 3 – con1.commit()
#Statement 4 – con1.close()

import mysql.connector as mysql
def sql_data():
 con1=mysql.connect(host="localhost",user="root", password="root", database="school1")
 mycursor= con1.cursor() #Statement 1
 Rollno=int(input("Enter Roll Number ::"))
 Name=input("Enter name :: ")
 Class=int(input("Enter class :: "))
 Marks=int(input("Enter Marks :: "))
 query="insert into student values({},'{}',{},{})".format(Rollno,Name,Class,Marks)
 mycursor.execute(query) #Statement 2
 con1.commit() # Statement 3
 print("Data Added successfully")
 con1.close() #Statement 4
sql_data()
