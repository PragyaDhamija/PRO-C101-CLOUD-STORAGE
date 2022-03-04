import os
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(fileFrom):
            for name in files:
                local_path = os.path.join(root, name)
                print(local_path)

                relative_path = os.path.relpath(local_path, fileFrom)
                dropbox_path = os.path.join(fileTo, relative_path)

                with open(path, "rb") as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BCGCBoqmIHXOoXxfXqXNv_CBMtR3p_d6Whnazb-vsALkXGJYZtHRif2qnUNoS40lkgi5a2goX8NO9BHAuFn1BYau9F5l5eNCzOIbv9Nxxv5Lpwp1EJQHv30vN70jaCPjx05Z6q02qLs'
    transfer_data = TransferData(access_token)

    fileFrom = input("Enter The Path Of File To Be Taken:- ")
    fileTo = input("Enter The Path Where The File Is To Be Dropped:- ")

    transfer_data.upload_file(fileFrom, fileTo)

    print("Your file has been uploaded successfully... :)")
    
main()