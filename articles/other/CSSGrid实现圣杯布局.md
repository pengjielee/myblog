#### 什么是圣杯布局？
一个header
一个footer
三列等高的body，两个侧边栏+主内容区域

![image](http://upload-images.jianshu.io/upload_images/822243-5622db5cf26b05c4..png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 定义HTML结构：
~~~
<div class="container">
  <header class="header">header</header>
  <aside class="aside-left">aside left</aside>
  <main class="main">main</main>
  <aside class="aside-right"></aside>
  <footer class="footer"></footer>
</div>
~~~

#### 定义Grid:
~~~
.header{
  grid-area: header;
}
.footer{
  grid-area: footer; 
}
.main{
  grid-area: main;
}
.aside-left{
  grid-area: aside-left;
}
.aside-right{
  grid-area: aside-right;
}
.container{
  display: grid;
  grid-template-areas: 
          'header header header'
          'aside-left main aside-right'
          'footer footer footer';
  min-height: 100vh;
}
~~~

#### 定义列的宽度：
~~~
.container{
  grid-template-columns: 200px 1fr 200px;
}
~~~

#### 定义行的高度：
~~~
.container{
  grid-template-rows: 50px 1fr 50px;
}
~~~

#### 添加响应式：
~~~
@media screen and (max-width: 600px) {
  .container{
    grid-template-areas: 
      'header' 
      'aside-left'
      'main'
      'aside-right'
      'footer';
    grid-template-columns: 100%;
    grid-template-rows: 50px 50px minmax(300px, auto) 50px 80px;
  }
  .aside-left,.aside-right,.main{
    display:flex;
    align-items:center;
    justify-content: center;
  }
}
~~~
![移动端效果](http://upload-images.jianshu.io/upload_images/822243-3110c3964c3aa754..png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

查看效果：[holy grail layout](http://m.pengjielee.cn/holygrail03.html)  
关于圣杯布局：[holygrail](http://alistapart.com/article/holygrail)  
CSS Grid浏览器支持：[css grid browser support](https://caniuse.com/#feat=css-grid)  
![image](http://upload-images.jianshu.io/upload_images/822243-1f1e9e8e1e493749..png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

