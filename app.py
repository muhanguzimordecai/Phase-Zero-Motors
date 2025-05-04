import streamlit as st
import pandas as pd

st.title('F1 Fantasy Analytics')
data = pd.read_csv('data/latest_results.csv')
st.line_chart(data.set_index('Race')[['DriverA', 'DriverB']])
