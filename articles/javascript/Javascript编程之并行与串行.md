假设给定一组url，要求尽可能快得加载，然后按照顺序打印出结果，用js如何实现？

分析：
因为要求尽可能快，所以要并行加载
因为要求按顺序打印结果，那么就要串行输出

将问题简化一下，请求url的异步任务换成简单地输出数字。

```
let makePromise = (value) => {
    console.log("sync", value)
    return new Promise(resolve => {
        setTimeout(() => {
            console.log("async", value)
            resolve(value)
        }, Math.random() * 1000)
    })
}

let print = (value) => {
    console.log("print", value)
    return value
}

let values = [1, 2, 3, 4]
let promises = values.map(value => makePromise(value)) // 这里就已经开始并行加载

let parallelPromises = promises.reduce(
    (current, next) => current.then(() => next.then(print)),
    Promise.resolve()
)

parallelPromises
    .then(() => console.log("done"))
    .catch(() => console.log("failed"))


// Promise.all(promises).then(function(values){
// 	console.log(values)
// })
```

# More
[https://lxzjj.github.io/2017/10/29/%E4%B8%80%E6%AC%A1js%E5%B9%B6%E8%A1%8C%E4%B8%B2%E8%A1%8C%E7%9A%84%E6%80%9D%E8%80%83/](https://lxzjj.github.io/2017/10/29/%E4%B8%80%E6%AC%A1js%E5%B9%B6%E8%A1%8C%E4%B8%B2%E8%A1%8C%E7%9A%84%E6%80%9D%E8%80%83/)