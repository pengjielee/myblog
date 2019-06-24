### CommonJS

Javascript不仅仅适用于浏览器。  

CommonJS API将通过定义处理许多常见应用程序需求的API来填补这一空白，最终提供与Python，Ruby和Java一样丰富的标准库。其目的是让应用程序开发人员能够使用CommonJS API编写应用程序，然后在不同的JavaScript解释器和主机环境中运行该应用程序。  

通过CommonJS兼容系统，您可以使用JavaScript编写：  
a. 服务器端JavaScript应用程序；  
b. 命令行工具；  
c. 基于桌面GUI的应用程序； 
d. 混合应用程序（Titanium，Adobe AIR）；  

CommonJS是一个项目，其目标是在浏览器外部（例如，在服务器上或为本地桌面应用程序）指定JavaScript的生态系统。  
 
CommonJS项目历史：  
2009年1月：在Kevin Dangoor的火星上的蓝天博客文章后，该小组成立为“ServerJS”  
2009年3月：尘埃落定于“安全模块”，作为该组的模块风格。这是CommonJS API 0.1  
2009年4月：CommonJS模块在华盛顿第一个JSConf上展示了几个实现。  
2009年8月：该组名正式更改为CommonJS以反映API的更广泛适用性。  

node.js的模块系统，就是参照CommonJS规范实现的。  
在CommonJS中，有一个全局性方法require()，用于加载模块。  

~~~
var math = require('math');  
math.add(2,3); // 5
~~~

但是，由于一个重大的局限，使得CommonJS规范不适用于浏览器环境。 

第二行math.add(2, 3)，在第一行require('math')之后运行，因此必须等math.js加载完成。也就是说，如果加载时间很长，整个应用就会停在那里等。   

http://www.commonjs.org/

Commonjs解决了模块化的问题，并且可以用在浏览器中，但是Commonjs是同步加载模块，当要用到该模块了，现加载现用，这种同步机制到了浏览器里边就有问题了，加载速度啊啥的（览器同步加载模块会导致性能、可用性、调试和跨域访问等问题）。    

### AMD

AMD和Commonjs是兼容的，只要稍稍调换一下调用方法就实现了同步加载。

浏览器端的模块，不能采用"同步加载"（synchronous），只能采用"异步加载"（asynchronous）。这就是AMD规范诞生的背景。  

AMD是"Asynchronous Module Definition"的缩写，意思就是"异步模块定义"。它采用异步方式加载模块，模块的加载不影响它后面语句的运行。所有依赖这个模块的语句，都定义在一个回调函数中，等到加载完成之后，这个回调函数才会运行。  

AMD也采用require()语句加载模块，但是不同于CommonJS，它要求两个参数：
~~~  
require([module], callback);  
~~~

目前，主要有两个Javascript库实现了AMD规范：require.js和curl.js。  

### CMD

CMD(Common Module Definition)，是seajs推崇的规范，CMD则是依赖就近，用的时候再require。 

淘宝的玉伯大牛搞了个seajs出来，并声称这个规范是遵循CMD规范的。  

Seajs也是预加载依赖js跟AMD的规范在预加载这一点上是相同的，明显不同的地方是调用，和声明依赖的地方。
AMD和CMD都是用difine和require，但是CMD标准倾向于在使用过程中提出依赖，就是不管代码写到哪突然发现需要依赖另一个模块，那就在当前代码用require引入就可以了，规范会帮你搞定预加载，你随便写就可以了。但是AMD标准让你必须提前在头部依赖参数部分写好（没有写好？ 倒回去写好咯）。这就是最明显的区别。

AMD和CMD的区别：
1. 对于依赖的模块，AMD是提前执行，CMD是延迟执行。不过RequireJS从2.0开始，也改成可以延迟执行（根据写法不同，处理方式不同）。CMD推崇aslazyaspossible.  
2. CMD推崇依赖就近，AMD推崇依赖前置。  
3. AMD的API默认是一个当多个用，CMD的API严格区分，推崇职责单一。比如AMD里，require分全局require和局部require，都叫require。CMD里，没有全局require，而是根据模块系统的完备性，提供seajs.use来实现模块系统的加载启动。CMD里，每个API都简单纯粹。  

AMD和CMD最大的区别是对依赖模块的执行时机处理不同，而不是加载的时机或者方式不同，二者皆为异步加载模块。
AMD依赖前置，js可以方便知道依赖模块是谁，立即加载； 
CMD就近依赖，需要使用把模块变为字符串解析一遍才知道依赖了那些模块，这也是很多人诟病CMD的一点，牺牲性能来带来开发的便利性，实际上解析模块用的时间短到可以忽略。   

### ES6 MODULE

在 ES6 之前，社区制定了一些模块加载方案，最主要的有 CommonJS 和 AMD 两种。 
前者用于服务器，后者用于浏览器。ES6 在语言标准的层面上，实现了模块功能，而且实现得相当简单，完全可以取代 CommonJS 和 AMD 规范，成为浏览器和服务器通用的模块解决方案。

~~~
// ES6模块
import { stat, exists, readFile } from 'fs';
~~~

上面代码的实质是从fs模块加载 3 个方法，其他方法不加载。这种加载称为“编译时加载”或者静态加载，即 ES6 可以在编译时就完成模块加载，效率要比 CommonJS 模块的加载方式高。当然，这也导致了没法引用 ES6 模块本身，因为它不是对象。  
 
除了静态加载带来的各种好处，ES6模块还有以下好处：  
a.不再需要UMD模块格式了，将来服务器和浏览器都会支持 ES6 模块格式。目前，通过各种工具库，其实已经做到了这一点。  
b.将来浏览器的新 API 就能用模块格式提供，不再必须做成全局变量或者navigator对象的属性。  
c.不再需要对象作为命名空间（比如Math对象），未来这些功能可以通过模块提供。  
    