import streamsync as ss

ss.md("## ss.expander 下拉展开")

ss.space("mt-8")
ss.md('''
下拉展开更多内容

#### 函数
ss.expander(label, expanded = False)
      
##### 函数说明

| 参数 | 说明 |
| --- | --- | 
| label | expander的标题 |
| expanded | 初始展开状态，默认未展开 |
      
''')

ss.space("mt-8")
ss.md('''
---
#### 示例
''')

with ss.expander("关于SimpleStart"):
    ss.text("Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! \
    Eaque cupiditate minima, at placeat totam, magni doloremque veniam neque porro libero rerum unde voluptatem!", style="padding:10px")


ss.space("mt-8")

ss.write("#### 代码")

ss.md('''
```python
import simplestart as ss

with ss.expander("关于SimpleStart"):
    ss.text("Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima, at placeat totam, magni doloremque veniam neque porro libero rerum unde voluptatem!")
```
''')