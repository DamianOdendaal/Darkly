<h2>Some steps to avoiding this kind of Xss</h2>


<ol>
<li>Sanitizing:</li>
<p>
Sanitizing user input is especially helpful on sites that allow HTML markup, to ensure data received can do no harm to users as well as your database by scrubbing the data clean of potentially harmful markup, changing unacceptable user input to an acceptable format.
</p>

<li>Input Validation:</li>
<p>
Validating input is the process of ensuring an application is rendering the correct data and preventing malicious data from doing harm to the site, database, and users.
</p>
<li>Escaping:</li>
<p>
Escaping data means taking the data an application has received and ensuring it’s secure before rendering it for the end user. By escaping user input, key characters in the data received by a web page will be prevented from being interpreted in any malicious way.
</p>
</ol>