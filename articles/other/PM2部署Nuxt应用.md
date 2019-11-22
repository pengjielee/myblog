### Nuxt.js应用部署

- nuxt	启动一个热加载的Web服务器（开发模式） localhost:3000。
- nuxt build	利用webpack编译应用，压缩JS和CSS资源（发布用）。
- nuxt start	以生产模式启动一个Web服务器 (nuxt build 会先被执行)。
- nuxt generate	编译应用，并依据路由配置生成对应的HTML文件 (用于静态站点的部署)。

~~~
{
	"scripts": {
	  "dev": "nuxt",
	  "build": "nuxt build",
	  "start": "nuxt start",
	  "generate": "nuxt generate"
	}
}
~~~

### PM2守护程序部署
~~~
$ yarn run build
$ pm2 start npm --name "my-nuxt" -- run start
~~~
