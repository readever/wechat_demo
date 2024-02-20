import simplestart as ss

ss.md("## ss.session session变量")

ss.space("mt-8")
ss.md('''
session变量，支持页面间数据传递

#### 使用方法
ss.session['变量名'] = ’变量值‘
        
''')

#in this page
ss.session["count"] = 100

#in another page
count = ss.session["count"]
ss.write("count:", count)
    
ss.space("mt-8")

ss.write('''
---
#### 代码
''')

ss.md('''
```python
import simplestart as ss

#in this page
ss.session["count"] = 100

#in another page
count = ss.session["count"]
ss.write("count:", count)

```
''')