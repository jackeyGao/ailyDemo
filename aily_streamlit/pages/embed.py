import streamlit as st
from aily_streamlit.fetures.embed import cui, embed_url
from aily_streamlit.sidebar import sidebar


sidebar()


st.caption("Iframe 模式下，仅需一个 URL 即可完成接入。\n适合在已有 SaaS 系统、网页内快速集成 AI 会话面板组件，实现同 Aily Bot 的对话。 [详情](https://aily.feishu.cn/hc/8qluoxsa/ldyc3hvx)")


with st.container(border=2):
    st.markdown(f'''
<iframe
  src="{embed_url}"
  frameBorder="0"
  style="height: 700px; width: 100%;"
></iframe>
''',
    unsafe_allow_html=True)

