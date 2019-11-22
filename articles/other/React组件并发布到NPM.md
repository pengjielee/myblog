实现步骤：
- 创建React组件项目；
- 创建测试项目并引用组件；
- 发布React组件到npm上；

#### 一、创建React组件项目,假设我们的组件名为react-cat

![react-cat项目结构](http://upload-images.jianshu.io/upload_images/822243-327783c16b32e62a..png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

创建react-cat目录：
~~~
//react-cat
> mkdir react-cat
> cd react-cat
> yarn init
~~~

安装依赖包:
~~~
//yarn add dependencies
yarn add babel-core babel-loader style-loader css-loader -D
yarn add react babel-preset-env babel-preset-react clean-webpack-plugin -D
yarn yarn add webpack webpack-cli -D
~~~

package.json
~~~
// react-cat/package.json
{
  "name": "react-cat",
  "version": "1.0.0",
  "main": "lib/index.js",
  "author": "pengjielee",
  "license": "MIT",
  "scripts": {
    "build": "webpack --progress",
    "watch": "webpack --watch --progress"
  },
  "devDependencies": {
    "babel-core": "^6.26.0",
    "babel-loader": "^7.1.4",
    "babel-preset-react": "^6.24.1",
    "clean-webpack-plugin": "^0.1.19",
    "css-loader": "^0.28.11",
    "react": "^16.2.0",
    "style-loader": "^0.20.3",
    "webpack": "^4.2.0",
    "webpack-cli": "^2.0.12"
  }
}
~~~

.gitignore
~~~
// react-cat/.gitignore
node_modules/
~~~

webpack.config.js
~~~
// react-cat/webpack.config.js
const path = require('path');
const CleanWebpackPlugin = require('clean-webpack-plugin');

module.exports = {
  mode: 'production', 
  
  entry: {
    index: './src/index.js'
  },

  output: {
    filename: '[name].js',
    path: path.resolve(__dirname, "lib"),
    libraryTarget: 'commonjs2'
  },

  module: {
    rules: [
      { 
        test: /\.js$/, 
        exclude: /node_modules/, 
        loader: 'babel-loader?presets[]=env&presets[]=react' 
      },
      { 
        test: /\.css$/, 
        use: ['style-loader','css-loader']
      }
    ]
  },

  plugins: [
    new CleanWebpackPlugin(['lib'])
  ]
}
~~~

src/components/hello.js
~~~
// react-cat/src/components/hello.js
import React from 'react';

import './hello.css'

class Hello extends React.Component {
  render() {
    return (
      Hello Cat!
    );
  }
}

module.exports =  Hello
~~~

src/components/hello.css
~~~
// react-cat/src/components/hello.css
body{
  padding:20px;
}

.hello{
  font-size: 30px;
  padding:20px 0;
  color:red;
}
~~~

src/index.js
~~~
// react-cat/src/index.js
import Hello from './components/Hello.js';

export default Hello
~~~

构建项目：
~~~
yarn run build
~~~

创建项目链接
~~~
yarn link
~~~

#### 二、创建测试项目
~~~
//pblog
yarn global add create-react-app
create-react-app pblog
~~~

![pblog项目结构](http://upload-images.jianshu.io/upload_images/822243-21a95677b8e603f5..png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

链接react-cat项目
~~~
yarn link ‘react-cat’
~~~

打开pblog/src/App.js，引入react-cat组件
~~~
// pblog/src/App.js
import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Hello from 'react-cat';
 
class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
        <Hello />
      </div>
    );
  }
}
 
export default App;
~~~

运行项目：
~~~
yarn run start
~~~

![image](http://upload-images.jianshu.io/upload_images/822243-9415fc264dfd3a70..png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 三、发布到npm上
- 注册npm账号 [npm](https://www.npmjs.com/)；
- 进入我们的react-cat组件项目,执行yarn login，输入npm用户名和密码；
- 发布我们的项目，执行yarn publish；


#### 四、遇到的问题
webpack生成组件项目的output的libraryTarget要设置为commonjs2
~~~
// react-cat/webpack.config.js
{
  ... 
  output: {
    filename: '[name].js',
    path: path.resolve(__dirname, "lib"),
    libraryTarget: 'commonjs2' //注意：记得设置commonjs2
  }
  ...
}
~~~
发布组件不成功的时候，搜一下npm上是否有同名组件

#### 五、参考文章
- [how-to-create-a-react-component-and-publish-it-in-npm](https://medium.com/@BrodaNoel/how-to-create-a-react-component-and-publish-it-in-npm-668ad7d363ce)
- [webpack output librarytarget](https://webpack.js.org/configuration/output/#output-librarytarget)
- [yarn link](https://yarnpkg.com/lang/zh-hans/docs/cli/link/)

