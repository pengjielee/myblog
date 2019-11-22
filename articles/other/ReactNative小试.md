### 创建项目
~~~
- 安装create-react-native-app
yarn global add create-react-native-app

- 快速创建项目
create-react-native-app Haoji

- 运行项目
cd Haoji && yarn start

- 安装expo客户端，扫描终端上的二维码
~~~

### 项目结构
~~~
src   //项目源码      
----components //基础组件
----navigation //导航路由
----screens    //页面组件
----utils      //工具类
.babelrc
.gitignore
App.js //入口文件
app.json
package.json
README.md
~~~
![最终项目结构](http://upload-images.jianshu.io/upload_images/822243-7cd4b3fbf11b206b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


### API设计
~~~
- 笔记列表
url: http://m.pengjielee.cn/api/v1/notes
method: get
params: page: 1, size: 10

- 创建笔记
url: http://m.pengjielee.cn/api/v1/notes
method: post
params: title: '', content: ''

- 笔记详情
url: http://m.pengjielee.cn/api/v1/notes/:id
method: get

- 笔记删除
url: http://m.pengjielee.cn/api/v1/notes/:id
method: delete
~~~

### UI设计

![笔记列表页](http://upload-images.jianshu.io/upload_images/822243-b21bb904ef3e0fd6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![笔记详情页](http://upload-images.jianshu.io/upload_images/822243-220d3271da4715e4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![新建笔记页](http://upload-images.jianshu.io/upload_images/822243-bb9d8b43d7a91857.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![个人中心页](http://upload-images.jianshu.io/upload_images/822243-a7707f1fa6ba9f81.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![设置页](http://upload-images.jianshu.io/upload_images/822243-3bbf8a1b7a9d55bd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


### 页面设计
- 笔记列表页 [ Haoji/src/screens/NoteListScreen.js ]
- 笔记详情页 [ Haoji/src/screens/NoteDetailScreen.js ]
- 新建笔记页 [ Haoji/src/screens/NewNoteScreen.js ]
- 个人中心页 [ Haoji/src/screens/MeScreen.js ]
- 设置页 [ Haoji/src/screens/SettingScreen.js ]

### 导航设计
- Notes      （笔记列表）
- Details    （笔记详情） 
- NewNote （新建笔记）
- Me           （个人中心）
- Setting    （设置）

Note栈导航：
~~~
export const NoteStack = StackNavigator({
  Notes: {
    screen: NoteListScreen,
    navigationOptions: {
      title: "Note List",
      headerStyle: {
        backgroundColor: "#f36838"
      },
      headerTintColor: "#fff"
    }
  },
  Details: {
    screen: NoteDetailScreen,
    navigationOptions: {
      title: "Note Detail",
      headerStyle: {
        backgroundColor: "#f36838"
      },
      headerTintColor: "#fff"
    }
  }
});
~~~

新建笔记栈导航
~~~
export const NewNoteStack = StackNavigator({
  NoteNote: {
    screen: NewNoteScreen,
    navigationOptions: {
      title: "New Note",
      headerStyle: {
        backgroundColor: "#4b5cc4"
      },
      headerTintColor: "#fff"
    }
  }
});
~~~

个人中心栈导航
~~~
export const MeStack = StackNavigator({
  Me: {
    screen: MeScreen,
    navigationOptions: {
      title: "Me",
      headerStyle: {
        backgroundColor: "#ff4e20"
      },
      headerTintColor: "#fff"
    }
  },
  Setting: {
    screen: SettingScreen,
    navigationOptions: {
      title: "Setting",
      headerStyle: {
        backgroundColor: "#ff4e20"
      },
      headerTintColor: "#fff"
    }
  }
});
~~~

底部Tab导航
~~~
export const Tabs = TabNavigator(
  {
    Notes: {
      screen: NoteStack
    },
    New: {
      screen: NewNoteStack
    },
    Me: {
      screen: MeStack
    }
  }
);
~~~

Root栈导航
~~~
export const RootStack = StackNavigator(
  {
    Tabs: {
      screen: Tabs
    }
  },
  {
    mode: "modal",
    headerMode: "none",
    initialRouteName: "Tabs"
  }
);
~~~

### React Native基础组件
- View
- Text
- TextInput
- Alert
- FlatList
- TouchableOpacity
- ActivityIndicator
- StyleSheet

### 第三方库：
- [react-navigation](https://reactnavigation.org/)
- [react-native-elements](https://react-native-training.github.io/react-native-elements/)
- [react-native-vector-icons](https://github.com/oblador/react-native-vector-icons)

