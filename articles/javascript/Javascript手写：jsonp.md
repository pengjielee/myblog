尽管浏览器有同源策略，但是 <script> 标签的 src 属性不会被同源策略所约束，可以获取任意服务器上的脚本并执行。 jsonp 通过插入 script 标签的方式来实现跨域，参数只能通过 url 传入，仅能支持 get 请求。

实现原理：
step1: 创建 callback 方法
step2: 插入 script 标签
step3: 后台接受到请求，解析前端传过去的 callback 方法，返回该方法的调用，并且数据作为参数传入该方法
step4: 前端执行服务端返回的方法调用

实现1:
```
function jsonp(url, params, callback) {
	return new Promise((resolve,reject) => {
		// 创建script标签
		let script = document.createElement("script");
		// 将回调函数挂在 window 上
		window[callback] = function(data){
			resolve(data);
			// 代码执行后，删除插入的script标签
			document.body.removeChild(script);
		}
		// 回调函数加在请求地址上
		params = {...params, callback}
		let arrs = [];
		for(let key in params){
			arrs.push(`${key}=${params[key]}`);
		}
		script.src = `${url}?${arrs.join('&')}`;
		document.body.appendChild(script);
	})
}
```

实现2：
```
var Jsonp = {
  loadScript: function(url){
      var script = document.createElement("script");
      script.type = "text/javascript";
      if(script.readyState){
          script.onreadystatechange = function(){
             if(this.readyState == "loaded" || this.readyState == "complete"){   
                  this.onreadystatechange = null; 
                  document.body.removeChild(this);
             }
          };
      }else {
          script.onload = function(){
              document.body.removeChild(this);
          };
      }
      script.setAttribute('src', url);
      document.body.appendChild(script);
  },
  encodeParameters: function(parameters){
      var paras = [];
      for (parameter in parameters){
          paras.push(escape(parameter) + "=" + escape(parameters[parameter]));
      }
      return paras.length>0?'?'+paras.join('&'):'';
  },
  request: function(url, param){
      this.loadScript(url + this.encodeParameters(param) );
  }
};

Jsonp.request("http://www.baidu.com", {"callback":"callback", "t":new Date().getTime()});
```