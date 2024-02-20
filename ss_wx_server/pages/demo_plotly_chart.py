import streamsync as ss

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

ss.heading("plotly demo")

# 生成模拟数据
data = {"fruit": ["apple", "banana", "cherry", "date"],
        "count": [4, 2, 5, 3]}
df = pd.DataFrame(data)

# 创建条形图
fig = px.bar(df, x="fruit", y="count", color="count", height=400)



# 显示图形
#fig.show()

ss.plotly_chart(fig, style="border:1px solid gray; width:800px")

ss.md("---")

ss.text("散点图")

fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
#fig.show()
ss.plotly_chart(fig, style="border:1px solid gray; width:800px")


df = px.data.iris()  # px自带数据集
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])
ss.plotly_chart(fig, style="border:1px solid gray; width:800px")

ss.text("折线图")


animals = ['giraffes', 'orangutans', 'monkeys']
 
fig = go.Figure(data=[
    go.Scatter(name='SF Zoo', x=animals, y=[20, 14, 23]),
    go.Scatter(name='LA Zoo', x=animals, y=[12, 18, 29])
])
#fig.show()
ss.plotly_chart(fig, style="border:1px solid gray; width:800px")

import numpy as np
np.random.seed(1)
 
N = 100
random_x = np.linspace(0, 1, N)
random_y0 = np.random.randn(N) + 5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N) - 5
 
# Create traces
fig = go.Figure()
fig.add_trace(go.Scatter(x=random_x, y=random_y0,
                    mode='lines',
                    name='lines'))
fig.add_trace(go.Scatter(x=random_x, y=random_y1,
                    mode='lines+markers',
                    name='lines+markers'))
fig.add_trace(go.Scatter(x=random_x, y=random_y2,
                    mode='markers', name='markers'))

ss.plotly_chart(fig, style="border:1px solid gray; width:800px")

ss.text("饼图")
# This dataframe has 244 lines, but 4 distinct values for `day`
df = px.data.tips()
fig = px.pie(df, values='tip', names='day')
ss.plotly_chart(fig, style="border:1px solid gray; width:800px")


df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
fig = px.pie(df, values='pop', names='country', title='Population of European continent')
#fig.show()

ss.plotly_chart(fig, style="border:1px solid gray; width:800px")

ss.text("箱型图")
df = px.data.tips()
fig = px.box(df, x="time", y="total_bill")
ss.plotly_chart(fig, style="border:1px solid gray; width:800px")

ss.text("气泡图")
import plotly.express as px
df = px.data.gapminder().query("year==2007")
fig = px.scatter_geo(df, locations="iso_alpha", color="continent",
                     hover_name="country", size="pop",
                     projection="natural earth")
ss.plotly_chart(fig, style="border:1px solid gray; width:800px")


ss.text("图像")
import cv2 
    
# You can give path to the 
# image as first argument 
img = cv2.imread('./media/image/dalao.jpeg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


fig = px.imshow(img_rgb)
fig.update_layout(width=400, height=300)

#fig.show()
ss.plotly_chart(fig, style="border:1px solid gray; width:400px;")
#ss.image(img)


ss.text("表格")

from plotly.subplots import make_subplots

# 读取csv文件数据
df = pd.read_csv('./data/iris.csv')

# 创建表格数据
table = go.Table(
    header=dict(
        values=list(df.columns),
        font=dict(size=14),
        align="left"
    ),
    cells=dict(
        values=[df[col] for col in df.columns],
        font=dict(size=12),
        align="left"
    )
)

# 创建布局
layout = go.Layout(
    title="Data",
    margin=dict(
        l=50,
        r=50,
        b=50,
        t=50
    ),
    showlegend=False
)

# 创建图表
fig = go.Figure(data=[table], layout=layout)


# 显示图像
#fig.show()
ss.plotly_chart(fig, style="border:1px solid gray; width:800px;")
