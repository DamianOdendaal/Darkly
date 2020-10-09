<h1>Flag nine of Darkly</h1>

<h2>How to get flag</h2>

<ol>

<li>   go to any page on the site and replace the pages value inside the query string to '../'</li>
<li> In doing this you see the friendly alert that says 'wtf',  try to branch further down by doing '../../'</li>
<li> When we keep traversing further the alerts keep changing indicating we are getting close.</li>
        <b>--> When we see the 'You are getting close' stop there and add '/etc/passwd/' to the end of all the '../../'</b>


<h3> Side Note:  --> The sequence ../ is valid within a file path, and means to step up one level in the directory structure.
        The three consecutive ../ sequences step up from /var/www/images/ to the filesystem root, and so the file that is actually read is: /etc/passwd </h3>
<li> Get the flag </li>

</ol>

Well done on finding the directory Traversal flag
