import gspread
class Reader:
    def reads(self):
        gc=gspread.service_account(filename='creds.json')
        sh=gc.open('test')
        ws=sh.sheet1
        res=ws.get_all_records()
        return res
    
#
#
#

