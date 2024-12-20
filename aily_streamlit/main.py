import streamlit as st
import random
import time
from aily_streamlit.fetures.openapi import init_default
from aily_streamlit.sidebar import sidebar



st.title("Aily Chat")
st.caption("欢迎体验飞书智能伙伴创建平台（:blue[Aily]）开放平台演示应用，在这里你可以问我关于Aily的开放能力相关的问题 ：）")

sidebar()



init_default()
