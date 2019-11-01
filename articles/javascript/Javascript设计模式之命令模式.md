~~~
var commands = {
	refresh: function(){
		console.log('refresh');
	},
	cut: function(){
		console.log('cut');
	},
	copy: function(){
		console.log('copy');
	},
	paste: function(){
		console.log('paste');
	}
}

var bindClick = function(button, fun){
	button.onclick = fun;
}


var button1 = document.createElement('button');
button1.innerHTML = 'CUT'
document.body.appendChild(button1);

bindClick(button1,commands.cut);
~~~