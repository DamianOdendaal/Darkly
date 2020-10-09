<h1>Fix for XXS</h1>

Before doing anything with data that came from client side we always need to validate it and make sure it is exactly as we expected it to come in




<h1>Some more ways to prevent XSS</h1>

<ul>
<li>Filter input on arrival. At the point where user input is received, filter as strictly as possible based on what is expected or valid input.</li>
<li>Encode data on output. At the point where user-controllable data is output in HTTP responses, encode the output to prevent it from being interpreted as active content. Depending on the output context, this might require applying combinations of HTML, URL, JavaScript, and CSS encoding.</li>
<li>Use appropriate response headers. To prevent XSS in HTTP responses that aren't intended to contain any HTML or JavaScript, you can use the Content-Type and X-Content-Type-Options headers to ensure that browsers interpret the responses in the way you intend.</li>
<li>Content Security Policy. As a last line of defense, you can use Content Security Policy (CSP) to reduce the severity of any XSS vulnerabilities that still occur.</li>
</ul>
