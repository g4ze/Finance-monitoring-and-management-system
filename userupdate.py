from fetcher import *
from variables import *
class userupdate:
    def newUser(self,name):
        print((f'-----------------I am now updating user, {name}******').upper())
        print('Enter the details')
        
        
        job=input('Job: ')
        income=input('Income: ')
#       WE WILL NOW MAKE A NEW WORKSHEET FOR THE NEW USER BY INPORTING FETCHER
        from fetcher import newsheet
        newuser=newsheet()
        newuser.newws(name,job,income)

        print((f'*********Arora Created new database for {name} :) ********').upper())



    def infoUpdate(self,username):
        print(div1)
        print((f'******** ARORA IS Updating {username} userifo********').upper())
        print(div1)
        print(("Tell me how much you spent this month on the following(enter 0 for no input): ").upper())
        electricitybill= int(input("electricitybill: "))
        internet2= int(input("internet bill: "))
        rent2= int(input("rent: "))
        entertainment2= int(input("entertainment like netflix: "))
        groceries2= int(input("groceries and food: "))
        petrol2= int(input("petrol/diesel: "))
        invest2= int(input("investment in stocks: "))
        edu2= int(input("investment on your education like books and courses: "))
        give2= int(input("donation: "))
        other2= int(input("enter the money you spend on other things like shopping etc: "))
        print(div1)
        expense=[electricitybill,internet2,rent2,entertainment2,groceries2,petrol2,invest2,edu2,give2,other2]
        print(aro)
        print(div1)
        infoUpdater().updates( expense,username)
        print(div1)
