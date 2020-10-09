<h1>Flag eleven of Darkly</h1>

<h2>Advanced Xss</h2>

<ol>

<li> go to http://192.168.1.100/index.php?page=media?src=nsa </li>
    once you are here you can change the value of source then see the sorry wrong answer indicating we on the right track
<li> Tried to change nsa to <script>alert("Working")</script>,  like this http://192.168.1.100/index.php?page=media?src=<script>alert("Working")</script>,  </li>
<li> Baring in mind we are working with an image, inside query strings sometimes we see the payload is a [base 64](./what-is-base64.md) encoded string</li>
<li>  Base64 encode the script and try again </li>



<h3>Note for Step 4</h3>
<p>Something to keep in mind ,  because we are putting a base 64 string into the href attribute we are going to need to 
add something too so that it will work </p>
<p>
according to https://base64.guru/developers/html/link
</p>
<p>
it would look like this with the encoded string --> data:text/html;base64,PHNjcmlwdD5hbGVydCgnVGhpcyB3b3JrcycpPC9zY3JpcHQ+

</p>
<p>
now replace nsa with the abovementioned string to get the flag like this -> http://192.168.1.100/index.php?page=media?src=data:text/html;base64,PHNjcmlwdD5hbGVydCgnVGhpcyB3b3JrcycpPC9zY3JpcHQ+
</p>
</ol>

Well done we found another flag
