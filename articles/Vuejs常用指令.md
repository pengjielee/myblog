## 1. v-if/v-else-if/v-else

~~~
<template v-if="type === 'A'">
A
</template>
<template v-else-if="type === 'B'">
B
</template>
<template v-else-if="type === 'C'">
C
</template>
<template v-else>
D
</template>
~~~

## 2. v-show

~~~
show = true

<p v-if="show">你好啊~~</p>
<p v-show="show">你好啊~~</p>

v-if 是“真正”的条件渲染。
v-show 只是简单地基于 CSS 进行切换。
~~~


## 3. v-for
~~~
// foreach array
todos = [
  { text: 'learn vue' },
  { text: 'learn algorithm' },
  { text: 'learn flutter' }
]

<ol>
  <li v-for="(item,index) in todos">
    {{ item.text }}
  </li>
</ol>

// foreach object
object = {
	name: 'jie',
	age: 28,
	address: 'beijing'
}

<ol>
  <li v-for="(value,name,index) in object">
    {{ name }}: {{ value }}
  </li>
</ol>

// foreach number
<ol>
  <li v-for="n in 10">{{ n }} </li>
</ol>
~~~

## 4. v-bind
~~~
// bind value
data = {
  title: 'hello',
  id: 'save',
  disabled: true
}

<span v-bind:title="title"></span>
<div v-bind:id="id"></div>
<button v-bind:disabled="disabled">Button</button>

// bind class

data = {
  activeClass: 'active',
  errorClass: 'error',
  isActive: true
}

<div v-bind:class="{ active: isActive }"></div>

<div v-bind:class="[ activeClass, errorClass ]"></div>

<div v-bind:class="[ isActive ? activeClass : '', errorClass]"></div>

<div v-bind:class="[{ active: isActive }, errorClass]"></div>

// bind style

<div v-bind:style="{ color: 'red', fontSize: '30px' }"></div>

data: {
  styleObject: {
    color: 'red',
    fontSize: '30px'
  }
}
<div v-bind:style="styleObject"></div>


<div v-bind:style="[baseStyles, overridingStyles]"></div>
~~~

## 5. v-html
~~~
data: {
  rawHtml: '<span style="color:red;">hello world</span>'
}

<p v-html="rawHtml"></p>
~~~

## 6. v-on
~~~
<a v-on:click="save.stop.prevent">save</a>

<a @click="save.stop.prevent">save</a>
~~~