import simplestart as ss

ss.md('''
## 运行
simeplestart 安装完成后，就可以使用了


### 1. 创建单页应用并运行

在你的文件夹里创建一个文件 app.py

内容如下

```python
import simplestart as ss

ss.write("Hello, World!")
```

然后执行命令

```
ss app.py
```

也可指定端口

```
ss app.py --port 8000
```


''')



ss.md('''
### 2. 创建多页应用并运行

在你的文件夹里创建一个文件 app.py。

内容如下

```python
import simplestart as ss

ss.write("Hello, World!")

def openpage():
    ss.openpage("second")
    
ss.button("open page", onclick=openpage)

```

然后创建一个子目录 pages, 在里面创建一个python程序，
second.py, 里面的内容自己定义，例如

```python
import simplestart as ss

ss.write("I am second page")

```

然后执行命令，运行程序

```
ss app.py
```

''')

