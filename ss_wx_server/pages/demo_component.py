import simplestream as ss

ss.md("### ss.component")


def testme(state, value):
    mytext.text = "接收到的前端UI的数据: " + value["value"]
    
#默认情况下，<iframe> 的宽度为 300 像素，高度为 150 像素。
ss.text("在文本框中输入内容并按回车")
myplugin = ss.component(path = f"components/index.html", onData = testme) ###style="border:none")


def postdata():
    data = {"my_input_value":"text from python"}
    myplugin.postMessage(data)

mytext = ss.text("接收到的前端UI的数据: ")

ss.markdown("---")
ss.space()
ss.text("点击按钮，传递数据到UI前端")
ss.button("post data", onclick=postdata)

ss.space()

ss.write("Python端代码")

ss.md('''
```python
import simplestart as ss

def testme(state, value):
    mytext.text = "接收到的前端UI的数据: " + value["value"]
    
ss.text("在文本框中输入内容并按回车")
myplugin = ss.component(path = f"components/index.html", onData = testme)

def postdata():
    data = {"my_input_value":"text from python"}
    myplugin.postMessage(data)

mytext = ss.text("接收到的前端UI的数据: ")

ss.markdown("---")

ss.space()
ss.text("点击按钮，传递数据到UI前端")
ss.button("post data", onclick=postdata)

```
''')

ss.write("Plugin/html/js端代码")

ss.md('''
```html
<html>
    
<head>
    <script src="pybridge.js"></script>
</head>
    
<body style="height:100px">
    <input id="myinput" value="" autocomplete="off" placeholder="输入内容，并按回车" />
</body>
    
<script>
    var myInput = document.getElementById("myinput");

    myInput.addEventListener("change", function() {
        ////将消息发送给Python端
        sendDataToPython({
            value: myInput.value,
        });
    })
    
    //接受来自Python端的消息消息
    window.addEventListener("message", onDataFromPython);
    
    function onDataFromPython(event) {
        var data = event.data.arg;
        if (event.data.type !== "ss:render") return;
            myInput.value = data.my_input_value;  // Access values sent from Python here!
    }
    
    //如果系统设置失败，可以手工设置高度
    //setFrameHeight(200);
</script>

</html>

```
''')