实现步骤：
- 绘制一个圆；
- 绘制圆环；
- 绘制进度环；
- 绘制文字；

#### 一、创建画布
~~~
<canvas id='myCanvas'></canvas>
~~~

#### 二、绘制一个圆
~~~
var canvas = document.getElementById('myCanvas1');
var ctx = canvas.getContext('2d');
ctx.beginPath();
ctx.arc(100, 100, 50, 0, 2 * Math.PI, false);
ctx.strokeStyle = 'red'; 
ctx.stroke();
~~~
![显示效果](http://upload-images.jianshu.io/upload_images/822243-04561a67acea07b7..png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


#### 三、绘制圆环：
~~~
var canvas = document.getElementById('myCanvas1');
var ctx = canvas.getContext('2d');
ctx.beginPath();
ctx.arc(100, 100, 50, 0, 2 * Math.PI, false);

// new added
ctx.lineWidth = 15;

ctx.strokeStyle = 'red'; 
ctx.stroke();
~~~
![显示效果](http://upload-images.jianshu.io/upload_images/822243-e8e096c3e52c9743..png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 四、绘制进度环
~~~
var canvas = document.getElementById('myCanvas1');
var ctx = canvas.getContext('2d');
ctx.beginPath();
ctx.arc(100, 100, 50, 0, 2 * Math.PI, false);
ctx.lineWidth = 15;
ctx.strokeStyle = 'red'; 
ctx.stroke();

//new added
var startAngle = 3 / 2 * Math.PI; //开始位置弧度
var percentage = 10;  //完成进度值 
var diffAngle = percentage / 100 * Math.PI * 2; //完成进度弧度值
ctx.beginPath();
ctx.arc(100, 100, 50, startAngle, diffAngle + startAngle, false);
ctx.strokeStyle = 'green';
ctx.stroke();
~~~
![显示效果](http://upload-images.jianshu.io/upload_images/822243-fda367cdc2dd0ce6..png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


#### 五、绘制文字
~~~
var canvas = document.getElementById('myCanvas1');
var ctx = canvas.getContext('2d');
ctx.beginPath();
ctx.arc(100, 100, 50, 0, 2 * Math.PI, false);
ctx.lineWidth = 15;
ctx.strokeStyle = 'red'; 
ctx.stroke();

var startAngle = 3 / 2 * Math.PI; //开始位置弧度
var percentage = 10;  //完成进度值 
var diffAngle = percentage / 100 * Math.PI * 2; //完成进度弧度值
ctx.beginPath();
ctx.arc(100, 100, 50, startAngle, diffAngle + startAngle, false);
ctx.strokeStyle = 'green';
ctx.stroke();

//new added
ctx.fillStyle = '#000';
ctx.textAlign = 'center';
ctx.font = '16px serif';
ctx.fillText(percentage + '%', 100+2, 100+5);
~~~
![显示效果](http://upload-images.jianshu.io/upload_images/822243-f694206b7abeca5d..png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


#### 六、完整代码
~~~
(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
    define(factory);// AMD
  } else if (typeof exports === 'object' && typeof module !== 'undefined') {
    module.exports = factory(); // CommonJS
  } else {
    window.Progressbar = factory(); // Browser globals
  }
}(this, function () {
  function Progressbar(options){
    this.id = options.id;
    this.value = options.value || 0;
    this.width = options.width || 200;
    this.height = options.height || 200;
    this.bgColor = options.bgColor || 'green';
    this.barColor = options.barColor || 'red';
    this.fontColor = options.fontColor || '#000';
    if(options.init){
      this.init();
    }
  }
  Progressbar.prototype.init = function(){
    var canvas = document.getElementById(this.id);

    if(!canvas.getContext) {
      throw new Error('your browser does not support canvas')
    }

    if(!this.id){
      throw new Error('your need pass id ')
    }

    var width = parseInt(this.width);
    var height = parseInt(this.height);
    canvas.setAttribute('width',width);
    canvas.setAttribute('height',height);

    var ctx = canvas.getContext("2d");

    var startAngle = 3 / 2 * Math.PI;
    var percentage = 0;
    var diffAngle = 0;
    var cx = width / 2;
    var cy = height / 2;
    var timer = setInterval(draw, 50);
    var value = this.value;
    var bgColor = this.bgColor;
    var barColor = this.barColor;
    var fontColor = this.fontColor;

    function draw(){
      diffAngle = (percentage / 100) * Math.PI * 2;

      //清除矩形区域
      ctx.clearRect(0, 0, width, height);

      ctx.beginPath();

      //设置线段宽度
      ctx.lineWidth = 15;

      //绘制圆
      ctx.arc(cx, cy, 50, 0, 2 * Math.PI, false);

      //设置填充色
      ctx.fillStyle = '#FFF';
      ctx.fill();

      //绘制图形轮廓
      ctx.strokeStyle = bgColor; 
      ctx.stroke();

      //绘制百分比进度
      ctx.beginPath();
      ctx.arc(cx, cy, 50, startAngle, diffAngle + startAngle, false);
      ctx.strokeStyle = barColor;
      ctx.stroke();

      //绘制百分比文字
      ctx.fillStyle = fontColor;
      ctx.textAlign = 'center';
      ctx.font = '16px serif';
      ctx.fillText(percentage + '%', cx, cy + 6);

      if (percentage >= value) {
        clearTimeout(timer);
      }

      percentage++;
    }
  }
  return Progressbar;
}));

var progressbar1 = new Progressbar({ id: 'myCanvas1',value: 20 ,init: true })
var progressbar2 = new Progressbar({ id: 'myCanvas2',value: 30 ,init: true })
~~~

#### 七、查看效果
[进度条](https://m.pengjielee.cn/progress.html)

#### 八、参考资料
[使用canvas来绘制图形](https://developer.mozilla.org/zh-CN/docs/Web/API/Canvas_API/Tutorial/Drawing_shapes)

