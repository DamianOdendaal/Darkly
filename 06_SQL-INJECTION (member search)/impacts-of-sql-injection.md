<h1>Impacts of SQL-injection</h1>

<p>Many high-profile data breaches in recent years have been the result of SQL injection attacks, leading to reputational damage and regulatory fines. In some cases, an attacker can obtain a persistent backdoor into an organization's systems, leading to a long-term compromise that can go unnoticed for an extended period.</p>
<h2>SQL injection examples</h2>
<h4>Although there is a very wide variety of SQL injection vulnerabilities,attacks, and techniques, which arise in different situations. We can look at four of the more common examples</h4>
<ol>
<li>Retrieving hidden data, (where you can modify an SQL query to return additional results.)</li>
<li>Subverting application logic, (where you can change a query to interfere with the application's logic.)</li>
<li>UNION attacks, (where you can retrieve data from different database tables.)</li>
<li>Examining the database, (where you can extract information about the version and structure of the database.)</li>
</ol>
<h2>So lets get more into the smaller details of the four examples</h2>

<ol>

<li><h1>Retrieving hidden data</h1></li>
<h3>Lets use a a shopping application that displays products in different categories as an example. With the following url</h3>
<p>https://insecure-website.com/products?category=Gifts</p>
<p>This will cause the application to make an SQL query to get details of the relevant products in a specific category from the database:</p>
<u>SELECT * FROM products WHERE category = 'Gifts' AND released = 1</u>
<h3>What the SQL query asks the database to return:</h3>
<ol>
<li>all details (*)</li>
<li>from the products table</li>
<li>where the category is Gifts</li>
<li>and released is 1.</li>
<li>A restriction is being used to hide products that are not released 'released = 1' . For unreleased products, presumably released should be 0.</li>
</ol>
<h2>In this case the application doesn't implement any defenses against SQL injection attacks, so an attacker can construct an attack like:</h2>
<h3>https://insecure-website.com/products?category=Gifts'--</h3>
<p>This results in the SQL query: ---->    <u>SELECT * FROM products WHERE category = 'Gifts'--' AND released = 1</u></p>
<h1>Important!</h1>
<p>
    The key thing here is that the double-dash sequence -- is a comment indicator in SQL, this means anything that comes after it will be ignored. So in a  case where people were trying to hide unreleased products, this would be effective because we have now made their query ignore the AND released = 1 so   now we are able to see things they never wanted us to see
</p>
<h2>An attacker can also cause the application to display all the products in any category, including categories that they don't know about:</h2>
<h3>https://insecure-website.com/products?category=Gifts'+OR+1=1--</h3>
<p>This results in the SQL query: ---->   <u>SELECT * FROM products WHERE category = 'Gifts' OR 1=1--' AND released = 1</u></p>
<h4>
The modified query will return all items where either the category is Gifts, or 1 is equal to 1. Since 1=1 is always true, the query will return all items.
</h4><br/>


<li><h1>Subverting application logic</h1></li>


<h3>Lets use a login page on an application as an example,  one that takes a username and a password.  If we had to enter a username "Damian" and a password "CornIsYellow", the application checks the credentials by performing the following SQL query: </h3>

<h2>
    '''
        SELECT * FROM users WHERE username = 'Damian' AND password = 'CornIsYellow' 
    ''' 
</h2>

<h3>An attacker can log in as any user without even needing their password by adding a SQL comment so that it removes the password from the WHERE clause in the query </h3>

<h4>Baring this in mind we can then simply log in as the admin user and not need the password by adding ( administrator'-- ) into the username field and leave the password blank. Doing that results in the following query</h4>

<h2>
    '''
       SELECT * FROM users WHERE username = 'administrator'--' AND password = ''

    ''' 
</h2>
   <p> This query returns the user whose username is administrator and successfully logs the attacker in as that user.</p>

<li><h1>Union Attack</h1></li>

<h3>
In cases where the results of an SQL query are returned within the application's responses, an attacker can leverage an SQL injection vulnerability to retrieve data from other tables within the database. This is done using the UNION keyword, which lets you execute an additional SELECT query and append the results to the original query.
</h3>

<h3>For example, if an application executes the following query containing the user input "Gifts":</h3>

<h4>SELECT name, description FROM products WHERE category = 'Gifts'</h4>

<h3>then an attacker can submit the input:</h3>

<h2>
    '''
     ' UNION SELECT username, password FROM users--

    ''' 
</h2>



<h4>This will cause the application to return all usernames and passwords along with the names and descriptions of products.</h4>



<h1>Examining Database</h1>

Some cases the attacker might not know the names of the tables or metadata related to the application but they can make use of [information_schema](./information_schema.md)


</ol>