# wechat_demo

### 说明
本演展示了如何使用 Python 完成微信小程序的应用逻辑。
前端是利用uniapp和webview实现的，应用逻辑是在后台用 python 和 simplestart 框架完成的。
simplestart框架是一个利用python实现网页和数据可视化的工具。

### 客户端
微信小程序用uniapp完成，在目录 ss_wx_demo目录中。里面用到了webview访问服务端，真正的应用逻辑是在服务端完成的。

### 服务端
目录 ss_wx_server是微信小程序的逻辑代码实现，是用python写的。
需要安装 SimpleStart, pip3 install simplestart
然后执行 ss /yourpath/main.py --port 8000

客户端webview访问的地址是
http://yourhost:8000/pages/menulist


### 扫码体验

![image](wx_2dcode.jpeg)
