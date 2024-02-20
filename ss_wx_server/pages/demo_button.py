import streamsync as ss


ss.md("## ss.button 按钮")

ss.space("mt-8")
ss.md('''
在页面上显示一个button组件

#### 函数
ss.button(label, type = None, onclick = None)
      
##### 函数说明

| 参数 | 说明 |
| --- | --- | 
| label | button的标题 |
| type | button的类型，可选值有 default, outlined, flat, text, plain |
| onclick | 点击按钮时的回调函数 |
      
''')



ss.space("mt-8")
ss.md('''
---
#### 示例
''')

#自定义函数
def myclick():
    mytext.text = "You clicked "
    
def reset():
    mytext.text = "This is button"
    but1.type = ""
    ss.getcm().components[but1.id]["content"]["options"]["icon"] = ""
    ss.getcm().components[but1.id]["content"]["options"]["endicon"] = ""
    ss.getcm().components[but1.id]["content"]["options"]["icon_color"] = "mediumseagreen"
    ss.getcm().components[but1.id]["content"]["options"]["style"] = "background-color:initial;color:initial"
    ss.session.state["iconstr"] = ''
    ss.session.state["style_str"] = ''
    ss.session.state["style"] = ''

    
#基本用法
cols = ss.columns([60,"flex:40; border-left:1px solid lightgray"], design=False, style="border:1px solid lightgray")
with cols[0]:
    mytext = ss.text("This is button")
    ss.space()
    but1 = ss.button("Click it", iconstr="search", onclick=myclick)

def onradiochange(state, value):
    if value == "default":
        but1.type = ""
        ss.session.state["buttonstyle"] = ""
    elif value == "outlined":
        but1.type = "outlined"
        ss.session.state["buttonstyle"] = '"outlined\",'
    elif value == "flat":
        but1.type = "tonal"
        ss.session.state["buttonstyle"] = '"flat\",'
    elif value == "text":
        but1.type = "text"
        ss.session.state["buttonstyle"] = '"text\",'
    elif value == "plain":
        but1.type = "plain"
        ss.session.state["buttonstyle"] = '"plain\",'

def oncheckbox_change(state, value):
    if value == True:
        ss.getcm().components[but1.id]["content"]["options"]["icon"] = "aim"
        ss.session.state["iconstr"] = ' icon="search",'
    else:
        ss.getcm().components[but1.id]["content"]["options"]["icon"] = ""
        ss.session.state["iconstr"] = ''

def onradiochange2(state, value):
    if value == 1:
        ss.getcm().components[but1.id]["content"]["options"]["icon"] = "aim"
        ss.getcm().components[but1.id]["content"]["options"]["endicon"] = ""
        ss.session.state["iconstr"] = ' icon="aim",'
    elif value == 2:
        ss.getcm().components[but1.id]["content"]["options"]["icon"] = ""
        ss.getcm().components[but1.id]["content"]["options"]["endicon"] = "search"
        ss.session.state["iconstr"] = ' endicon="search",'
    else:
        ss.getcm().components[but1.id]["content"]["options"]["icon"] = ""
        ss.getcm().components[but1.id]["content"]["options"]["endicon"] = ""
        ss.session.state["iconstr"] = ''
    
def changeColor(bkcolor):
    ss.getcm().components[but1.id]["content"]["options"]["style"] = f"background-color:{bkcolor}; color:white"
    ss.getcm().components[but1.id]["content"]["options"]["icon_color"] = "white"
    ss.session.state["style_str"] = 'style="background-color:#409eff, color:white"'
    ss.session.state["style"] = 'style=style,'

    
with cols[1]:
    ss.text("测试radio")
    
    ss.radio(["default", "outlined", "flat", "text", "plain"], "Default", buttonstyle = True, onchange=onradiochange)
    ss.space()
    ss.radio([(1, "图标(前)"), (2, "图标(后)"), (3, "图标按钮")], onchange=onradiochange2)
    
    ss.space()
    ss.button("", "flat", style="background-color:#409eff", onclick=[changeColor, "#409eff"])
    ss.button("", "flat", style="background-color:#67c23a", onclick=[changeColor, "#67c23a"])
    ss.button("", "flat", style="background-color:#e6a23c", onclick=[changeColor, "#e6a23c"])
    ss.button("", "flat", style="background-color:#f56c6c", onclick=[changeColor, "#e6a23c"])
    ss.button("", "flat", style="background-color:#909399", onclick=[changeColor, "#909399"])
    
    
    ss.space()
    ss.button("重置", onclick=reset)


ss.space("mt-8")

ss.write("#### 代码")

ss.md('''
```python
import simplestart as ss

def clickme():
    mytext.text = "You clicked"
    
mytext = ss.text("This is button")
@style_str
ss.button("Click it", @buttonstyle@iconstr@style onclick=clickme)
```
''')

ss.md('''
::: tip
  可以通过style改变button的部分css属性， 例如 mybutton = ss.button("button", style="color:red")
:::
''')


def onPageLoad():
    ss.session.state["xxx"] = 111
    ss.session.state["buttonstyle"] = ""