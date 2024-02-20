import streamsync as ss
import pandas as pd

ss.md("## ss.write 输出")

ss.md('''
ss.write 类似于print，可以输出文本，列表和其它类型，方便测试和输出

### ss.write(str|list|db data)
      
''')

ss.space("mt-8")

ss.md('''
---
#### 示例
''')

ss.md("#### 1. 输出文本")
ss.write("This is a text")

ss.md('''
```python
ss.write("This is a text")
```
''')

ss.md("#### 2. 输出多个变量")
a = "aaa"
b = "bbb"
ss.write(a, ",", b)

ss.md('''
```python
a = "aaa"
b = "bbb"
ss.write(a, ",", b)
```
''')

ss.md("#### 3. 输出列表")
data = ["aaa", "bbb", "ccc"]
ss.write(data)

data = {"aaa":1, "bbb":2, "ccc":3}
ss.write(data)

ss.md('''
```python
data = ["aaa", "bbb", "ccc"]
ss.write(data)

data = {"aaa":1, "bbb":2, "ccc":3}
ss.write(data)
```
''')


ss.md("#### 4. 输出表格")
# 创建数据
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [25, 30, 35, 40],
        'city': ['New York', 'Paris', 'London', 'Sydney']}

# 将数据转换为 DataFrame 格式
df = pd.DataFrame(data)
ss.write(df)

ss.md('''
```python
# 创建数据
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [25, 30, 35, 40],
        'city': ['New York', 'Paris', 'London', 'Sydney']}

# 将数据转换为 DataFrame 格式
df = pd.DataFrame(data)
ss.write(df)
```
''')