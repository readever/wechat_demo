#这个例子不做演示
import simplestart as ss

ss.md("## onPageEnter 页面加载事件")

ss.space("mt-8")
ss.md('''
页面每次进入的时候事件

#### 函数
onPageEnter()
 
''')

ss.md("每次进入这个页面的时候，会看到一条弹出消息")

def onPageEnter():
    ss.message("page enter event")


ss.space("mt-8")

ss.write('''
---
#### 代码
''')

ss.md('''
```python
import simplestart as ss

def onPageEnter():
    ss.message("enter")

```
''')