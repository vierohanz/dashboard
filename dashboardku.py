import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import numpy as np
from babel.numbers import format_currency

df = pd.read_csv('proyek_data_analyst.csv')

# #Mengubah dtype column
data_column = ['order_purchase_timestamp','order_approved_at','order_delivered_carrier_date',
               'order_estimated_delivery_date','order_delivered_customer_date']
for change in data_column:
    df[change] = pd.to_datetime(df[change])
    print(df.info())
    
minimum = df['order_estimated_delivery_date'].min()
maximum = df['order_estimated_delivery_date'].max()
with st.sidebar:
    st.image('pngegg.png')
        
    
col1, col2 = st.columns(2)
with col1:
    st.header("Purchase City")
    code = """# EDA 1: Visualizing Number of Orders in Each City
data_penjualan = df.groupby(by=df['customer_city']).order_id.nunique().sort_values(ascending=False).reset_index(0).head()
st.title('Exploratory Data Analysis (EDA)')
st.subheader('Number of Orders in Each City')
fig, ax = plt.subplots(figsize=(12, 8))
ax.barh(y=data_penjualan['customer_city'], width=data_penjualan['order_id'], color='orange')
ax.set_title('DATA PENJUALAN 5 KOTA')
ax.set_xlabel('Number of Orders')
ax.set_ylabel('City')
st.pyplot(fig)
st.balloons()"""
    st.code(code, language='python')

with col2:
    st.header("Salles Status")
    code = """# EDA 2: Visualizing Order Status
status_penjualan = df.groupby(by=df['order_status']).order_id.nunique().sort_values(ascending=False).reset_index(0).head()
st.subheader('Order Status Visualization')
fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(x=status_penjualan['order_status'], height=status_penjualan['order_id'], color='blue')
ax.set_title('PERBANDINGAN')
ax.set_xlabel('Status (Order)')
ax.set_ylabel('Number of Customers')
st.pyplot(fig)
st.balloons()
"""
    st.code(code, language='python')


# EDA 1: Visualizing Number of Orders in Each City
data_penjualan = df.groupby(by=df['customer_city']).order_id.nunique().sort_values(ascending=False).reset_index(0).head()
st.title('Exploratory Data Analysis (EDA)')
st.subheader('Number of Orders in Each City')
fig, ax = plt.subplots(figsize=(12, 8))
ax.barh(y=data_penjualan['customer_city'], width=data_penjualan['order_id'], color='orange')
ax.set_title('DATA PENJUALAN 5 KOTA')
ax.set_xlabel('Number of Orders')
ax.set_ylabel('City')
st.pyplot(fig)
st.balloons()

# EDA 2: Visualizing Order Status
status_penjualan = df.groupby(by=df['order_status']).order_id.nunique().sort_values(ascending=False).reset_index(0).head()
st.subheader('Order Status Visualization')
fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(x=status_penjualan['order_status'], height=status_penjualan['order_id'], color='blue')
ax.set_title('PERBANDINGAN')
ax.set_xlabel('Status (Order)')
ax.set_ylabel('Number of Customers')
st.pyplot(fig)
st.balloons()

# Caption Hak Cipta
st.caption('Copyright (c) Dicoding 2023')
