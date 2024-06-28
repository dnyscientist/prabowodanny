import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

%%writefile  webapp.py 
import streamlit as st 

def main() : 
  st.header('This is Header')
  st.subheader('This is SubHeader')
  st.markdown('# Rendering Markdown ')
  st.write('Some Phytagorean Equation : ')
  st.latex('c^2 = a^2+b^2')

if __name__ == '__main__' : 
  main()
