import simplestart as ss

import cv2
from PIL import Image
import os

ss.md("## ss.image 图像")

ss.space("mt-8")
ss.md('''
在页面上显示图像的组件

#### 函数
ss.image(source)
      
##### 函数说明

| 参数 | 说明 |
| --- | --- | 
| image | 图像源，可以是网络路径、文件路径、PIL图像或者OpenCV图像 |
| fit | 图像显示时的fit模式，可以是 contain, cover, fill, scale-down 和 none |
      
''')


style = "width:200px;height:200px;margin:10px"
img = "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg"

cols = ss.columns([60,"flex:40; border-left:1px solid lightgray"], design=False, style="border:1px solid lightgray")
with cols[0]:
    mytext = ss.text("This is image")
    ss.space()
    myimg = ss.image(img, style=style, fit="fill")
    ss.text("Image fit mode: @fit_str")
    
def onradiochange(state, value):
    ss.message(value)
    ss.session.state["fit_str"] = value
    ss.getcm().components[myimg.id]["content"]["options"]["fit"] = value

def onradiochange2(state, value):
    source = ["Http", "PIL", "OpenCV", "Local"]
    ss.session.state["source_str"] = source[int(value)]
    count = int(value)

    if count == 0:
        img = "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg"
        ss.session.state["image_path"] = "\"https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg\""
        myimg.image = img
    if count == 1:
        image = Image.open('./media/image/dalao.jpeg')
        ss.session.state["image_path"] = "Image.open('./media/image/dalao.jpeg')"
        myimg.image = image
    if count == 2:
        img = cv2.imread('./media/image/cat.jpeg',cv2.IMREAD_COLOR)
        ss.session.state["image_path"] = "cv2.imread('./media/image/cat.jpeg',cv2.IMREAD_COLOR)"
        myimg.image = img  
    if count == 3:
        file_path = './media/image/dog.jpeg'
        ss.session.state["image_path"] = "'./media/image/dog.jpeg'"
        myimg.image = file_path
        
with cols[1]:
    ss.text("image fit mode")
    ss.radio(["fill", "contain", "cover", "none", "scale-down"], "fill", buttonstyle = True, onchange=onradiochange)
    ss.space()
    ss.text("image source")
    ss.radio([("0","Http image"), (1,"PIL image"), (2, "OpenCV image"), (3, "Local image")], "0", buttonstyle=False, onchange=onradiochange2)
    
ss.space()

ss.write("代码")

ss.md('''
```python
import simplestart as ss
import cv2
from PIL import Image

style = "width:100px; height:100px; margin:10px"
img = @image_path
ss.image(img, style=style, fit="@fit_str")
```
''')



def onPageLoad():
    ss.session.state["info"] = "x"
    ss.session.state["fit_str"] = "fill"
    ss.session.state["source_str"] = "Http"
    ss.session.state["image_path"] = "\"https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg\""
