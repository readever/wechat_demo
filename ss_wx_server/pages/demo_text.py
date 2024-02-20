import streamsync as ss

ss.md("## ss.text 文本")

ss.space("mt-8")
ss.md('''
在页面上显示文本组件

#### 函数
ss.text (text, inline = False, style = None)
      
##### 函数说明

| 参数 | 说明 |
| --- | --- | 
| text | 要显示的文本内容 |
| inline | inline属性 |
| style | 文本组件的 css 属性，例如颜色和背景色等 |
      
''')

ss.space("mt-8")
ss.md("#### 示例")

ss.md("---")

#基本用法
ss.text("This is a text", inline=True)

#改变值
test = ss.text("hello, world")
test.text = "你好!"

#添加前缀图标, icon的值可参考element plus
ss.text("Search...", icon="search")

#改变颜色
ss.text("This is a red string", style="color:red")

#设置css
style = '''
    background-color:#02a982;
    color:white;
    padding:3px 5px;
    border-radius:3px;
    display:inline-block;
'''
ss.text("Please input somthing...", style=style)

ss.text("搜索中...", cursor = True)


ss.space("mt-8")

ss.write("#### 代码")

ss.md('''
```python
import simplestart as ss

test = ss.text(\"hello, world\")
test.text = "你好!"

#添加前缀图标, icon的值可参考element plus
ss.text("Search...", icon="search")

#改变颜色
ss.text(\"This is a red string\", style=\"color:red\")

#设置css
style = \'''
    background-color:#02a982;
    color:white;
    padding:3px 5px;
    border-radius:3px;
    display:inline-block;
\'''
ss.text(\"Please input somthing...\", style=style)

ss.text(\"搜索中...\", cursor = True)

```
''')

