import gspread
from variables import *
class Reader:
    gc=gspread.service_account(filename='creds.json')
    sh=gc.open('test')
    def readall(self,sheetname):
        
        ws=self.sh.worksheet(sheetname)
        res=ws.get_all_records()
        return res

    def readrow(self,name,r):
        ws=self.sh.worksheet(name)
        values_list = ws.row_values(r)
    def readcol(self,col,name):
        
        
        ws=self.sh.worksheet(name)
        print(aro)
        if col==0:
            col=int(ws.acell('B4').value)
            return ws.col_values(col)
        else:
            return ws.col_values(col)
    def check(self,name):
        
        ws=self.sh.worksheet('sheet1')
        l = (ws.acell('A1').value).split(',')
        for i in l:
            if name in i:
                return True
        return False    
    def months(self,name):
        
        ws=self.sh.worksheet(name)
        print(aro)
        col=int(ws.acell('B4').value)
        return col

class newsheet(Reader):
    gc=gspread.service_account(filename='creds.json')
    sh=gc.open('test')
    def newws(self,name,job,income):
        
        worksheet = self.sh.add_worksheet(title=name, rows=100, cols=20)
        ws=self.sh.sheet1
        st=ws.acell('A1').value
        ws.update('A1',st+','+name)
        worksheet.update('A1',f'name: {name}')
        worksheet.update('A2',f'job: {job}')
        worksheet.update('A3',f'income: {income}')
        worksheet.update('A4',f'month:')
        worksheet.update('B4',0)
        #######################################################################################3
        worksheet.update('A5',f'electricitybill:')
        worksheet.update('A6',f'internet:')
        worksheet.update('A7',f'rent:')
        worksheet.update('A8',f'entertainment:')
        worksheet.update('A9',f'groceries:')
        worksheet.update('A10',f'petrol:')
        worksheet.update('A11',f'invest:')
        worksheet.update('A12',f'edu:')
        worksheet.update('A13',f'give:')
        worksheet.update('A14',f'other:')
        ######################################################################################3

class infoUpdater:
    gc=gspread.service_account(filename='creds.json')
    sh=gc.open('test')
    def updates(self,expenses,name):
        
        ws=self.sh.worksheet(name)
        month=int(ws.acell('B4').value)+1
        ws.update('B4',month)
        col=chr(65+month)
        row=5
        j=0
        for i in range (row,15):
            ws.update(f'{col}{i}',f'{expenses[j]}')
            j+=1
        print(('--------------All information is now updated--------------').upper())
        print(div1)