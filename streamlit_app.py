import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

def main1() : 
  st.write('Minimal Example')

if __name__ == '__main1__' : 
  main1()
  
def main2() : 
  st.header('This is Header')
  st.subheader('This is SubHeader')
  st.markdown('# Rendering Markdown ')
  st.write('Some Phytagorean Equation : ')
  st.latex('c^2 = a^2+b^2')

if __name__ == '__main2__' : 
  main2()
