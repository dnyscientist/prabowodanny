import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

def main() : 
  st.write('Minimal Example')

if __name__ == '__main__' : 
  main()
  
def main() : 
  st.header('Halaman Streamlit Prabowo Danny W')
  st.subheader('Web ini memiliki konten terkait Data Scientist')
  st.markdown('#### Rendering Markdown ')
  st.write('Some Phytagorean Equation : ')
  st.latex('c^2 = a^2+b^2')

if __name__ == '__main__' : 
  main()

import requests
from st_aggrid import AgGrid

# Read the CSV file
house = pd.read_csv('house_clean.csv')

def main():
    st.write('Contoh dataframe')
    st.dataframe(house)
    st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
    
    st.write('Menampilkan Dataframe dengan St AgGrid')
    AgGrid(house)
    
    st.table([x for x in range(1, 5)])

if __name__ == '__main__':
    main()

import plotly.express as px 
import matplotlib.pyplot as plt
# Read dataframe from CSV file
titanic = pd.read_csv('titanic.csv')

def main():
    st.write('Contoh dataframe')
    st.dataframe(titanic)
  
if __name__ == '__main__':
    main()
