<h1>Some examples of using curl using -F </h1> 
 
<h3>
   Example: send an image to an HTTP server, where 'profile' is the name of the form-field  to  which  the  file  por‐
              trait.jpg will be the input:

               curl -F profile=@portrait.jpg https://example.com/upload.cgi

              Example: send a your name and shoe size in two text fields to the server:

               curl -F name=John -F shoesize=11 https://example.com/

              Example:  send  a your essay in a text field to the server. Send it as a plain text field, but get the contents for
              it from a local file:

               curl -F "story=<hugefile.txt" https://example.com/

              You can also tell curl what Content-Type to use by using 'type=', in a manner similar to:

               curl -F "web=@index.html;type=text/html" example.com
</h3>