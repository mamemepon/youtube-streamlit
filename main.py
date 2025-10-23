import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title('行ってみよう会')

st.write('おでかけ記録')

if st.checkbox('Show Image'):
    img = Image.open('IMG_staba.JPG')
    st.image(img, caption='STABA',use_container_width=True)



st.write('Intaractive Widgets ↓')    

option = st.sidebar.selectbox(
    'あなたの好きな数字を教えて下さい。',
    list(range(1, 11))
)
'あなたの好きな数字は', option,'です。'

text = st.sidebar.text_input('あなたの趣味を教えてください。')
'あなたの趣味：', text

condition = st.sidebar.slider('あなたの調子は？',0, 100, 50)
'コンディション：', condition

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')


st.write('プレグレスバーの表示 ↓')
'START!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!'



df1= pd.DataFrame({
    '１列目':[1, 2, 3, 4],
    '２列目':[10, 20, 30, 40]
})
st.write(df1)

st.dataframe(df1.style.highlight_max(axis=0), width=100, height=100)

st.table(df1.style.highlight_max(axis=0))



df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(df2)

st.area_chart(df2)

st.bar_chart(df2)


df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50]+[35.69, 139.70],
    columns=['lat', 'lon']
)
st.map(df3)





"""
# 章
## 節
### 項

```pthon
import streamlit as st
import numpy as np
import pandas as pd
```
"""