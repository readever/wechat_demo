import simplestart as ss

ss.md("## ss.sqlite 数据库")

ss.space("mt-8")
ss.md('''
提供 sqlite 数据库的简单操作

    
##### 函数说明

| 函数 | 说明 |
| --- | --- | 
| sqlite(dbfile = None) | 创建实例, 如果指定的数据库文件路径，会自动调用Open打开数据库|
| open（dbfile） | 打开数据库，成功返回 True, 失败返回 False |
| close() | 关闭数据库 |
| query(sz_sql)| 查询数据库， sz_sql 是SQL查询语句 |
| pd_query(sz_sql) | 查询数据库，结果 pandas DataFrame 形式返回 |
| commit() | 提交修改 |

      
''')

ss.space("mt-8")
ss.md("#### 示例")
ss.write("这是波士顿房价数据表")

sql = ss.sqlite("./data/ss_data.db")
data = sql.pd_query("select * from HousingData")
ss.write(data)


ss.space("mt-8")
ss.write("#### 代码")

ss.md('''
```python
import simplestart as ss

sql = ss.sqlite("./data/ss_data.db")
data = sql.pd_query("select * from HousingData")
ss.write(data)
```
''')
