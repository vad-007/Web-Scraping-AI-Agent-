import streamlit as st
import selenium.webdriver as webdriver
from selenium import webdriver
from app import scrape_wbsite

st.title('AI Web Scraper')
url=st.text_input('Enter the URL')

if st.button('Scrape site'):
    st.write('Scraping site...')
    result= scrape_wbsite(url)
    print(result)