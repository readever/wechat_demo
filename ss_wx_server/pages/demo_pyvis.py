import simplestream as ss

import networkx as nx
from pyvis.network import Network
import pyvis 

##用iframe.srcdoc，会造成console里面 Src明文太长
##用html造成代码不执行

# 创建一个只有几个节点的简单图
G = nx.path_graph(5) 

# 用Pyvis生成交互式网络图 
net = Network(notebook=True)
net.from_nx(G)
net.show_buttons(filter_=['physics']) 


# 在Streamlit中显示图
graph = net.generate_html()

with open('graph.html', 'w') as f:
  f.write(graph)

# 嵌入Streamlit界面中
#st.components.v1.html(graph, width=700, height=450)

test = graph

test2 = f'''
<iframe src="{graph}"></iframe>
'''

ss.component("http://www.baidu.com")

jscode = f'''
let doc = document;
let blob = new Blob([`{test}`], {{type : 'text/html'}});
let url = URL.createObjectURL(blob);
let iframe = document.createElement('iframe');
iframe.src = url;
doc.body.appendChild(iframe);
'''

ss.experimental_js(jscode)


#test
from io import BytesIO

data = "{test}"

# 将字符串数据封装成一个BytesIO对象  
blob = BytesIO(data.encode('utf-8'))

# 生成一个URL来访问这个对象
import uuid
url =uuid.uuid4().hex 

ss.write("url", url)

# 将对象存储在一个全局字典中,key是生成的url
import tempfile
blob_dict = tempfile.gettempdir()
blob_dict[url] = blob

ss.write("url", url)




'''
class BlobUrl(object):

    def __init__(self, data):
        self.blob = BytesIO(data)
        self.url = uuid.uuid4().hex
        self.finished = False
        
    def get_url(self):
        return self.url
    
    def read(self):
        if self.finished:
            raise ValueError("Blob is already read")
        self.finished = True
        return self.blob.read()

blob = BlobUrl(b"hello")
url = blob.get_url()

# 前端读取后
print(blob.read()) 

# 此时可以检测到finished标记为True,表示前端已读取
if blob.finished:
    del blob
'''