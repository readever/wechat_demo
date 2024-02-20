import streamsync as ss


ss.md("### 平均间距")

def onchange1(state, value):
    #cols_ex1.design = True
    cols_ex1_id = cols1[0].id #通过cols_ex1不能直接得到

    if value == True:
        ss.getcm().components[cols_ex1_id]["content"]["options"]["design"] = True
        ss.session.state["cols1_design"] = ', design = True'
    else:
        ss.getcm().components[cols_ex1_id]["content"]["options"]["design"] = False
        ss.session.state["cols1_design"] = ''

        
cols_ex1 = ss.columns([90,"flex:10; border-left:1px solid lightgray"], design=False, style="border:1px solid lightgray")
        
with cols_ex1[0]:
    cols1 = ss.columns(2)

    with cols1[0]:
        ss.text("First of two columns")
        
    with cols1[1]:
        ss.text("Second of two columns")


with cols_ex1[1]:
    ss.checkbox("设计", onchange = onchange1)

ss.md('''
```python
import simplestart as ss

    cols1 = ss.columns(3@cols1_design)

    with cols1[0]:
        ss.text("First of three columns")
    with cols1[1]:
        ss.text("Second of three columns")
    with cols1[2]:
        ss.text("Third of three columns")
```
''')
    
ss.space()


ss.md("### 按比例间距")

def onchange2(state, value):
    #cols_ex1.design = True
    cols_ex2_id = cols2[0].id #通过cols_ex1不能直接得到

    if value == True:
        ss.getcm().components[cols_ex2_id]["content"]["options"]["design"] = True
        ss.session.state["cols2_design"] = ', design = True'
    else:
        ss.getcm().components[cols_ex2_id]["content"]["options"]["design"] = False
        ss.session.state["cols2_design"] = ''
        
cols_ex2 = ss.columns([90,"flex:10; border-left:1px solid lightgray"], design=False, style="border:1px solid lightgray")
    
with cols_ex2[0]:
    cols2 = ss.columns([4,6])

    with cols2[0]:
        ss.text("First of two columns")
    with cols2[1]:
        ss.text("Second of two columns")


with cols_ex2[1]:
    ss.checkbox("设计", onchange = onchange2)
        
ss.md('''
```python
import simplestart as ss

    cols1 = ss.columns([1, 1, 2]@cols2_design)

    with cols1[0]:
        ss.text("First of three columns")
    with cols1[1]:
        ss.text("Second of three columns")
    with cols1[2]:
        ss.text("Third of three columns")
```
''')

def onPageLoad():
    ss.session.state["cols1_design"] = ''
    ss.session.state["cols2_design"] = ''