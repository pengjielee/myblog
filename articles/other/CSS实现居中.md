html结构：
```
<div class="container">
	<div class="main">main</div>
</div>
```

css样式：
```
*{ margin: 0;padding: 0;box-sizing:border-box;}
html,body{ width: 100%; height: 100%; }
.container{ border:1px solid red; width:100%;height:100%;}
.container>.main{ border:1px solid blue;}
```

## center01: 不知道父元素和子元素宽高 
```
.container{ position: relative;}
.container>.main{ position: absolute;left:50%;top:50%;transform:translate(-50%,-50%);}
```

## center02: 知道父元素宽高，不知道子元素宽高 
```
.container>.main{ position: relative;top: 50%;transform:translateY(-50%);text-align: center;}
```

## center03: 知道子元素宽高（绝对定位+负外边距）
```
.container>.main{ width:100px; height: 100px; position: absolute; top:50%; left:50%;margin-left:-50px;margin-top: -50px;}
```

## center04: 知道子元素宽高（margin+transform） 
```
.container>.main{ width:100px; height: 100px; margin:0 auto;position: relative;top:50%;transform:translateY(-50%);}
```

## center05: table实现
``` 
.container{ display: table;}
.container>.main{ display: table-cell;vertical-align: middle;text-align: center;}
```

## center06: line-height实现 
```
.container{ height:300px; line-height:300px; }
.container>.main{ text-align: center;}
```

## center07: flex实现1 
```
.container{ display: flex; height:100vh;}
.container>.main{ margin:auto;}
```

## center08: flex实现2 
```
.container{ display: flex; align-items:center; justify-content:center;}
```
