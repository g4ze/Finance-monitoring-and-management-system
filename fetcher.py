import gspread
#importing gspread api
class Reader:
    def reads(self):
        gc=gspread.service_account(filename='creds.json')
        #specifying credidentials file
        sh=gc.open('test')  #telling the spreadsheet name
        ws=sh.sheet1    #telling spreadsheet' workseet
        res=ws.get_all_records()    #calling all records
        return res  #returning the whole ws's info in form of a list of dictionaries
    
#
#
#

