状态模式：允许一个对象在其内部状态改变时改变它的行为，对象看起来似乎修改了它的类。

状态模式的关键是区分事物内部的状态，事物内部状态的改变往往会带来事物的行为改变。

~~~
var delegate = function(client,delegation){
	return {
		pressed: function(){
			return delegation.pressed.apply(client,arguments);
		}
	}
}

var FSM = {
	off: {
		pressed: function(){
			console.log('closed');
			this.button.innerHTML = 'OPEN';
			this.currState = this.onState;
		}
	},
	on: {
		pressed: function(){
			console.log('opened');
			this.button.innerHTML = 'CLOSE';
			this.currState = this.offState;
		}
	}
}

function Light(){
	this.offState = delegate(this,FSM.off);
	this.onState = delegate(this,FSM.on);
	this.currState = this.offState;
	this.button = null;
}

Light.prototype.init = function(){
	var self = this,button = document.createElement('button');
	button.innerHTML = 'OPEN'
	this.button = document.body.appendChild(button);
	this.button.onclick = function(){
		self.currState.pressed();
	}
}

var light = new Light();
light.init();
~~~