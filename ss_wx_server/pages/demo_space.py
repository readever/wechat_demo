import simplestart as ss

ss.md("### ss.space")
ss.space()

ss.text("text1")
ss.text("text2")
ss.space("mt-4 mt-b")
ss.text("text3")

ss.space("mt-4 mb-4")
with ss.section(style="display:flex; border:1px solid lightgray; padding:10px;width:200px"):
    ss.text("text4")
    ss.text("text5")
    
ss.space("mt-4 mb-4")
with ss.section(style="display:flex; border:1px solid lightgray; padding:10px;width:200px"):
    ss.text("text6")
    ss.space("ml-4")
    ss.text("text7")
    
    
ss.space()

ss.write("代码")

ss.md('''
```python
import simplestart as ss

ss.text("text1")
ss.text("text2")
ss.space("mt-4 mt-b")
ss.text("text3")

ss.space("mt-4 mb-4")
with ss.section(style="display:flex; border:1px solid lightgray; padding:10px;width:200px"):
    ss.text("text4")
    ss.text("text5")
    
ss.space("mt-4 mb-4")
with ss.section(style="display:flex; border:1px solid lightgray; padding:10px;width:200px"):
    ss.text("text6")
    ss.space("ml-4")
    ss.text("text7")
''')