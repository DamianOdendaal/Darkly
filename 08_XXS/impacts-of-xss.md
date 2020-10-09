<h1>What are the types of XSS attacks?</h1>

<ul>
<li>Reflected XSS,(where the malicious script comes from the current HTTP request.)</li>
<li>Stored XSS, (where the malicious script comes from the website's database.)</li>
<li>DOM-based XSS, (where the vulnerability exists in client-side code rather than server-side code.)</li>
</ul>

<h3></h3>

<ol>
<li><h1>Reflected XSS</h1></li>
<h3>Reflected XSS is the simplest variety of cross-site scripting. It happens when an application receives data in an HTTP request and includes that data within the immediate response in an unsafe way.</h3>
<h3>A simple example of reflected Xss</h3>
<h4>

https://insecure-website.com/status?message=All+is+well.

<p>Status: All is well.</p>

The application doesn't perform any other processing of the data, so an attacker can easily construct an attack like this:

https://insecure-website.com/status?message=<script>/*+Bad+stuff+here...+*/</script>

<p>Status: <script>/* Bad stuff here... */</script></p>

If the user visits the URL constructed by the attacker, then the attacker's script executes in the user's browser, in the context of that user's session with the application. At that point, the script can carry out any action, and retrieve any data, to which the user has access.

</h4>

<li><h1>Stored XSS</h1></li>

<h4>
Stored XSS (also known as persistent Xss) arises when an application receives data from an untrusted source and includes that data within its later HTTP responses in an unsafe way.
The data in question might be submitted to the application via HTTP requests; for example, comments on a blog post, user nicknames in a chat room, or contact details on a customer order. 


Here is a simple example of a stored XSS vulnerability. A message application lets users submit messages, which are displayed to other users:

<p>Hello, this is my message!</p>
The application doesn't perform any other processing of the data, so an attacker can easily send a message that attacks other users:

<p><script>/* Bad stuff here... */</script></p>



</h4>

<li><h1>DOM-based XSS</h1></li>

<h4>
DOM-based XSS (also known as DOM XSS) arises when an application contains some client-side JavaScript that processes data from an untrusted source in an unsafe way, usually by writing the data back to the DOM.

In the following example, an application uses some JavaScript to read the value from an input field and write that value to an element within the HTML:

var search = document.getElementById('search').value;
var results = document.getElementById('results');
results.innerHTML = 'You searched for: ' + search;

If the attacker can control the value of the input field, they can easily construct a malicious value that causes their own script to execute:

You searched for:  <img src=1 onerror='/* Bad stuff here... */'>


<h3>Note</h3>
In a typical case, the input field would be populated from part of the HTTP request, such as a URL query string parameter, allowing the attacker to deliver an attack using a malicious URL, in the same manner as reflected XSS.
</h4>
</ol>


<h1>What can XSS be used for</h1>
<ul>
<li>Impersonate or masquerade as the victim user.</li>
<li>Carry out any action that the user is able to perform.</li>
<li>Read any data that the user is able to access.</li>
<li>Capture the user's login credentials.</li>
<li>Perform virtual defacement of the web site.</li>
<li>Inject trojan functionality into the web site.</li>
</ul>


<h1>Impact of Xss</h1>

<ul>
<h2>The actual impact of an XSS attack generally depends on the nature of the application, its functionality and data, and the status of the compromised user. Some Examples</h2>
<li>In a brochureware application, where all users are anonymous and all information is public, the impact will often be minimal.</li>
<li>In an application holding sensitive data, such as banking transactions, emails, or healthcare records, the impact will usually be serious.</li>
<li>If the compromised user has elevated privileges within the application, then the impact will generally be critical, allowing the attacker to take full control of the vulnerable application and compromise all users and their data.</li>
</ul>