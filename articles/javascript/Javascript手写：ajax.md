## 手写实现原生Ajax
```
var xhr = null;

// Old compatibility code, no longer needed.
if (window.XMLHttpRequest) { // Mozilla, Safari, IE7+ ...
  xhr = new XMLHttpRequest();
} else if (window.ActiveXObject) { // IE 6 and older
  xhr = new ActiveXObject("Microsoft.XMLHTTP");
}

xhr.onreadystatechange = function(){
  // Process the server response here.
  if (xhr.readyState === XMLHttpRequest.DONE) {
    // Everything is good, the response was received.
    if (xhr.status === 200) {
		  // Perfect!
		} else {
	    // There was a problem with the request.
	    // For example, the response may have a 404 (Not Found)
	    // or 500 (Internal Server Error) response code.
		}
	} else {
	  // Not ready yet.
	}
};


xhr.open('GET', 'http://www.example.org/some.file', true);

// Set the MIME type of the request
xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

xhr.send();
 ```

## open(param1,parma2,param3)

- param1, the HTTP request method – GET, POST, HEAD, or another method supported by your server.
- param2, the URL you're sending the request to.
- param3, sets whether the request is asynchronous. If true (the default)

## XMLHTTPRequest.readyState

- 0 (uninitialized) or (request not initialized)
- 1 (loading) or (server connection established)
- 2 (loaded) or (request received)
- 3 (interactive) or (processing request)
- 4 (complete) or (request finished and response is ready)

```
Value	    State	                 Description
0	        UNSENT	               Client has been created. open() not called yet.
1	        OPENED	               open() has been called.
2	        HEADERS_RECEIVED	     send() has been called, and headers and status are available.
3	        LOADING	               Downloading; responseText holds partial data.
4	        DONE	                 The operation is complete.
```

# 更多  

AJAX（Asynchronous JavaScript And XML）
https://developer.mozilla.org/en-US/docs/Glossary/AJAX

AJAX Getting Started 
https://developer.mozilla.org/en-US/docs/Web/Guide/AJAX/Getting_Started  

XMLHttpRequest 
https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest    

Using XMLHttpRequest  
https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/Using_XMLHttpRequest  

XMLHttpRequest readyState
https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/readyState  