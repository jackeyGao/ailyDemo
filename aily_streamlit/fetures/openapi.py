import streamlit as st
from aily_streamlit.connector import chat_with_stream
from aily_streamlit.connector import AilyTimeoutError
from aily_streamlit.fetures.embed import cui

# Streamed response emulator
def response_generator(message):
    stream = chat_with_stream(message)

    content = ""
    for message in stream:
        yield message.content[len(content):]
        content = message.content
    

def init_default():
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("你有哪些开放能力? "):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message(
            "user",
            avatar="https://s1-imfile.feishucdn.com/static-resource/v1/v3_00ae_73b4091f-35a4-4399-bc41-53d95a2c347g",
        ):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message(
            "assistant", 
            avatar="https://anycross-showcase.feishu.cn/ai/img/182097/4c9f67aa89c244e48eeb326c6b587959_p.jpg"
        ):
            response = st.write_stream(response_generator(prompt))
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

