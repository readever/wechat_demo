import simplestart as ss

ss.md("### ss.style")
ss.space()

ss.heading("Using ss.style to change the style of element")

ss.html('''
    <div class="test1">this is a div</div>
    <span class="test2">this is a text</span>
''')

ss.style('''
    .test1{
        dislplay:inline-block !important;
        background-color:lightgray;
        padding:5px;
        width:100px;
    }
    .test2{
        color:red;
    }
''')

ss.space()

ss.write("代码")



ss.md('''
```python
import simplestart as ss

ss.html(\'''
    <div class="test1">this is a div</div>
    <span class="test2">this is a text</span>
\''')

ss.style(\'''
    .test1{
        dislplay:inline-block !important;
        background-color:lightgray;
        padding:5px;
        width:100px;
    }
    .test2{
        color:red;
    }
\''')
''')
