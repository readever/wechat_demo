import simplestart as ss

ss.md("## ss.selectbox 多选框")

ss.space("mt-8")
ss.md('''
以下拉菜单方式选择选项

#### 函数
ss.checkbox(label, checked = False, onchange = None)
      
##### 函数说明

| 参数 | 说明 |
| --- | --- | 
| options | 可选项，数组形式 |
| value | 默认选择项 |
| returnValue | "text" 或 "index", 返回值，默认是文本|
| onchange | 选项改变事件 |
      
''')

ss.space("mt-8")
ss.md('''
---
#### 示例
''')

options = ["option1","option2", "option3"]

def selchange(state, value):
    info.text = "the selection is: " + str(value)

def onradiochange(state, value):
    ss.session.state["returnValueStr"] = f'returnValue = "{value}", '
    if value == "index":
        ss.show(sb2)
        ss.hide(sb1)
    else:
        ss.show(sb1)
        ss.hide(sb2)

    
cols = ss.columns([60,"flex:40; border-left:1px solid lightgray"], design=False, style="border:1px solid lightgray")

with cols[0]:
    info = ss.text("no selection")
    sb1 = ss.selectbox(options, value="", onchange = selchange)
    sb2 = ss.selectbox(options, value="", returnValue="index", onchange = selchange, style="display:none")
    ss.md("Defalut return value is text, but you can also set it in index")

with cols[1]:
    ss.text("returnValue")
    ss.radio(["text", "index"], value="text", onchange=onradiochange)


ss.space("mt-8")

ss.write("#### 代码")

ss.md("""
```python
import simplestart as ss

options = ["option1","option2", "option3"]


info = ss.text("no selection")

def selchange(state, value):
    info.text = "the selection is: " + str(value)

ss.selectbox(options, value="", @returnValueStr onchange = selchange)

```
""")



def onPageLoad():
    ss.session.state["returnValueStr"] = ""