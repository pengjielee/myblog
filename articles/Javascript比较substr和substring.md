### substr()  

substr() 方法可在字符串中抽取从 start 下标开始的指定数目的字符。  
 
stringObject.substr(start,length)  
start   必需。要抽取的子串的起始下标。必须是数值。如果是负数，那么该参数声明从字符串的尾部开始算起的位置。也就是说，-1 指字符串中最后一个字符，-2 指倒数第二个字符，以此类推。  
length  可选。子串中的字符数。必须是数值。如果省略了该参数，那么返回从 stringObject 的开始位置到结尾的字串。  

返回值  
一个新的字符串，包含从 stringObject 的 start（包括 start 所指的字符） 处开始的 length 个字符。如果没有指定 length，那么返回的字符串包含从 start 到 stringObject 的结尾的字符。  

重要事项：ECMAscript 没有对该方法进行标准化，因此反对使用它。  

~~~
var name = 'lipengjie';
console.log(name.substr(0)); // lipengjie
console.log(name.substr(0,2)); // li
console.log(name.substr(-1,1)); // e
console.log(name.substr(-1,2)); // e
~~~

## substring()  

substring() 方法用于提取字符串中介于两个指定下标之间的字符。  

stringObject.substring(start,stop)  
start   必需。一个非负的整数，规定要提取的子串的第一个字符在 stringObject 中的位置。  
stop    可选。一个非负的整数，比要提取的子串的最后一个字符在 stringObject 中的位置多 1。  
如果省略该参数，那么返回的子串会一直到字符串的结尾。  

返回值  
一个新的字符串，该字符串值包含 stringObject 的一个子字符串，其内容是从 start 处到 stop-1 处的所有字符，其长度为 stop 减 start。  

注意：  
substring() 方法返回的子串包括 start 处的字符，但不包括 stop 处的字符。

如果参数 start 与 stop 相等，那么该方法返回的就是一个空串（即长度为 0 的字符串）。如果 start 比 stop 大，那么该方法在提取子串之前会先交换这两个参数。  

重要事项：与 slice() 和 substr() 方法不同的是，substring() 不接受负的参数。  

~~~
var name = 'lipengjie';
console.log(name.substring(1)); //ipengjie
console.log(name.substring(0,2)); //li
console.log(name.substring(0,100)); //lipengjie
console.log(name.substring(2,0)); //li
~~~

## slice()

slice() 方法可提取字符串的某个部分，并以新的字符串返回被提取的部分。  

stringObject.slice(start,end)  

start 要抽取的片断的起始下标。如果是负数，则该参数规定的是从字符串的尾部开始算起的位置。也就是说，-1 指字符串的最后一个字符，-2 指倒数第二个字符，以此类推。  
end 紧接着要抽取的片段的结尾的下标。若未指定此参数，则要提取的子串包括 start 到原字符串结尾的字符串。如果该参数是负数，那么它规定的是从字符串的尾部开始算起的位置。  

返回值  
一个新的字符串。包括字符串 stringObject 从 start 开始（包括 start）到 end 结束（不包括 end）为止的所有字符。  
~~~
var name = 'lipengjie';
console.log(name.slice(0)); //lipengjie
console.log(name.slice(0,2)); //li
console.log(name.slice(-1)); //e
console.log(name.slice(-1,-2)); //''
console.log(name.slice(-2,-1)); //i
~~~