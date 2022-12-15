import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="amsal", passwd="1234", database="finance")
mycursor= mydb.cursor()

sqltable= "CREATE TABLE IF NOT EXISTS income(name VARCHAR(200), salary INT, freelance INT, dividend INT, business INT, other INT)"
mycursor.execute(sqltable)
mydb.commit()


sqltable2= "CREATE TABLE IF NOT EXISTS expense(name VARCHAR(200), elecbill INT, internet INT, rent INT, entertainment INT, groceries INT, petrol INT, invest INT, edu INT, charity INT, other INT, saving INT)"
mycursor.execute(sqltable2)
mydb.commit()

def update():
    name=input("Please enter your name;  ")
    sqlformula="SELECT * FROM income"
    mycursor.execute(sqlformula)
    result=mycursor.fetchall()
    for i in result:
        if i[0]==name:
            print()
            print("Welcome, Please choose which data you want to change")
            print("enter 1 for salary")
            print("enter 2 for freelance")
            print("enter 3 for dividend")
            print("enter 4 for business")
            print("enter 5 for other")
            print()
            num=int(input("enter your choice here"))
            print()
            value=int(input("enter the new value"))
            vt=(value, name)
            
            if num==1:
                      
                sqlformula2="UPDATE income SET salary = %s WHERE name = %s"
                mycursor.execute(sqlformula2,vt)
                mydb.commit()
                print("data entered successsfully")
                print()

            elif num==2:
                      
                sqlformula2="UPDATE income SET freelance = %s WHERE name = %s"
                mycursor.execute(sqlformula2,vt)
                mydb.commit()
                print("data entered successsfully")
                print()

            elif num==3:
                      
                sqlformula2="UPDATE income SET dividend = %s WHERE name = %s"
                mycursor.execute(sqlformula2,vt)
                mydb.commit()
                print("data entered successsfully")
                print()

            elif num==4:
                      
                sqlformula2="UPDATE income SET business = %s WHERE name = %s"
                mycursor.execute(sqlformula2,vt)
                mydb.commit()

                print("data entered successsfully")
                print()

            elif num==5:
                      
                sqlformula2="UPDATE income SET other = %s WHERE name = %s"
                mycursor.execute(sqlformula2,vt)
                mydb.commit()

                print("data entered successsfully")
                print()

            else:
                print("enter a valid number")

def dataentry():
    name=input("pls enter your name")
    namet=(name,)
    sqlformula="SELECT * FROM expense"
    mycursor.execute(sqlformula)
    result=mycursor.fetchall()
    for i in result:
        if i[0]==name:
            print()
            print("Welcome, pls tell us how much you spent this month on the following: ")
            electricitybill= int(input("electricitybill"))
            internet2= int(input("internet bill"))
            rent2= int(input("rent"))
            entertainment2= int(input("entertainment like netflix"))
            groceries2= int(input("groceries and food"))
            petrol2= int(input("petrol/diesel"))
            invest2= int(input("investment in stocks"))
            edu2= int(input("investment on your education like books and courses"))
            give2= int(input("donation"))
            other2= int(input("enter the money you spend on other things like shopping etc"))

            totalexpense=electricitybill+internet2+rent2+entertainment2+groceries2+petrol2+invest2+edu2+give2+other2
            exp=(electricitybill, internet2, rent2, entertainment2, groceries2, petrol2, invest2, edu2, give2, other2,str(name))

            sqlformula2="SELECT * FROM income"
            mycursor.execute(sqlformula2)
            result2=mycursor.fetchall()
            totalincome=0
            for j in result2:
                if j[0]==name:
                    totalincome=j[1]+j[2]+ j[3] + j[4]+ j[5]
            savings=totalincome+totalexpense
                    
            print()
            print("your last month's financial status was:")
            print()
            print("spending on necessaties:",i[1]+i[2]+i[3]+i[5]+i[6])
            print("spending on fun:",i[4]+i[10])
            print("spending on investment:  ",i[7])
            print("spending on charity:  ",i[9])
            print("spending on education:  ",i[8])
            '''print("savings:  ",i[11])'''
            print()
            
            sqlformula3="UPDATE expense SET elecbill= %s, internet= %s,rent= %s, entertainment= %s,groceries= %s, petrol= %s, invest= %s, edu= %s, charity= %s,other= %s WHERE name=%s"
            mycursor.execute(sqlformula3,exp)
            mydb.commit()

            sqlformula4= "SELECT * FROM expense"
            mycursor.execute(sqlformula4)
            result5=mycursor.fetchall()
            for r in result5:
                if r[0]==name:
                    
                    print()
                    print("your current financial status is:")
                    print()
                    print("spending on necessaties:",r[1]+r[2]+r[3]+r[5]+r[6])
                    print("spending on fun:",r[4]+r[10])
                    print("spending on investment:  ",r[7])
                    print("spending on charity:  ",r[9])
                    print("spending on education:  ",r[8])
                    '''print("savings:  ",r[11])"'''
                    print()
                    
                    

