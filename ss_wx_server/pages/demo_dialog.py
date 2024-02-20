import simplestart as ss

ss.md("## ss.dialog 对话框")

ss.space("mt-8")
ss.md('''
dialog 对话框

#### 函数
ss.dialog(title, width = None, onclose = None)
      
##### 函数说明

| 参数 | 说明 |
| --- | --- | 
| title | 对话框的标题 |
| width | 指定对话框的宽度，默认为屏幕尺寸的 30% |
| onclose | 对话框关闭的事件处理 |

##### 成员函数
show(fullscreen = False)
      
''')

ss.space("mt-8")
ss.md('''
---
#### 示例
''')


def testme():
    ss.message("testme")
    
def showit():
    if ss.session.state["str_fullscreen"] != "":
        dialog.show(fullscreen = True)
    else:
        dialog.show()
    
def myclose(state, value):
    ss.message("dialog close with result " + value)
    
dialog = ss.dialog(title="对话框标题", onclose=myclose)
with dialog:
    ss.text("SimpleStart dialog demostration")
    ss.md("---")
    ss.button("testme", onclick=testme)
    ss.md(":smile:")
        
cols = ss.columns([60,"flex:40; border-left:1px solid lightgray"], design=False, style="border:1px solid lightgray")
with cols[0]:
    mytext = ss.text("This is dialog")
    ss.button("show dialog", onclick=showit)
    
def mycheck(state, value):
    if value != None:
        ss.session.state["str_fullscreen"] = "fullscreen = True"
        #dialog.show(fullscreen = True)
    else:
        ss.session.state["str_fullscreen"] = ""

with cols[1]:
    ss.text("对话框选项")
    ss.checkbox("全屏", onchange=mycheck)

ss.space("mt-8")

ss.write("#### 代码")

ss.md('''
```python
import simplestart as ss

def myclose(state, value):
    ss.message("dialog close with result " + value)
    
dialog = ss.dialog(title="对话框标题", onclose=myclose)
with dialog:
    ss.text("Opening from the bottom")
    ss.md("---")
    ss.button("testme", onclick=testme)
    ss.md(":smile:")
    
def showit():
    dialog.show(@str_fullscreen)
    
ss.button("show dialog", onclick=showit)
```
''')

def onPageLoad():
    ss.session.state["str_fullscreen"] = ""