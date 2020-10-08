<h1>More about Cross site request forgery</h1>

<p>Cross-site request forgery (also known as CSRF) is a web security vulnerability that allows an attacker to make users to perform actions that they do not intend to perform. It allows an attacker to partly find a way around the same origin policy, which is designed to prevent different websites from interfering with each other.</p>

<h1>How does it work?</h1>
<h2>For a CSRF attack to be possible, three key conditions must be in place:<h2>
<ol>
<li>A relevant action. There is an action within the application that the attacker has a reason to induce. This might be a privileged action (such as modifying permissions for other users) or any action on user-specific data (such as changing the user's own password).</li>
<li>No unpredictable request parameters. The requests that perform the action do not contain any parameters whose values the attacker cannot determine or guess. For example, when causing a user to change their password, the function is not vulnerable if an attacker needs to know the value of the existing password.</li>
<li>Cookie-based session handling. Performing the action involves issuing one or more HTTP requests, and the application relies solely on session cookies to identify the user who has made the requests. There is no other mechanism in place for tracking sessions or validating user requests.</li>
</ol>