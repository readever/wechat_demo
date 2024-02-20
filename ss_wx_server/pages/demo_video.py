import streamsync as ss

ss.md("## ss.video 视频播放")

ss.md('''
播放视频，支持mp4等格式

##### ss.video(src)

| 参数 | 说明 |
| --- | --- | 
| src | 要播放的视频地址 |
      
''')

src = "https://media.w3.org/2010/05/sintel/trailer.mp4"

player = ss.video(src, style="width:100%; max-width:640px")

ss.text("来源: https://media.w3.org/2010/05/sintel/trailer.mp4", style="color:gray")

ss.space("mt-8")

ss.write('''
---
#### 代码
''')

ss.md('''
```python
import simplestart as ss

src = "https://media.w3.org/2010/05/sintel/trailer.mp4"

player = ss.video(src, style="width:100%; max-width:640px")
    
#修改视频地址
#player.src = "..."
```
''')
