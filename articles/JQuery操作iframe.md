<iframe id="test" name="test" src="http://www.baidu.com" scrolling="auto" width="100%" height="100%"></iframe>

## iframe加载
$('#test').load(function () {
	var doc = $(this).contents();

	// 注册事件
	var search = doc.find('#su');
	search.click(function () {
	   console.log('search')
	});

	// 设置样式 
	doc.find('#kw').css('background','red')
}