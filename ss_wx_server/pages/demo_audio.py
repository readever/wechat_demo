import streamsync as ss

ss.md("## ss.audio 音频播放")

ss.space("mt-8")
ss.md('''
播放音频, 支持wav, mp3 等格式

#### 函数
ss.audio(src)
      
##### 函数说明

| 参数 | 说明 |
| --- | --- | 
| src | 音频文件的路径，支持http url 和 本地路径 |
      
''')


ss.space("mt-8")
ss.md('''
---
#### 示例
''')

audiosrc = "media/davide_quatela--breathing_barcelona.mp3"
player = ss.audio(audiosrc)

ss.md('''
作品:Breathing Barcelona
作者:Davide Quatela
来源:Mazwai.com
''')

ss.space("mt-8")

ss.write('''
---
#### 代码
''')

ss.md('''
```python
import simplestart as ss

audiosrc = "media/davide_quatela--breathing_barcelona.mp3"
player = ss.audio(audiosrc)
```
''')


