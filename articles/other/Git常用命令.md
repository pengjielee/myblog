#### 生成密钥
~~~
$ ssh-keygen -t rsa -C "pengjielee"
~~~

#### 配置用户名和邮箱
~~~
//--global表示你这台机器上的所有git仓库都会使用这个配置
$ git config --global user.name "your name" 
$ git config --global user.email "email@example.com"
~~~

#### 仓库操作
~~~
// 初始化
$ git init

// 克隆库
$ git clone git@github.com:pengjielee/git-learn.git

// 关联远程库
$ git remote add origin git@github.com:pengjielee/git-learn.git

// 添加提交库
$ git add .
$ git commit -m 'update'

// 推送库
$ git push origin master

// 查看文件状态
$ git stauts

// 查看文件修改
$ git diff
~~~

#### 版本回退
~~~
//回退上一个版本
$ git reset --hard HEAD^ 

//回退上上一个版本
$ git reset --hard HEAD^^

//回退上100个版本
$ git reset --hard HEAD~100

//回退到指定版本
$ git reset --hard commit_id

//查看提交详细历史记录
$ git log 

//查看提交摘要历史记录
$ git log --pretty=oneline

//查看git命令历史记录
$ git relog
~~~

#### 暂存区和工作区
~~~
// 把文件修改从工作区添加到暂存区
$ git add

// 把暂存区的所有内容提交到当前分支
$ git commit

// 撤销工作区的修改:
// a.修改后未放到暂存区，现在，撤销修改就回到和版本库一模一样的状态；
// b.添加到暂存区后又作了修改，现在，撤销修改就回到添加到暂存区后的状态；
// 总之就是回到最近一次git commit或git add时的状态。
$ git checkout -- readme.txt

// 撤销暂存区的修改（把暂存区的修改撤销掉（unstage），重新放回工作区)
$ git reset HEAD readme.txt


- 场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令git checkout -- file。
- 场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令git reset HEAD file，就回到了场景1，第二步按场景1操作。
- 场景3：已经提交了不合适的修改到版本库时，想要撤销本次提交，参考版本回退一节，不过前提是没有推送到远程库。
~~~

#### 标签操作
~~~
默认标签是打在最新提交的commit上的

// 创建标签
$ git tag v1.0

// 查看标签
$ git tag

// commit上创建标签
$ git tag v1.0 commit_id

// 查看标签信息
$ git show v1.0

// 创建标签信息
$ git tag -a v1.0 -m 'version 1.0' commit_id
~~~

#### 分支操作
~~~
// 创建分支
$ git branch dev

// 切换分支 
$ git checkout dev

// 创建并切换分支
$ git checkout -b dev

// 查看分支（列出所有分支，当前分支前面会标一个*号）
$ git branch

// 合并分支，快速模式（Fast forward），删除分支后，会丢掉分支信息。
$ git merge dev

// 合并分支，普通模式，合并后的历史有分支，能看出来曾经做过合并，而fast forward合并就看不出来曾经做过合并。
$ git merge --no-ff -m "merge with no-ff" dev //注意--no-ff参数，表示禁用Fast forward。

// 删除分支
$ git branch -d dev

// 删除远程分支
$ git push origin:dev

// 查看分支合并详细信息
$ git log --graph

// 查看分支合并摘要信息
$ git log --graph --pretty=oneline --abbrev-commit 
~~~