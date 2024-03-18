import streamlit as st 
import pandas as pd
import numpy as np
voc=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRHSxLMq45CeyPtFGnXQaIevxQHFmbiefc0xiMiHCWbfaJD6yi8qbMEdVQksCqwPbfBiqVaWKrKBd4H/pub?output=csv")
st.dataframe(voc)







