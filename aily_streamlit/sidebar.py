import streamlit as st
from aily_streamlit.fetures.embed import cui

def sidebar():

    st.html('''
<style>
.st-key-assistant button {
    position: fixed;
    right: 10px;
    bottom: 10px;   
    z-index: 1000;     
}
</style>''')
    if st.button("", type="primary", icon=":material/smart_toy:", key="assistant"):
        cui()

    with st.sidebar:
        st.image("https://lf3-static.bytednsdoc.com/obj/eden-cn/LMfspH/ljhwZthlaukjlkulzlp/logo.png")

        st.caption("飞书智能应用平台为开发者提供了一系列开放 API，允许你将系统与 Aily 助手进行无缝连接。通过这些 API，你可以管理用户会话、发送和接收消息，以及执行复杂的技能调用。")

        st.caption("[Aily 开放能力介绍](https://aily.feishu.cn/hc/8qluoxsa/cvg9t9pe)")

        st.page_link("main.py", label="Aily Chat", icon=":material/hotel_class:")

        st.page_link("pages/embed.py", label="Embed ChatUI", icon=":material/bolt:")

        st.page_link("pages/skill.py", label="Trigger Skill", icon=":material/rebase:")