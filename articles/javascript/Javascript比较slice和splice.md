## splice()

splice() 方法向/从数组中添加/删除项目，然后返回被删除的项目。  
注释：该方法会改变原始数组。  
arrayObject.splice(index,howmany,item1,.....,itemx)  

参数  描述  
index   必需。整数，规定添加/删除项目的位置，使用负数可从数组结尾处规定位置。  
howmany 必需。要删除的项目数量。如果设置为 0，则不会删除项目。  
item1, ..., itemx   可选。向数组添加的新项目。  

返回值  
Array   包含被删除项目的新数组，如果有的话。  

说明  
splice() 方法可删除从 index 处开始的零个或多个元素，并且用参数列表中声明的一个或多个值来替换那些被删除的元素。  
如果从 arrayObject 中删除了元素，则返回的是含有被删除的元素的数组。  

注意，splice() 方法与 slice() 方法的作用是不同的，splice() 方法会直接对数组进行修改。  

~~~
var numbers = [ 1,2,3 ]
numbers.splice(0,0,4) //在数组0处添加一个元素4
console.log(numbers) // [4,1,2,3]

numbers = [ 1,2,3 ]
numbers.splice(2,0,4) //在数组2处添加一个元素4
console.log(numbers) // [1,2,4,3]

numbers = [ 1,2,3 ]
numbers.splice(2,1,4) //删除数组2处的元素，并替换为4
console.log(numbers) // [1,2,4]

numbers = [ 1,2,3 ]
numbers.splice(1,1,4,5) //删除数组1处的元素，并替换为4,5
console.log(numbers) // [1,4,5,3]

numbers = [ 1,2,3 ]
numbers.splice(0,1) //删除数组从0开始的1个元素
console.log(numbers) // [2,3]

numbers = [ 1,2,3 ]
numbers.splice(1,2) //删除数组从1开始的1个元素
console.log(numbers) // [1]
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