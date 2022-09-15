
import csv
import random
file='vr.csv'
print("welcome to the matrimony system")

def insertion():
    name=input("enter name:")
    age=input("enter age:")
    occupation=input("enter occupation")
    gender=input("enter gender:")
    id=random.randint(1,1000)  
    marriage_preference=input("enter the preference")
    insert_data=[name,id,age,gender,occupation,marriage_preference]
    print(insert_data)
        with open(file.filename,'a',newline='')as f:
            csvwriter=csv.writer(f)
            csvwriter.writerow([name,age,occupation,gender,id,marriage_preference])
        print("details added")
def Retrival():
    with open(file,'r') as f:
        print('name\ age\occupation\gender\id\marriage_preference')    
        data=csv.reader(f)
        for r in list(data):
            print(f'{r[0]}\t\t{r[1]}\t\t{r[2]}\t\t{r[3]}\t\t{r[4]}\t\t{r[5]}\t\t{r[6]}') 
def Searching():
    search_elt=input("Enter the name to search:")
        print(" f'{r[0]}\t\t{r[1]}\t\t{r[2]}\t\t{r[3]}\t\t{r[4]}\t\t{r[5]}\t\t{r[6]}')
        data=csv.reader (file)
        namelist=list(data)
s_result=[names for names in namelist if search elt in names]
    if len(s_result)>0:
       for row in s result:

        print(f'{r[0]}\t\t{r[1]}\t\t{r[2]}\t\t{r[3]}\t\t{r[4]}\t\t{r[5]}\t\t{r[6]}')
        else:
        print("No Results Found")
def Deletion(self):
    name_elt input("Enter the persons name to delete:")
    with open(self.filename, 'r') as file: I
data-csv.reader (file) namelist=list(data)
f_result-[names for names in namelist if name elt Innanes[0]] with open(self.filename, 'w',newline="") as file:
csvwriter csv.writer(file)
csvwriter.writerows(f_result) if(len(f_result)= len(namelist)):
    print("Nothing is available to delete")
else:
    print("updated list")
        
def menu():
    print("menu")
    print("0.Exit")
    print("1.Insertion")
    print("2.Modification")
    print("3.Retreival")
    print("4.Searching")
    print("5.Recommandation")
    print("6.Deletion")
    mychoice=None
    try:
        mychoice=eval(input("enter the choice"))
    except:
        logging.error("enter the choice as number")
    return mychoice
while True:
if (mychoice==0):
    exit()
elif(mychoice==1):
    insertion()
elif(mychoice==2):
    Modification()    
elif(mychoice==3):
    Retrival()
elif(mychoice==4):
    Searching() 
elif(mychoice==5):
    Recommandation()      
elif(mychoice==6):
    Deletion()
else:
    pass    
