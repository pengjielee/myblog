组合模式就是用小的对象来构建更大的对象，而这些小的对象本身也许是由更小的子对象构成的。

~~~
var openDoorCommand = {
	execute: function(){
		console.log('open the door');
	}
}

var openWindowCommand = {
	execute: function(){
		console.log('open the window');
	}
}

var openComputerCommand = {
	execute: function(){
		console.log('open the computer');
	}
}

var openLightCommand = {
	execute: function(){
		console.log('open the light');
	}
}

var closeLightCommand = {
	execute: function(){
		console.log('close the light');
	}
}

var MacroCommand = function(){
	return{
		commandList: [],
		add: function(command){
			this.commandList.push(command);
		},
		execute: function(){
			this.commandList.forEach(function(command){
				command.execute();
			})
		}
	}
}

var macroCommand = MacroCommand();
macroCommand.add(openDoorCommand);
macroCommand.add(openWindowCommand);
macroCommand.add(openComputerCommand);

var lightCommand = MacroCommand();
lightCommand.add(openLightCommand);
lightCommand.add(closeLightCommand);

macroCommand.add(lightCommand);

macroCommand.execute();
~~~