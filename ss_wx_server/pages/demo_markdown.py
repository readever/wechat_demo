import simplestart as ss

ss.md("## ss.markdown md文本")

ss.space("mt-8")
ss.md('''
在页面上显示 html 超文本内容

#### 函数
ss.markdown(body)
ss.md(body)
      
##### 函数说明

| 参数 | 说明 |
| --- | --- | 
| body | markdown格式的超文本内容 |
      
''')

ss.space("mt-8")

ss.md('''
---
#### 示例
''')

ss.markdown("# 一级标题")
ss.markdown("## 二级标题")
ss.markdown("### 三级标题")

#水平分割线
ss.markdown("---")

ss.markdown('''
- list item1
- list item2
- list item3
''')



ss.space("mt-8")

ss.write('''
---
#### 代码
''')

ss.md('''
```python
import simplestart as ss

ss.markdown("# 一级标题")
ss.markdown("## 二级标题")
ss.markdown("### 三级标题")

#水平分割线
ss.markdown("---")

ss.markdown(\'''
- list item1
- list item2
- list item3
\''')

```
''')