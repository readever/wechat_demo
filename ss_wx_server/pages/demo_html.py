import streamsync as ss


ss.md("## ss.html 超文本")

ss.space("mt-8")
ss.md('''
在页面上显示 html 超文本内容

#### 函数
ss.html(body)
      
##### 函数说明

| 参数 | 说明 |
| --- | --- | 
| body | html格式的超文本内容 |
      
''')


ss.space("mt-8")

ss.md('''
---
#### 示例
''')


ss.md("### html")

ss.html(f"""
    <p>This is a piece of rich text content, which contains <strong>bold</strong> and <em>italic</em> text.</p>
    <style>
    .testclass{{
        color:red;
        font-weight:bold;
    }}
    </style>
    <div class="testclass">this is red</div>
""")

ss.space("mt-8")

ss.write('''
---
#### 代码
''')

ss.md('''
```python
import simplestart as ss

ss.html(f"""
    <p>This is a piece of rich text content, which contains <strong>bold</strong> and <em>italic</em> text.</p>
    <style>
    .testclass{{
        color:red;
        font-weight:bold;
    }}
    </style>
    <div class="testclass">this is red</div>
""")
```
''')