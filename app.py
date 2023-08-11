import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='Portfolio Optimization')
st.header('Optimize your Portfolio')
st.subheader('Closing Prices')

### --- LOAD DATAFRAME

excel_file = 'PORTFOLIO_OPTIMIZATION.xlsx'
sheet_name = '1_RISKY_ASSETS'

df_closing_prices = pd.read_excel(excel_file, 
                   sheet_name=sheet_name,
                   usecols='A:F',
                   header=1)

df_asset_allocation = pd.read_excel(excel_file, 
                   sheet_name='5_ASSET_ALLOCATION',
                   usecols='L:M',
                   header=2,
                   nrows=5)
 
df_risky_portfolio = pd.read_excel(excel_file, 
                   sheet_name='5_ASSET_ALLOCATION',
                   usecols='L:M',
                   header=11,
                   nrows=5)

df_portfolio = pd.read_excel(excel_file, 
                   sheet_name='5_ASSET_ALLOCATION',
                   usecols='L:M',
                   header=19,
                   nrows=6)
 
df_asset_allocation.dropna(inplace=True)

df_portfolio.dropna(inplace=True)

st.dataframe(df_closing_prices)

st.subheader('Weight Distribution')
st.dataframe(df_asset_allocation)

st.subheader('OPTIMAL RISKY PORTFOLIO')
st.dataframe(df_risky_portfolio)

#st.subheader('HOW DOES THE PORTFOLIO LOOK?')
#st.dataframe(df_portfolio)

pie_chart = px.pie(df_portfolio,
                    title = 'HOW DOES THE PORTFOLIO LOOK?',
                    values = 'WEIGHTS',
                    names = 'STOCKS')
               
st.plotly_chart(pie_chart)

image = Image.open('images/graph.jpg')
st.image(image, 
         caption = 'Designed by ceativeart / Freepik',
         use_column_width=True)
