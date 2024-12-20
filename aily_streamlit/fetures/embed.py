import streamlit as st
from aily_streamlit.config import settings


app_key = settings.get("general", {}).get("app_key", "")


embed_url = f"https://ae.feishu.cn/cui#appkey={app_key}&config=eyJjb252ZXJzYXRpb24iOnsidXNlckF2YXRhciI6Imh0dHBzOi8vczEtaW1maWxlLmZlaXNodWNkbi5jb20vc3RhdGljLXJlc291cmNlL3YxL3YzXzAwYWVfNzNiNDA5MWYtMzVhNC00Mzk5LWJjNDEtNTNkOTVhMmMzNDdnIiwiaW5pdFVzZXJNZXNzYWdlIjoiJUU3JUJEJTkxJUU3JUFCJTk5JUU1JUE2JTgyJUU0JUJEJTk1JUU1JUI1JThDJUU1JTg1JUE1QWlseSVFOCU4MSU4QSVFNSVBNCVBOSVFNSVBRiVCOSVFOCVBRiU5RCJ9fQ=="

@st.dialog("智能问答", width="large")
def cui():
    st.caption("注意: 访问会话面板的终端用户，需要具备**飞书登录态（并确保在 Aily Bot 的可用范围内）**，才能发起对话")

    st.markdown(f'''
<iframe
  src="{embed_url}"
  frameBorder="0"
  style="height: 550px; width: 100%;"
></iframe>
''',
        unsafe_allow_html=True)