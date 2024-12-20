import streamlit as st


embed_url = "https://ae.feishu.cn/cui#appkey=a_1461a20fbe1e492885e6da1dfca0dd94&config=eyJjb252ZXJzYXRpb24iOnsidXNlckF2YXRhciI6Imh0dHBzOi8vczEtaW1maWxlLmZlaXNodWNkbi5jb20vc3RhdGljLXJlc291cmNlL3YxL3YzXzAwYWVfNzNiNDA5MWYtMzVhNC00Mzk5LWJjNDEtNTNkOTVhMmMzNDdnIiwiaW5pdFVzZXJNZXNzYWdlIjoiJUU3JUJEJTkxJUU3JUFCJTk5JUU1JUE2JTgyJUU0JUJEJTk1JUU1JUI1JThDJUU1JTg1JUE1QWlseSVFOCU4MSU4QSVFNSVBNCVBOSVFNSVBRiVCOSVFOCVBRiU5RCJ9fQ=="

@st.dialog("智能问答", width="large")
def cui():
    st.markdown(f'''
<iframe
  src="{embed_url}"
  frameBorder="0"
  style="height: 550px; width: 100%;"
></iframe>
''',
        unsafe_allow_html=True)