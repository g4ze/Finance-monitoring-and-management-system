from features import *
from fetcher import *
from userupdate import userupdate
feature=features()
#WE HAVE ALL OUR MENUS AT ONE PLACE FOR EASE OF ACCESS
class menus:
    def menu1(self,name):
        while True:
            print(div1)
            print('==========LIST OF SERVICES==========')
            print('1.EXPENDITURE FOR NEXT MONTH')
            print('2.CURRENT EXPENDITURE ANALYSIS')
            print('3.REPORT')
            print('4.LOAN CALCULATOR')
            print('5.Update USer')
            chc=input('Enter Choice(numeric): ')
            if chc=='ex': return 'ex'
            print(div1)
            if chc=='1':
                print(div1)
                feature.fornext(name)
            if chc=='2':
                print(div1)
                feature.analysis(name)
            if chc=='3':
                print(div1)
                feature.report(name)
            elif chc=='4':
                print(div1)
                LoanCalculator().calc()

                pass
            elif chc=='5':
                userup=userupdate()
                print('============GREAT! NOW I SHALL ASK YOU A FEW MORE DETAILS FOR THIS MONTH==========')
                userup.infoUpdate(name)

