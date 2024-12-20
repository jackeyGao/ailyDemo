import streamlit as st
from aily_streamlit.connector import chat_with_skill
from aily_streamlit.sidebar import sidebar

sidebar()

st.caption("🎉 通过Aily的开放平台，不仅能够实现对话能力的集成对接，还能直接通过代码调用某个技能。在这里演示调用指定技能（润色文本）。")

# Streamed response emulator
def response_generator(input, style):
    stream = chat_with_skill(
        message=input, 
        skill_id="skill_dfb12fee999e", 
        skill_input=dict(
            style=style,
            input=input
        )
    )

    content = ""
    for message in stream:
        yield message.content.replace(content, '')
        content = message.content
    


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Accept user input
with st.container(border=2):
    option = st.selectbox(
        "选择风格",
        ("更礼貌", "更直白", "更严肃", "更活泼", "郭德纲"),
        index=1,
        placeholder="选择风格..",
    )
    input = st.text_area("你有哪些开放能力? ")


if st.button("润色", type="primary", key="pref", icon=":material/hotel_class:") and input:
    # Add user message to chat history
    # st.session_state.messages.append({"role": "user", "content": f"润色: {input}, 风格: {option}"})
    # Display user message in chat message container
    # Display assistant response in chat message container
    with st.container(border=2):
        with st.chat_message(
            "assistant", 
            avatar="https://anycross-showcase.feishu.cn/ai/img/182097/4c9f67aa89c244e48eeb326c6b587959_p.jpg"
        ):
            response = st.write_stream(response_generator(input, option))
    # Add assistant response to chat history
    # st.session_state.messages.append({"role": "assistant", "content": response})

