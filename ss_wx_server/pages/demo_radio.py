import simplestart as ss

ss.md("## ss.radio 单选框")

ss.space("mt-8")
ss.md('''
在备选项中进行单选

#### 函数
ss.radio(options, inline = True, button_style = False, onchange = None)
      
##### 函数说明

| 参数 | 说明 |
| --- | --- | 
| options | 可选项，数组形式 |
| inline | 默认True, 水平显示选项. 设为 False时，垂直显示选项 |
| button_style | 是否显示成按钮组形式，只在inline时有效 |
| returnValue | "text" 或 "index", 返回值，默认是文本|
| onchange | 选项改变事件 |
      
''')

def onchange(state, value):
    state["options_value"] = value

options = ["aaa", "bbb", "ccc"]

ss.space("mt-8")
ss.md('''
---
#### 示例
''')

ss.md("#### inline")
ss.radio(options, onchange = onchange)

ss.space()
ss.md("#### non inline and return index")
ss.radio(options, button_style = True, returnValue = "index", onchange = onchange)

ss.space()
ss.md("#### vertical")

ss.radio(options, inline = False, onchange = onchange)

ss.md("onchange: @options_value")

ss.space("mt-8")

ss.write("#### 代码")

ss.md('''
```python
import simplestart as ss

def onchange(state, value):
    state["options_value"] = value
    
options = ["aaa", "bbb", "ccc"]
ss.radio(options, onchange = onchange)

ss.space()
ss.radio(options, button_style = True, returnValue = "index", onchange = onchange)

ss.space()
ss.radio(options, inline = False, onchange = onchange)

ss.md("onchange: \@options_value")

def onPageLoad():
    ss.session.state["options_value"] = ""

''')


def onPageLoad():
    ss.session.state["options_value"] = ""