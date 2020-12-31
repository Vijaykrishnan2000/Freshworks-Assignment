import time
import json
import sys

database={}
Db_size=pow(1024,3)
JSON_size=16*pow(1024,2)

def create(key,val,timer=0):
    if key in database:
        print("Error: Create is invoked for an existing key")
    else:
        if(key.isalnum() and len(key)<=32):
            if (len(database)< Db_size and len(val)<= JSON_size):
                if timer==0:
                    data=json.dumps([val,timer])
                else:
                    data=json.dumps([val,time.time()+timer])
                database[key]=data
                print("DB added successfully")
            else:
                print("Error: Memory limit exceeded")
        else:
            print("Error: Key is not Valid")

def read(key):
    if key in database:
        data=json.loads(database[key])
        if time.time()<data[1] or data[1]==0:
            z={data[0]:key}
            return json.dumps(z)
        else:
            print("Error: Time-To-Live for the key has expired")
        
    else:
        print("Error: Read is invoked for inaccessible key")

def delete(key):
    if key in database:
        data=json.loads(database[key])
        if time.time()<data[1] or data[1]==0:
            del database[key]
            print("Delete sucessfull")
        else:
            print("Error: Time-To-Live for the key has expired")
    else:
        print("Error: Delete is invoked for inaccessible key")
        
if __name__ == "__main__":
    print("Enter the number to invoke the function \n1.CREATE \n2.READ \n3.DELETE \n4.Exit\n")
    while(1):
        n=int(input())
        if(n==1):
            key=str(input("Key: "))
            value=str(input("Value: "))
            timer=int(input("Time-to-Live for key: "))
            create(key,value,timer)
            print()
        elif(n==2):
            key=str(input("Key: "))
            print(read(key))
            print()
        elif(n==3):
            key=str(input("Key: "))
            print(delete(key))
            print()
        else:
            exit()
        
            
