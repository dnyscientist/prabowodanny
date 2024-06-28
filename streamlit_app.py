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
import json

# Read the CSV file
house = pd.read_csv('house_clean.csv')

def main():
    st.write('Contoh dataframe')
    st.dataframe(house)
   # Load JSON data from file
    with open('timeseries.json', 'r') as f:
        json_data = json.load(f)
    # Display JSON data using Streamlit
    st.subheader('JSON Data:')
    st.json(json_data)
  
    st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
    
    st.write('Menampilkan Dataframe dengan St AgGrid')
    # AgGrid(house)
    
    st.table([x for x in range(1, 5)])

if __name__ == '__main__':
    main()

import plotly.express as px 
import matplotlib.pyplot as plt
# Read dataframe from CSV file
titanic = pd.read_csv('titanic.csv')

def main() : 
    #matplotlib chart 
    fig,ax = plt.subplots()
    plt.scatter(titanic['Age'],titanic['Fare'])
    st.pyplot(fig)
    plotly_fig = px.scatter(titanic['Age'],titanic['Fare'])
    st.plotly_chart(plotly_fig)
  
if __name__ == '__main__':
    main()

def main() : 
    click_me_btn = st.button('Click Me')
    st.write(click_me_btn) #Return True kalo di Click 
    check_btn = st.checkbox('Klik Jika Setuju')
    if check_btn :
        st.write('Anda Setuju')
    
    
    radio_button= st.radio('Choose below',[x for x in range(1,3)])
    st.write('Anda Memilih',radio_button)
    
    #slider 
    age_slider = st.slider('Berapa Usia Anda',0,100)
    st.write('Usia Anda',age_slider)
    
    #Input (Typing)
    num_input = st.number_input('Input Berapapun')
    st.write('Kuadrat dari {} adalah {}'.format(num_input,num_input**2))

    #Input (Typing)
    alas_input = st.number_input('Input Alas')
    tinggi_input = st.number_input('Input Tinggi')
    st.write('Luas dari segitiga adalah {}'.format(1/2*alas_input*tinggi_input))
if __name__ == '__main__' : 
  main()

def main() : 
    #sidebar 
    sidebar_checkbox = st.sidebar.checkbox('Checkbox di Sidebar')
    sidebar_radio_button = st.sidebar.radio('Pilih Menu',options=['A','B','C'])
    # Insert containers separated into tabs:
    tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
    tab1.write("this is tab 1")
    tab2.write("this is tab 2")

    # You can also use "with" notation:
    with tab1:
        st.radio("Select one:", [1, 2])
    #columns :
    col1, col2, col3 = st.columns(3)

    with col1:
       st.header("A cat")
       st.image("https://static.streamlit.io/examples/cat.jpg")
    #atau dengan assignment 
    # image_col1 = col1.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
       st.header("A dog")
       st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
       st.header("An owl")
       st.image("https://static.streamlit.io/examples/owl.jpg")
    #expander 
    #dengan with atau dengan assignment 
    expander = st.expander("Klik Untuk Detail ")
    expander.write('Anda Telah Membuka Detail')
if __name__ == '__main__' : 
  main()
import time
def main() : 
    #sidebar 
    with st.form("Data Diri"):
       st.write("Inside the form")
       slider_val = st.slider("Form slider",0,1000)
       checkbox_val = st.checkbox("Form checkbox")

       # Every form must have a submit button.
       submitted = st.form_submit_button("Submit")
       if submitted:
           st.write("slider", slider_val, "checkbox", checkbox_val)

    st.write("Outside the form")

    # Show a spinner during a process
    with st.spinner(text="In progress"):
        time.sleep(3)
        st.success("Done")
    
    # Show and update progress bar
    bar = st.progress(50)
    time.sleep(3)
    bar.progress(100)
    
    with st.status("Authenticating...") as s:
        time.sleep(2)
        st.write("Some long response.")
        s.update(label="Response")
    
    st.balloons()
    st.snow()
    st.toast("Warming up...")
    st.error("Error message")
    st.warning("Warning message")
    st.info("Info message")
    st.success("Success message")
    # Example of potential exception handling
    try:
        # Simulate some operation that might raise an exception
        result = 1 / 0  # This will raise a ZeroDivisionError
        st.write("Result:", result)
    except Exception as e:
        st.error(f"Error: {str(e)}")
if __name__ == '__main__' : 
  main()

import numpy as np

# Generate example DataFrame
np.random.seed(0)
df = pd.DataFrame({
    'x': np.arange(100),
    'y': np.random.randn(100),
    'category': np.random.choice(['A', 'B', 'C'], 100)
})

def main():
    st.title('Streamlit Chart Examples')

    # Area Chart
    st.subheader('Area Chart')
    st.area_chart(df['y'])

    # Bar Chart
    st.subheader('Bar Chart')
    st.bar_chart(df.set_index('x'))

    # Horizontal Bar Chart
    st.subheader('Horizontal Bar Chart')
    st.bar_chart(df.set_index('x'), use_container_width=True, orientation='h')

    # Line Chart
    st.subheader('Line Chart')
    st.line_chart(df.set_index('x'))

    # Map
    st.subheader('Map')
    st.map(df)

    # Scatter Chart
    st.subheader('Scatter Chart')
    st.scatter_chart(df, x='x', y='y')

if __name__ == '__main__':
    main()
