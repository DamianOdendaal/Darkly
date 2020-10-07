
'''
 download all the files to the local system with the web scraper and use find command 
 to search through all thoose files and check if the content of thoose files contains numbers 
 and characters for the flag

'''

mkdir ./info
wget --mirror -A  README -P ./info -e robots=off http://192.168.1.100/.hidden/
find ./info -name README | xargs grep [0-9] | cut -d : -f2
rm -rf ./info