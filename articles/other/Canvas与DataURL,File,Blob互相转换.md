### 1. Canvas转换为dataURL

toDataURL(in optional DOMString type, in any ...args)

返回一个data: URL,根据type参数指定的类型将包含在canvas中的图片文件编码成字符串形式, type参数的默认值为image/png.
- 如果该canvas的宽度或长度是0,则会返回字符串"data:,".
- 如果指定的type参数不是image/png,但返回的字符串是以data:image/png开头的,则所请求的图片类型不支持.Chrome支持image/webp类型.
- 如果type参数的值为image/jpeg或image/webp,则第二个参数的值如果在0.0和1.0之间的话,会被看作是图片质量参数,如果第二个参数的值不在0.0和1.0之间,则会使用默认的图片质量.

~~~
var dataUrl1 = canvas.toDataURL('image/png');
var dataUrl2 = canvas.toDataURL('image/png',0.8);
~~~

### 2. Canvas转换为Blob对象

toBlob(in Function callback, in optional DOMString type, in any ...args) 

返回一个Blob对象,表示了包含在该canvas中的图片文件,这个文件可能缓存在硬盘上,也可能存储在内存中,这由浏览器决定.如果没有指定type参数,则默认使用image/png.

~~~
// A low performance polyfill based on toDataURL.

if (!HTMLCanvasElement.prototype.toBlob) {
 Object.defineProperty(HTMLCanvasElement.prototype, 'toBlob', {
  value: function (callback, type, quality) {

    var binStr = atob( this.toDataURL(type, quality).split(',')[1] ),
        len = binStr.length,
        arr = new Uint8Array(len);

    for (var i=0; i<len; i++ ) {
     arr[i] = binStr.charCodeAt(i);
    }
    callback( new Blob( [arr], {type: type || 'image/png'} ) );
  }
 });
}

canvas.toBlob(function(blob){
	var fd = new FormData();
  fd.append('file',blob,'sprite.png');

  var xhr = new XMLHttpRequest();
  xhr.onload = function(){};
  xhr.onerror = function(){};
  xhr.open("POST",'/server');
  xhr.send(fd);

  },'image/png');
~~~


### 3. dataURL图片数据绘制到Canvas

~~~
var img = new Image();
img.onload = function(){
	canvas.drawImage(img,0,0);
};
img.src = dataUrl;
~~~

### 4. dataURL转换为Blob对象

~~~
function dataURLtoBlob(dataURL) {//图片转成Buffer
	var byteString = atob(dataURL.split(',')[1]);
	var mimeString = dataURL.split(',')[0].split(':')[1].split(';')[0];
	var ab = new ArrayBuffer(byteString.length);
	var ia = new Uint8Array(ab);
	for (var i = 0; i < byteString.length; i++) {
	   ia[i] = byteString.charCodeAt(i);
	}
	return new Blob([ab], {type: mimeString});
}
var dateURI = canvas.toDataURL("image/png");
var blob = dataURLtoBlob(dateURI);
~~~

### 5. Blob/File对象转换为dataURL（File对象也是一个Blob对象）

~~~
function readBlobAsDataURL(blob, callback) {
  var reader = new FileReader();
  reader.onload = function(e) { 
  	callback(e.target.result);
  };
  reader.readAsDataURL(blob);
}

readBlobAsDataURL(blob, function (dataurl){
    console.log(dataurl);
});
readBlobAsDataURL(file, function (dataurl){
    console.log(dataurl);
});
~~~

### 6. Blob/File的图片文件数据绘制到Canvas

先转换成一个url，然后构造Image对象，src为dataURL，图片onload之后绘制到Canvas.

~~~
// 调用5
readBlobAsDataURL(blob, function(dataUrl){
	var img = new Image();
	img.onload = function(){
		canvas.drawImage(img,0,0);
	};	
	img.src = dataUrl;
});
~~~

### 7. dataURL转换为File对象

~~~
function dataURLtoFile(dataurl, filename) {
  var arr = dataurl.split(','), mime = arr[0].match(/:(.*?);/)[1],
      bstr = atob(arr[1]), n = bstr.length, u8arr = new Uint8Array(n);
  while(n--){
      u8arr[n] = bstr.charCodeAt(n);
  }
  return new File([u8arr], filename, {type:mime});
}
~~~


### 参考：  
HTMLCanvas元素接口
https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLCanvasElement

HTMLCanvasElement.toBlob()
https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLCanvasElement/toBlob

DataURL与File,Blob,canvas对象之间的互相转换的Javascript
https://blog.csdn.net/cuixiping/article/details/45932793