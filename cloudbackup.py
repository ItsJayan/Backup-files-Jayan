from os import access
import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    def upload_files(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)
def main():
    access_token = 'sl.BKBNbjoJamUgQSNTBdR3lg2remVt8so4HWlXoDjJ23I5PW0OKRED2EazXP89lehPK_DX02MXuuiIGyKoinqFx6dn8Mpc2ndMA8Sa6GS-kps594_8EEsXhTR9TTxWYTYb0yzZwi4'
    Transferdata = TransferData(access_token)
    file_from = input("enter the source")
    file_to = input("enter the destination") 
    Transferdata.upload_files(file_from,file_to)
    print("the upload was succesful")
main()