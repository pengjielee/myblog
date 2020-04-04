Object.create创建一个新对象，使用现有的对象来提供新创建的对象的__proto__，第二个可选参数为属性描述对象

```
function objectCreate_(proto, propertiesObject = {}){
  if(typeof proto !== 'object' || typeof proto !== 'function' || proto !== null){
    throw('Object prototype may only be an Object or null:'+proto)
  }
  let res = {}
  res.__proto__ = proto
  Object.defineProperties(res, propertiesObject)
  return res
}
```