def seegoal():
    totalincome=0
    
    name=input("pls enter your name")
    sqlformula="SELECT * FROM income"
    mycursor.execute(sqlformula)
    result=mycursor.fetchall()
    for i in result:
        if i[0]==name:
            
            

            totalincome=i[1]+ i[2] + i[3] + i[4] + i[5]
            
            idealnec= totalincome*0.55
            idealsaving= totalincome*0.10
            idealinvest=totalincome*0.10
            idealeducation= totalincome*0.10
            idealfun= totalincome*0.10
            idealgive= totalincome*0.05

            print()
            print("Here are your goals of the month")
            print()
            print("spending on necessaties:    ",round(idealnec,2))
            print("spending on fun:            ",round(idealfun,2))
            print("spending on investment:     ",round(idealinvest,2))
            print("spending on charity:        ",round(idealgive,2))
            print("spending on education:      ",round(idealeducation,2))
            print("saving:                     ",round(idealsaving,2))
            print()
        else:
            continue
        print("user not found")
            
    



def showall():
    mycursor.execute("SELECT * FROM income")
    myresult= mycursor.fetchall()
    for i in myresult:
            print(i)
    mycursor.execute("SELECT * FROM expense")
    myresult= mycursor.fetchall()
    for i in myresult:
            print(i)

def newentry():
    name = input("enter your name: ")
    print("Let's talk about your income first")
    print("We are going to ask you how much you earn from different sources, Enter your monthly income and type 0 if you don't use that source to earn ")
    print()
    sal=int(input("enter your monthly salary"))
    freelance= int(input("how much you earn by freelancing"))
    dividend= int(input("how much you earn from dividend"))
    business= int(input("how much you earn from your business"))
    other = int(input("how much you earn by other sources"))

    mysql= "INSERT INTO income (name, salary, freelance, dividend, business, other) VALUES (%s, %s, %s, %s, %s, %s)"
    data=(name, sal, freelance, dividend, business, other)
    mycursor.execute(mysql, data)
    mydb.commit()
    print()
    print("GREAT!! Let's talk about your expenses now")
    print()
    print("We are going to ask you how much you spend on different sectors, Enter your monthly expenses on the following thing. Don't worry, no need to be exact ")
    print()
    electricitybill= int(input("enter your monthly electricitybill"))
    internet= int(input("enter your monthly internet bill"))
    rent= int(input("enter your monthly rent"))
    entertainment= int(input("enter your monthly expenditure on entertainment like netflix"))
    groceries= int(input("enter your monthly expenditure on groceries and food"))
    petrol= int(input("enter your monthly expenditure on petrol/diesel"))
    invest= int(input("How much you invest monthly in stocks or other investment sources"))
    edu= int(input("enter your monthly investment on your education like books and courses"))
    give= int(input("enter the monthly amount you donate in charity or to the needy ones"))
    other= int(input("enter the money you spend on other things like shopping etc"))

    totalincome=sal+freelance+dividend+business+other
    totalexpenses=electricitybill+internet+rent+entertainment+groceries+petrol+other
    saving=totalincome-totalexpenses

    sqlformula= "INSERT INTO expense (name, elecbill, internet, rent, entertainment, groceries, petrol, invest, edu, charity, other) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    data2=(name, electricitybill, internet, rent, entertainment, groceries, petrol, invest, edu, give, other)
    mycursor.execute(sqlformula, data2)
    mydb.commit()

    totalincome=sal+freelance+dividend+business+other
    totalexpenses=electricitybill+internet+rent+entertainment+groceries+petrol+other

    idealnec= totalincome*0.55
    idealsaving= totalincome*0.10
    idealinvest=totalincome*0.10
    idealeducation= totalincome*0.10
    idealfun= totalincome*0.10
    idealgive= totalincome*0.05

    print()
    print("Thank You, your current financial report is:")
    print()
    print("spending on necessaties:    ",electricitybill+internet+rent+groceries+petrol)
    print("spending on fun:            ", entertainment+other)
    print("spending on investment:     ",invest)
    print("spending on charity:        ",give)
    print("spending on education:      ",edu)
    print("saving:                     ",totalincome-totalexpenses)
    print()

    print("We have also prepared a goal chart for you to manage your finance accordingly next month")
    print()
    print("spending on necessaties:    ",round(idealnec,2))
    print("spending on fun:            ",round(idealfun,2))
    print("spending on investment:     ",round(idealinvest,2))
    print("spending on charity:        ",round(idealgive,2))
    print("spending on education:      ",round(idealeducation,2))
    print("saving:                     ",round(idealsaving,2))
    print()
    print("come back next month to check if you accomplished your goals, ALL THE BEST!")
    
print('\n,\n,\n')
print("--------FINANCE FREEDOM--------")
print()
print("Manage your finance with ease")
print()
print("Are you an existing user?")
print()
u=input("type 'y' for yes or 'n' for no;     ")
print()
while True:
    if u.lower() =="y":
        print("WELCOME BACK!")
        print()
        print("Choose the desired option from the following")
        print()
        print("Enter 1 to enter to enter your expenses for this month and see if you achieved your goal")
        print("Enter 2 to see your goal for this month")
        print("Enter 3 to update your income information")
        print("Enter 4 to exit")
        print()
        n=int(input("Enter your choice here;    "))

        if n==1:
                dataentry()
                print()
                input("press any key to return")

        if n==2:
            seegoal()
            print()
            input("press any key to return")

        if n==3:
            update()
            print()
            input("press any key to return")

        if n==4:
            break


    if u.lower()=="n":
        newentry()
        print()
        input("press any key to exit")
        break

        







	
