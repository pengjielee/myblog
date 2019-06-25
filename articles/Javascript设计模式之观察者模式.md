观察者模式，又叫发布者-订阅者模式 。

观察者模式可以很好的实现两个模块之间的解耦。 

好莱坞有句名言。“不要给我打电话， 我会给你打电话”.  其中“我”是发布者， “你”是订阅者。

我来公司面试的时候，完事之后每个面试官都会对我说：“请留下你的联系方式， 有消息我们会通知你”。 在这里“我”是订阅者， 面试官是发布者。

观察者模式实现：面试者把简历扔到一个盒子里， 然后面试官在合适的时机拿着盒子里的简历挨个打电话通知结果.

~~~
Events = function() {
 
    var listen, log, obj, one, remove, trigger, __this;
    obj = {};
    __this = this;
 
    listen = function( key, eventfn ) {  
      //把简历扔盒子, key就是联系方式.
      var stack, _ref;  
      //stack是盒子
      stack = ( _ref = obj[key] ) != null ? _ref : obj[ key ] = [];
      return stack.push( eventfn );
    };
 
    one = function( key, eventfn ) {
      remove( key );
      return listen( key, eventfn );
    };

    remove = function( key ) {
      var _ref;
      return ( _ref = obj[key] ) != null ? _ref.length = 0 : void 0;
    };

    trigger = function() {  
         //面试官打电话通知面试者
         var fn, stack, _i, _len, _ref, key;
         key = Array.prototype.shift.call( arguments );
         stack = ( _ref = obj[ key ] ) != null ? _ref : obj[ key ] = [];
         for ( _i = 0, _len = stack.length; _i < _len; _i++ ) {
               fn = stack[ _i ];
               if ( fn.apply( __this,  arguments ) === false) {
                 return false;
               }
         }
         return {
            listen: listen,
            one: one,
            remove: remove,
            trigger: trigger
         }
    };
}
~~~
