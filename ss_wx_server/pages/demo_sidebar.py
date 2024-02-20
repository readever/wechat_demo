import simplestart as ss

ss.md("## ss.sidebar 侧边栏")

ss.space("mt-8")
ss.md('''
在屏幕左侧的侧边栏内显示各种组件，例如可以放置数据控制和一些设置。只能在桌面端使用，移动应用和微信小程序内不可用。

#### 函数
ss.sidebar()
      
''')

ss.md('''
::: tip
  sidebar = ss.sidebar()
  with sidebar:
      ss.text("hello, world") #这将显示在侧边栏内
:::
''')

sidebar = ss.sidebar()

with sidebar:
    ss.button("click")
    section = ss.section()
        

def testme(state, value):
    with sidebar:
        ss.text("text in sidebar")

def clear(state, value):
    section.text(111)
    
ss.button("Demo", onclick = testme)
ss.button("Clear", onclick = clear)


ss.space()

ss.write("代码")

ss.md('''
```python
import simplestart as ss

sidebar = ss.sidebar()

with sidebar:
    ss.button("click")
    section = ss.section()
        

def testme(state, value):
    with sidebar:
        ss.text("text in sidebar")

def clear(state, value):
    section.text(111)
    
ss.button("Demo", onclick = testme)
ss.button("Clear", onclick = clear)

```
''')