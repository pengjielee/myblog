## 防抖（Debouncing）

防抖技术即是可以把多个顺序地调用合并成一次，也就是在一定时间内，规定事件被触发的次数。

```
// 简单的防抖动函数
function debounce(func, wait, immediate) {
  // 定时器变量
  var timeout;
  return function() {
    // 每次触发 scroll handler 时先清除定时器
    clearTimeout(timeout);
    // 指定 xx ms 后触发真正想进行的操作 handler
    timeout = setTimeout(func, wait);
  };
};

// 实际想绑定在 scroll 事件上的 handler
function realFunc(){
  console.log("Success");
}

// 采用了防抖动
window.addEventListener('scroll',debounce(realFunc,500));
// 没采用防抖动
window.addEventListener('scroll',realFunc);

// 防抖动函数
function debounce(func, wait, immediate) {
  var timeout;
  return function() {
      var context = this, args = arguments;
      var later = function() {
          timeout = null;
          if (!immediate) func.apply(context, args);
      };
      var callNow = immediate && !timeout;
      clearTimeout(timeout);
      timeout = setTimeout(later, wait);
      if (callNow) func.apply(context, args);
  };
};
```

## 节流（Throttling）

节流函数：只允许一个函数在X毫秒内执行一次，只有当上一次函数执行后过了你规定的时间间隔，才能进行下一次该函数的调用。

与防抖相比，节流函数最主要的不同在于它保证在X毫秒内至少执行一次我们希望触发的事件handler。
节流函数多了一个mustRun属性，代表mustRun毫秒内，必然会触发一次 handler。

```
// 简单的节流函数
function throttle(func, wait, mustRun) {
  var timeout,startTime = new Date();

  return function() {
    var context = this,
      args = arguments,
      curTime = new Date();

    clearTimeout(timeout);
    // 如果达到了规定的触发时间间隔，触发 handler
    if(curTime - startTime >= mustRun){
      func.apply(context,args);
      startTime = curTime;
    // 没达到触发间隔，重新设定定时器
    }else{
      timeout = setTimeout(func, wait);
    }
  };
};
// 实际想绑定在 scroll 事件上的 handler
function realFunc(){
  console.log("Success");
}
// 采用了节流函数
window.addEventListener('scroll',throttle(realFunc,500,1000));
```

## More 

[如何不择手段提升scroll事件的性能](https://zhuanlan.zhihu.com/p/30078937?group_id=903286564285767680)  
https://zhuanlan.zhihu.com/p/30078937?group_id=903286564285767680

[高性能滚动scroll及页面渲染优化](https://github.com/chokcoco/cnblogsArticle/issues/12) 
https://github.com/chokcoco/cnblogsArticle/issues/12 
