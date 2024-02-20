import simplestart as ss

ss.md("## ss.checkbox 多选框")
ss.md("有一个bug, 放在main.py里面，check会出错, 尤其是放在sidebar里")

ss.space("mt-8")
ss.md('''
在备选项中进行多选

#### 函数
ss.checkbox(label, checked = False, onchange = None)
      
##### 函数说明

| 参数 | 说明 |
| --- | --- | 
| label | checkbox的标题 |
| checked | 初始选中状态，默认未选中 |
| onchange | 选项改变事件 |
      
''')

def onchange(state, value):
    state["checked_value"] = value

ss.space("mt-8")
ss.md('''
---
#### 示例
''')

ss.checkbox("checkme", onchange = onchange)

ss.checkbox("initially unchecked", checked = True, onchange = onchange)


ss.md("onchange: @checked_value")

ss.space("mt-8")

ss.write('''
---
#### 代码
''')

ss.md('''
```python
import simplestart as ss

def onchange(state, value):
    state["checked_value"] = value
    
ss.checkbox("checkme", onchange = onchange)
ss.checkbox("initially unchecked", checked = True, onchange = onchange)

ss.md("onchange: \@checked_value")

def onPageLoad():
    ss.session.state["checked_value"] = ""

''')


def onPageLoad():
    ss.session.state["checked_value"] = ""