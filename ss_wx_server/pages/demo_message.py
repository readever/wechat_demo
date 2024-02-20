import simplestart as ss

ss.md("## ss.message 弹出消息")

ss.space("mt-8")
ss.md('''
在屏幕上方弹出消息提示

#### 函数
ss.message(text)
      
##### 函数说明

| 参数 | 说明 |
| --- | --- | 
| text | 弹出的消息字符串内容 |
      
''')

ss.space("mt-8")
ss.md('''
---
#### 示例
''')


def showmsg():
    ss.message("Hello, world")

showmsg()
ss.button("message", onclick=showmsg)


ss.space("mt-8")

ss.write('''
---
#### 代码
''')

ss.md('''
```python
import simplestart as ss

def showmsg():
    ss.message("Hello, the world")

```
''')