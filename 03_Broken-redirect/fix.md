<h1>The redirect is being controlled by a function that takes in data and sends you there, which is an Open redirect</h1>

<h2>In many cases, this behavior can be avoided in two ways:</h2>

<ol>
<li>Remove the redirection function from the application, and replace links to it with direct links to the relevant target URLs.</li>
<li>Do error handling on server side,  like have a list of allowed urls and only refer to that list when doing redirects</li>
</ol>





