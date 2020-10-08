<h2>Sensitive data <b><u>should never</u></b> be in cookies. Rather have it inside a session on the server side</h2>

</br>
<ul>
<li>Something we could have done here was put an encoded token that would be unique for every user</li>
<li>Making use of something like JWT to generate a token for each user would make it harder to steal the</li>
<br/><br/>
<h3>According to guides.codepath.com</h3>

<li>The best prevention advice is simply not to put anything of value in cookies where it could be stolen. Only store non-sensitive data in cookies. For example, it is acceptable to store a user's language preference or a user's most recent choice for sorting a table of data.</li>

</ul>