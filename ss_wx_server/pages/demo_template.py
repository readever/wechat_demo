import streamsync as ss


ss.md("## ss.template 简单模版")

ss.space("mt-8")
ss.md('''
在SimpleStart中，可以通过ss.template定义一个简单的vue组件，在这个组件里实现属性和数据交互。

#### 函数
ss.template(src, path, data, handlers)
      
##### 函数说明

| 参数 | 说明 |
| --- | --- | 
| src | 字符串形式的组件脚本 |
| path | 外部文件的组件的原代码路径 |
| data | 用于实现前端组件和Python端的交互数据 |
| handlers | 在Python端实现前端组件定义的事件 |
      
''')

ss.space("mt-8")

ss.md('''
---
#### 示例1
在这里例子中，我们定义一个简单的前端组件，组件里定义了一个"myclick"事件，当用户点击"Click me"按钮时，
Python端的myclick事件处理函数会处理，并且接受前端组件传递的数据。同时，当点击Python端的 "增加数字"
按钮时，通过state变量改变前端的数值。

''')

template1 = '''
<el-space wrap fill>
<el-card class="box-card">
    <template #header>
      <div class="card-header">
        <span>当前数字:@counter</span>
        <el-button class="button" text \@click='onserver("myclick", 12345)'>Click me</el-button>
      </div>
    </template>
    <div v-for="o in 4" :key="o" class="text item">{{ 'List item ' + o }}</div>
  </el-card>
</el-space>
'''

def myclick(state, value=None):
    ss.message(f"you trigger myclick {value}")

ss.template(template1, handlers = {"myclick":myclick})


ss.session.state["counter"] = 0

def increment(state, value=None):
    state["counter"] += 1

ss.space()
ss.button("增加数字", onclick=increment)

ss.space("mt-8")

ss.write('''
---
#### 代码
''')

ss.md('''
```python
import simplestart as ss

def myclick(state, value=None):
    ss.message(f"you trigger myclick {value}")

ss.template(template1, handlers = {"myclick":myclick})


ss.session.state["counter"] = 0

def increment(state, value=None):
    state["counter"] += 1

ss.space()
ss.button("增加数字", onclick=increment)
```
''')

ss.space("mt-8")

ss.md('''
---
#### 示例2
在这里例子中，我们将 element plus 的颜色组件 ColorPicker 引入进来,通过它不但可以获取
选择的颜色值，也可以预定义颜色值。从而实现前端组件与Python端的数据通讯。这个例子中，我们通过
template输出化时的data变量，直接获取在组件中的变量改变值。

''')

data = {"color":"#409EFF"}
cp = ss.template('''
    <span class="demonstration">颜色选择 &nbsp;</span>
    <el-color-picker show-alpha v-model="data.color" \@change = 'syncdata' />
    ''', data=data)

def getColor():
    txt.text = cp.data["color"]

ss.button("获取颜色值", onclick = getColor)

def setColor(state, value):
    cp.data["color"] = "0xff0000"
    
ss.button("设置颜色值", onclick = setColor)

txt = ss.text("")

ss.md('''
::: tip
  组件内对于data的变化如果需要传递到后端，需要显示地调用syncdata或者onserver事件。
  如上面例子中的 onchange="syncdata", 就是当用户改变了颜色后，将data的值传到python后端。
:::
''')