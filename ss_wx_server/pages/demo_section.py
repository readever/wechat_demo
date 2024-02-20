import simplestart as ss

ss.md("## ss.section 容器")

ss.space("mt-8")
ss.md('''
section 父容器， 可以装载其它组件

#### 函数
ss.section(title, style=None)
      
##### 函数说明

| 参数 | 说明 |
| --- | --- | 
| title | section的标题 |
| style | 容器的css样式，比如可以设置边框 |

##### 成员函数
empty()
      
''')

ss.space("mt-8")
ss.md('''
---
#### 示例
''')

#const
style = '''
    border:1px solid lightgray;
    padding:10px;
    display:inline-block;
'''

#api
def clear():
    section.empty()
    
def write_something():
    section.text("Hello, I am inside section 2")

#ui
with ss.section(style=style):
    ss.text("This is inside the section 1")
    

ss.space("mt-4 mb-4")    

section = ss.section(style=style)
section.text("This is inside the section 2")

ss.space("mt-4 mb-4")   
ss.text("outside the section")


ss.md("---")

ss.button("clear", onclick=clear)

ss.button("add something", onclick=write_something)

ss.space("mt-8")

ss.write("#### 代码")

ss.md("""
```python
import simplestart as ss

style = '''
    border:1px solid lightgray;
    padding:10px;
    display:inline-block;
'''

with ss.section(style=style):
    ss.text("This is inside the section 1")


#api
def clear():
    section.empty()
    
def write_something():
    section.text("Hello, I am inside section 2")

section = ss.section(style=style)
section.text("This is inside the section 2")

ss.button("clear", onclick=clear)

ss.button("add something", onclick=write_something)

```
""")

ss.md('''
::: tip
  除了可以通过 with 语法添加组件，也可以直接通过section.text(), section.button()等方式添加容器内的组件
:::
''')