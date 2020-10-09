<h1> Flag eight of Darkly </h1>

<ol>

<li> Navigate to http://192.168.1.100/index.php?page=feedback </li>

<li> Inside any of the fields add html markup to see if instructions are executed,  example <b>Oh</b> </li>

--> in doing this you see that the instruction is executed and we can now go deeper

<li> <body onload="alert("it works")"> will insert the alert but not produce flag </li>

<li>Trying to do reflected Xss didnt work,  entering script into url </li>

<li>Trying to do persistent Xss didnt work,  entering script into input </li>

<li>In messing around,  inside the name or the comment field you can put any characters from the words
alert or script,  but they must be in order,  the whole word need not be there for the flag to appear </li>


</ol>

Well done thats the 8th flag