## 自用的OPQBot的python封装

#### 一个简单的脚手架，用来提供更好的插件支持，使用异步socketio实现

#### 只是在已完成的大厦上刷了层漆而已

## 使用方法

### 1 安装依赖 pip3 install -r requirement
### 2 把config.py改成自己的
### 3 python3 run.py
### 4 在qq里输入/echo看看有没有回应

## 插件开发

#### 在plugins下的所有py文件都会自动注册为插件，使用on_command修饰器指定命令入口，
#### 示例:@on_command("ECHO"),参数为触发命令 限定大写（输入命令的时候不区分大小写）
#### 特殊的 @on_command("else")修饰器用来处理例外信息
#### 函数一个入参message
    '''
    message.isGroup 是否来自群聊
    message.FromQQ 消息来源
    message.QQGName 来源QQ群昵称
    message.FromQQG 来源QQ群
    message.FromNickName 来源QQ昵称
    message.Content 消息内容
    message.ToQQ 自己的QQ
    '''

#### 发送接口还没加完 就实现了发送文字图片声音，群管啥的有时间再说，都在message.py里，简单看下OPQBot的发送格式就知道怎么用和加接口了（因为暂时不用就懒得加了）

#### 将要完成的工作：完善修饰器功能，区分群聊私聊，识别at，接口补全

#### 2020.8.15全部换成异步了，性能提升（也许）

#### 自用  佛系更新，不服自己写好了merge过来

## 存在的问题

### ~~win下socketio没法正常退出，只能强关控制台，Linux还好~~ 已解决
