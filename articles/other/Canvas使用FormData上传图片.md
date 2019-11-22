~~~
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

var img = new Image();
var formData = new FormData();
var canvas = document.createElement('canvas');
var ctx = canvas.getContext('2d');

img.onload = function(){
  canvas.width = img.width;
  canvas.height = img.height;
  ctx.drawImage(img,0,0);
  canvas.toBlob(function(blob){
    formData.append('file',blob,'sprite.png');
    var xhr = new XMLHttpRequest();
    xhr.onload = function(e){
      if(xhr.status === 200){
        var response = JSON.parse(xhr.responseText);
        if(response.code == 0){
          console.log('upload success')
        }
      }else{
        console.log('upload fail')
      }
    }
    xhr.onerror = function(){
      console.log('upload error')
    }
    xhr.open("POST",'http://c.shijiebng.com/op/opfileupload/');
    xhr.send(formData);
  },'image/png');
};
img.src = src;
~~~

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

var formData = new FormData();
formData.append('file',blob);
~~~


canvas利用formdata上传到服务器
https://www.cnblogs.com/zhenfei-jiang/p/8206146.html