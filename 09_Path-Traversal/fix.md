<h1>Some ways to avoid a path traversal attack(Both applicable to our current flag)</h1>

<ol>

<li> 
Make sure the server process can only access the directories it needs.
Consider running the process in a chroot jail if you are running on Unix. 
This will mitigate the risks if a directory traversal vulnerability is discovered.
</li>

<li>
Sanitise filename parameters
The safest approach is to restrict filenames to a list of known good characters,
and ensure that any references to files use only those characters.
</li>

</ol>
