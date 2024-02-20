import simplestart as ss
import pandas as pd

ss.md("## ss.table 表格数据")

ss.md('''
以表格方式显示数据

##### ss.table()

| 参数 | 说明 |
| --- | --- | 
| data | 要显示的数据，pandas DataFrame形式 |
| show_border | 是否显示纵向边框, 默认为 false |
| sortable | 是否提供排序功能, 默认为 false |
| selectable| 行是否可选择, 默认为 false |
| handlers | 一些处理事件，包括行改变、选择改变, 参见示例 |
      
''')

ss.space("mt-8")

ss.md('''
---
#### 示例
''')

def onchange_border(state, value):
    if value == True:
        ss.getcm().components[mytable.id]["content"]["show_border"] = True
        ss.session.state["show_border"] = ', border = True'
    else:
        ss.getcm().components[mytable.id]["content"]["show_border"] = False
        ss.session.state["show_border"] = ''

def onchange_sortable(state, value):
    if value == True:
        ss.getcm().components[mytable.id]["content"]["sortable"] = True
        ss.session.state["sortable"] = ', sortable = True'
    else:
        ss.getcm().components[mytable.id]["content"]["sortable"] = False
        ss.session.state["sortable"] = ''
        
def onchange_selectable(state, value):
    if value == True:
        ss.getcm().components[mytable.id]["content"]["selectable"] = True
        ss.session.state["selectable"] = ', selectable = True'
    else:
        ss.getcm().components[mytable.id]["content"]["selectable"] = False
        ss.session.state["selectable"] = ''  
        
def current_change(state, value):
    ss.session.state["row_selected"] = value["index"]
    
def selection_change(state, value):
    ss.session.state["selection_change"] = value["selected"]
        
# 创建一个包含三列的数据集
data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'city': ['New York', 'San Francisco', 'Los Angeles']}
df = pd.DataFrame(data)
    
cols = ss.columns([70,"flex:30; border-left:1px solid lightgray"], design=False, style="border:1px solid lightgray")
with cols[0]:
    mytable = ss.table(df, handlers={"current-change":current_change, "selection-change":selection_change})
    ss.md("#### Events")
    ss.write("Row selected: @row_selected")
    ss.write("Selection changed: @selection_change")

with cols[1]:
    ss.text("setting")    
    ss.checkbox("边框", onchange = onchange_border) 
    ss.space()
    ss.checkbox("排序", onchange = onchange_sortable)
    ss.space()
    ss.checkbox("可选择", onchange = onchange_selectable)

    
ss.space("mt-8")

ss.write('''
---
#### 代码
''')

ss.md('''
```python
import simplestart as ss

def current_change(state, value):
    ss.session.state["row_selected"] = value["index"]
    
def selection_change(state, value):
    ss.session.state["selection_change"] = value["selected"]

data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'city': ['New York', 'San Francisco', 'Los Angeles']}
df = pd.DataFrame(data)

ss.table(df@show_border@sortable@selectable, handlers={\"current-change\":current_change, \"selection-change\":selection_change})
ss.md(\"#### Events\")
ss.write(\"Row selected: \@row_selected\")
ss.write(\"Selection changed: \@selection_change\")
    
def onPageLoad():
    ss.session.state["row_selected"] = ''
    ss.session.state["selection_change"] = ''
    
```
''')


ss.md('''
---
#### 示例 - 自定义列
''')

vuestr = '''
<template>
    <el-tag>{{item.row.city}}</el-tag>
</template>

<script>

module.exports = {
    props:["item"],

    methods: {
        //todo
    },
}
</script>
'''
    
mytable_ex = ss.table(df, custom_columns = ["city"], custom_columns_template = vuestr)
#mytable_ex = ss.table(df, custom_columns = ["city"], custom_columns_vue="components/mycell.vue")

ss.space("mt-8")

ss.write('''
---
#### 代码
''')

ss.md('''
```python
import simplestart as ss

data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'city': ['New York', 'San Francisco', 'Los Angeles']}
df = pd.DataFrame(data@show_border@sortable@selectable)

vuestr = \'''
<template>
    <el-tag>{{item.row.city}}</el-tag>
</template>

<script>
module.exports = {
    props:[\"item\"],

    methods: {
        //todo
    },
}
</script>
\'''

ss.table(df, custom_columns = ["city"], custom_columns_template = vuestr)
```
''')


ss.md('''
::: tip
  可以在vue中定义的方法和属性，已经和python端交互数据。参考帮助中的自定义组件中的方法。
:::
''')



def onPageLoad():
    ss.session.state["show_border"] = ''
    ss.session.state["selectable"] = ''
    ss.session.state["sortable"] = ''
    ss.session.state["row_selected"] = ''
    ss.session.state["selection_change"] = ''