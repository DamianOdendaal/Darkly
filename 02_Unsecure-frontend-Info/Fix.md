<h1>Rather set sensative information on the backend rather than the frontend. A hidden field can still be viewed or editted by the client.</h1>

<p>Even if the field was hidden we still need to replace the inputs value back to an empty string, Leaving any sensitive data on the client side is 
    risk because anyone can simply inspect the page and see it.  Rather keep data on the backend after you sanitise it on the frontend and the backend </p>