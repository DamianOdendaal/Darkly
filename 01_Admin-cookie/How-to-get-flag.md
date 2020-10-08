<h1>Flag number one</h1>

<h2>Cookie Theft</h2>

<h3>Steps to finding the flag</h3>

<ol>

<li> On the landing page inspect the element </li>
<li> Go to application and then cookies,  in there we will find the i_am_admin cookie with the value --> 68934a3e9455fa72420237eb05902327 </li>
<li> decrypt value using MD5 to get this --> false </li>
<li> Change the false to true,  so encrypt True with MD5 hash then replace the first value with our new hashed value </li>
<li> refresh the page </li>

</ol>

<b><u>Well done we have our first flag</u></b>
