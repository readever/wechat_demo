import simplestart as ss

ss.md("## ss.slider 滑块")

ss.space("mt-8")
ss.md('''
slider 滑块

#### 函数
ss.slider(value, min = 0, max = 100, onchange = None)
      
##### 函数说明

| 参数 | 说明 |
| --- | --- | 
| value | 滑块的当前值 |
| min | 滑块的最小值 |
| max | 滑块的最大值 |
| onchange | 拉动滑块改变事件 |
      
''')

ss.space("mt-8")
ss.md('''
---
#### 示例
''')

ss.md("### Please drag the slider to change the value")

info = ss.text("number")

def onchange(state, value):
    info.text = value

ss.slider(500, 0, 1000, onchange = onchange, style="width:50%")

ss.space()

ss.write("代码")

ss.md('''
```python
import simplestart as ss

info = ss.text("number")

def onchange(state, value):
    info.text = value

ss.slider(500, 0, 1000, onchange = onchange)
''')