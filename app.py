import streamlit as st
import pandas as pd

on = st.toggle('Activate feature')

if on:
    st.write('Feature activated!')



st.write('Test')