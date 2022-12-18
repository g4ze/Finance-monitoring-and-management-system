from fetcher import *
class features:
        
    def fornext(self,name):
        print(div1)
        print('======Telling ideal expenditure for next month=====')
        reader=Reader()
        col1=reader.readcol(1,name)
        totalincome=int(col1[2].split(' ')[1])
        idealnec= totalincome*0.55
        idealsaving= totalincome*0.10
        idealinvest=totalincome*0.10
        idealeducation= totalincome*0.10
        idealfun= totalincome*0.10
        idealgive= totalincome*0.05
        print(div1)
        print("Here are your goals of the month")
        print()
        print("spending on necessaties:    ",round(idealnec,2))
        print("spending on fun:            ",round(idealfun,2))
        print("spending on investment:     ",round(idealinvest,2))
        print("spending on charity:        ",round(idealgive,2))
        print("spending on education:      ",round(idealeducation,2))
        print("saving:                     ",round(idealsaving,2))
        print(div1)
    
    def analysis(self, name):
        print(div1)
        print('Running the analyser')
        mo=int(input('enter the number of last months to analyse(enter 0 for latest month): '))
        col1=Reader().readcol(1,name)
        totalincome=int(col1[2].split(' ')[1])
        if not(mo=='0'):
            totalincome*=(int(mo))
        def colvals(m):
            reader=Reader()
            col=reader.readcol(m,name)
            
            necc=int(col[4])+int(col[5])+int(col[6])+int(col[8])+int(col[9])
            fun=int(col[7])+int(col[13])
            invest=int(col[10])
            charity=int(col[12])
            edu=int(col[11])
            exp=necc+fun+invest+charity+edu
            return {'necc':necc,'fun':fun,'invest':invest,'charity':charity,'edu':edu,'exp':exp}
        
        def analyser(mon):
            month=Reader().months(name)+1
            
            totalvalues={'necc':0,'fun':0,'invest':0,'charity':0,'edu':0,'exp':0}
            values={}
            if mon ==0:
                mon=1
            for i in range(month-(mon),month):
                values=colvals(i+1)
                for key in values:
                    totalvalues[key]=totalvalues[key]+values[key]
                values=totalvalues
            print(div1)
            print('Total income: ',totalincome)
            print("spending on necessaties:    ",values['necc'])
            print("spending on fun:            ",values['fun'])
            print("spending on investment:     ",values['invest'])
            print("spending on charity:        ",values['charity'])
            print("spending on education:      ",values['edu'])
            save=totalincome-values['exp']
            if save<0:
                print("Debt:                     ",save)
                print('You are in debt. Would you like to explore loan options?')
                chc=input('Y/N?')
                if chc=='N':
                    print(div1)
                    print('-----------Continuing analysis-------')
                    print(div1)
                else:
                    LoanCalculator().calc()
                    pass
            else:
                print("Savings:                     ",save)
                print(div1)
            print(div1)
            print('====Displaying graph====')
            chc=input('Y/N: ')
            if chc=='Y':
                graph().display(name)
            print(div1)
        analyser(int(mo))
    
class graph:
    def colvals(self,m,name):
            reader=Reader()
            col=reader.readcol(m,name)
            
            necc=int(col[4])+int(col[5])+int(col[6])+int(col[8])+int(col[9])
            fun=int(col[7])+int(col[13])
            invest=int(col[10])
            charity=int(col[12])
            edu=int(col[11])
            exp=necc+fun+invest+charity+edu
            return [necc,fun,invest,charity,edu,exp]
        
    def display(self,name):
        print(div1)

        import matplotlib.pyplot as plt
        month=Reader().months(name)
        xax=[]
        values=[]
        labels=['necc','fun','invest','charity','edu','expenditure']
        for i in range(1,month+1):
            xax.append(i)
        j=0
        res=[]
        for i in range(2,month+2):
            values=graph().colvals(i,name)
            res.append(values)
        for i in range(0,5):
            line1=[]
            for j in range(0,month):
               
                line1.append(res[j][i])
            plt.plot(xax, line1, label = labels[i],linewidth = 1)
        
        line1=[]
        for j in range(0,month):
            line1.append(res[j][5])
        plt.plot(xax, line1, label = labels[5],color='black', linestyle='dashed', linewidth = 1,marker='o', markerfacecolor='blue', markersize=4)
            
    
        
        # naming the x axis
        plt.xlabel('months')
        # naming the y axis
        plt.ylabel('money')
        # giving a title to my graph
        plt.title('EXPENSE ANALYSIS PER MONTH')
        
        # show a legend on the plot
        plt.legend()
        
        # function to show the plot
        plt.show()
        print(div1)


class LoanCalculator:
    def calc(self):
        print(div1)
        amt=int(input('Enter Total amount needed '))
        r=input('Enter Rate: ')
        t=input('Enter time in years: ')
        r=int(r)/1200
        t=int(t)
        print('Monthly EMI: ',round((amt*r*((1+r)**(t*12)))/(((1+r)**(t*12))-1),2))
        print(div1)
    # print('Please tell the constant factor(s)')
    # chc=[]
    # while 1:
    #     print('Rate(r) EMI(e) Time(t)-in-years')
    #     chc=(input('enter choice seperated by space(not more than 2)').split())
    #     if len (chc)<=2:break
    # if 'r' in chc:
    #     if 'e' in chc:
    #         r=float(input(('Enter rate: ')))
    #         e=int(input('Enter EMI: '))
    #         t=math.log((e/r)/(e/r-amt))/math.log(1+r)

    #         print(f'Time required for {amt} would be',t)



