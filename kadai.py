#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import streamlit as st
import plotly.express as px


# In[2]:


#merged.csvを読み込む
merged_df = pd.read_csv('merged.csv')


# In[3]:


#streamlitの部品設定
st.title('サロンサーチ')
price_limit = st.slider("最低カット価格の上限", min_value=1000, max_value=9500, step=200, value=6000)
score_limit = st.slider("人気スコアの下限", min_value=0.0, max_value=18.5, step=2.0, value=5.0)


# In[4]:


#フィルタ処理
filtered_df = merged_df[
    (merged_df['Average_Price'] <= price_limit) &
    (merged_df['pop_score'] >= score_limit)
]


# In[5]:


#散布図の作成
fig = px.scatter(
    filtered_df,
    x = 'pop_score',
    y = 'Average_Price',
    hover_data = ['Title', 'Genre', 'Rating', 'Review_Count'],
    title = '人気スコアと最低カット価格の散布図'
)

st.plotly_chart(fig)


# In[7]:


# 詳細リンクの表示
selected_salon = st.selectbox('気になるサロンを選んで詳細を確認', filtered_df['Title'])

if selected_salon:
    url = filtered_df[filtered_df['Title'] == selected_salon]['URL'].values[0]
    st.markdown(f"[{selected_salon}のページへ移動]({url})", unsafe_allow_html=True)


# In[8]:


# In[13]:


sort_key = st.selectbox(
    "ランキング基準を選んでください",
    ("Rating", "pop_score", "Review_Count", "Average_Price")
)

ascending = True if sort_key == "Average_Price" else False


# In[9]:


# In[14]:


st.subheader(f"{sort_key}によるサロンランキング（上位10件）")

ranking_df = filtered_df.sort_values(by=sort_key, ascending=ascending).head(10)


# In[10]:


# 必要な列だけ表示
st.dataframe(ranking_df[["Title", "Average_Price", "pop_score", "Rating", "Review_Count",  "Genre"]])


# In[ ]:





# In[ ]:




