import simplestart as ss

ss.md("## ss.loadvue 自定义VUE组件")

ss.space("mt-8")
ss.md('''
在SimpleStart中，可以通过ss.loadvue加载自定义的vue组件，在这个组件里实现属性和数据交互。

#### 函数
ss.loadvue(src, path, data, handlers)
      
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
#### 示例
在这里例子中，我们定义一个简单的前端组件，组件里定义了一个"myclick"事件，当用户点击"Click me"按钮时，
Python端的myclick事件处理函数会处理，并且接受前端组件传递的数据。同时，当点击Python端的 "增加数字"
按钮时，通过state变量改变前端的数值。

''')

ss.space("mt-8")
ss.md("---")
ss.space("mt-8")

tagid = 0
tags = ["Python", "Java", "Javascript"]
data = {"count":0, "language":"C++"}
global myvue

#trigger event on server from client side
def ontest(state, value):
    ss.message(value)

#change data in client component on server side
def changedata(state, value=None):
    global tagid
    myvue.data["language"] = tags[tagid]
    tagid = (tagid+1) % 3
    
ss.text("Python 端")
ss.button("修改数据", onclick=changedata)

ss.space()
sec = ss.section()

def onPageLoad():
    global myvue
    #load code from file
    with sec:
        ss.text("组件端")
        myvue = ss.loadvue(path = "components/mycomponent.vue", data = data, handlers = {"ontest":ontest})
    
    
ss.space()
ss.write("Python端 代码")

ss.md('''
```python
tagid = 0
global myvue

tags = ["Python", "Java", "Javascript"]
data = {"count":0, "language":"C++"}


#trigger event on server from client side
def ontest(state, value):
    ss.message(value)

#change data in client component on server side
def changedata(state, value=None):
    global tagid
    myvue.data["language"] = tags[tagid]
    tagid = (tagid+1) % 3
    
ss.text("Python 端")
ss.button("修改数据", onclick=changedata)


def onPageLoad():
    global myvue
    #load code from file
    myvue = ss.loadvue(path = "components/mycomponent.vue", data = data, handlers = {"ontest":ontest})
```
''')


ss.space()
ss.write("Vue JS代码")

ss.md('''
```js
<template>
  <div class="my-component">
    <h1>{{title}}: {{ data.language }}</h1>
    <el-button @click="testme">handle on server</el-button>
  </div>
</template>

<script>
module.exports = {
    name: 'MyComponent',

    data() {
        return {
            title:"computer",
        }
    },

    methods: {
        testme(){
            this.streamsync.forwardData(this, eventname="ontest", "12345")
        }
    }
}
</script>

<style>
.my-component {
    width:50%;
    background-color: #f0f0f0;
    padding: 20px;
    margin:10px 0;
}
</style>

```
''')