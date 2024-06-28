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

# Read JSON file from GitHub repository
url = 'timeseries.json'
response = requests.get(url)
covid = response.json()

def main():
    st.write('Contoh dataframe')
    st.dataframe(house)
    
    st.write('Contoh JSON')
    st.json(covid)
    
   
    st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
    
    # st.write('Menampilkan Dataframe dengan St AgGrid')
    # AgGrid(house)
    
    # st.table([x for x in range(1, 5)])

if __name__ == '__main__':
    main()
