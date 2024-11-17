## OOPS PROJECT
'''you are an admin of rgpv panel and we are creating  management site for student database management'''
import string
import random
from pathlib import Path
import json


class Students:
    data=[]
    database = "student.json"
    
    with open(database) as fs:
        data=json.loads(fs.read())
    
    @classmethod
    def updatedata(cls): #cls se mai class ko target krrhi hu qki mne class method use kiya hai
        with open(cls.database,"w") as fs:
            fs.write(json.dumps(cls.data))
            
    @classmethod
    def Randomid(cls):
        alpha=random.choices(string.ascii_letters,k=3)
        numbers=random.choices(string.digits,k=3)
        spchar= random.choices("!@#$%^&*",k=2)
        id=alpha+numbers+spchar
        random.shuffle(id)
        return "".join(id)
    
    def registerstudent(self):
        stu={
            "id": Students.Randomid(),
            "name": input("please tell your name"),
            "email": input("tell your email"),
            "password": input("enter your password"),
            "age": int(input("tell your age"))
        }
        Students.data.append(stu)
        Students.updatedata()
        
    def readsinglestudent(self):
        id = input("enter id: ")
        password= input("enter your password: ")
        student= [i for i in Students.data if i["id"]==id and i["password"]==password]
        
        if len(student)==0:
            print("sorry wrong credentials try again")
        else:
            for i in student[0]:
                print()
                print(f"{i}: {student[0][i]}")

    def accessdatabase(self):
        a=Students.data
        counter=1
        print()
        print(counter)
        print()
        for i in a:
            for j in i:
                print(f"{j}: {i[j]}")
            counter=+1
            
    def updatestudent(self):
        id = input("enter id: ")
        password= input("enter your password: ")
        student= [i for i in Students.data if i["id"]==id and i["password"]==password]
        
        if len(student)==0:
            print("wrong credentials")
        else:
            print("either write new name or press enter to skip")
            stu={
                "name": input("update your name"),
                "email": input("tell your new email"),
                "password": input("enter your new password"),
                "age": int(input("tell your new age"))
            }
            
        if stu["name"]=="":
            stu["name"]=student[0]["name"]
            
        if stu["email"]=="":
            stu["email"]=student[0]["email"]
        if stu["password"]=="":
            stu["password"]=student[0]["password"]
        if stu["age"]==0:
            stu["age"]=student[0]["age"]
        
        for i in stu.keys():
            if stu[i]==student[0][i]:
                continue
            else:
                student[0][i]=stu[i]
            
            
        self.updatestudent()
        
    def deletestudent(self):
        id = input("enter id: ")
        password= input("enter your password: ")
        student= [i for i in Students.data if i["id"]==id and i["password"]==password]
        
        if len(student)==0:
            print("wrong credentials")
        else:
            check=print("are you sure you want to delete press y/n")

            if check=='y':
                studentindex=Students.data.index(student[0])
                Students.data.pop(studentindex)
                self.updatedata()
            elif check=="n":
                pass

            else:
                print("sahi bata bhai")
        
obj= Students()

while True:
    print("""
            select an option:  
            1. register as student 
            2. login student profile
            3. Access database
            4. update student data
            5. delete student data
            6. exit the application
    """)
    n=int(input("tell your response"))

    if n==6:
        exit(0)
    elif n==1:
        #self likha hai to usko work krne k liye ek object chahiye, agar mai obj create nahi krti to error aata //ya fir self hatana pdta
        obj.registerstudent()

    elif n==2:
        obj.readsinglestudent()

    elif n==3:
        obj.accessdatabase()

    elif n==4:
        obj.updatestudent()

    elif n==5:
        obj.deletestudent()
        
    else:
        print("sahi bata")
