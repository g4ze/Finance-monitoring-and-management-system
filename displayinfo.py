from fetcher import Reader
from variables import *

class displayinfo:
    def displayExpenses(self,name,month=0):
        read=Reader()
        expenses=read.readcol(month,name)
        expenseList1=expenseList
        if not month==0:
            print('FOR MONTH----->',month)
            for i in range(4,len(expenseList1)+4):
                print(f'{expenseList1[i-4]}: {expenses[i]}')
        else:
            print(read.readall(name))
    def seegoals(self):
        a=1