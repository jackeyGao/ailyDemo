import streamlit as st
from streamlit_chat import message
from connector import chat_with_stream
from connector import AilyTimeoutError

def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.past.append(user_input)
    st.session_state.generated.append( { "type": "normal", "data": "思考中..." }) 

    response = ""
    stream = chat_with_stream(user_input)
    
    try:
        for msg in stream:
            response += msg.content
            st.session_state.generated[-1] = { "type": "normal", "data": response }
    except AilyTimeoutError as e:
        # 处理超时的情况
        print(e)

    # st.session_state.generated.append("The messages from Bot\nWith new line")

def on_btn_click():
    del st.session_state.past[:]
    del st.session_state.generated[:]


# st.session_state.setdefault(
#     'past', 
#     [
#         "哈喽"
#     ]
# )
# st.session_state.setdefault(
#     'generated', 
#     [
#         {'type': 'normal', 'data': '你也好.'},
#     ]
# )


if 'past' not in st.session_state:
    st.session_state.setdefault('past', [])


if 'generated' not in st.session_state:
    st.session_state.setdefault('generated', [])


st.title("Aily Chat Demo")

chat_placeholder = st.empty()

with chat_placeholder.container():    
    for i in range(len(st.session_state['generated'])):                
        message(st.session_state['past'][i], is_user=True, key=f"{i}_user")
        message(
            st.session_state['generated'][i]['data'], 
            key=f"{i}", 
            allow_html=True,
            is_table=True if st.session_state['generated'][i]['type']=='table' else False
        )
    
    st.button("Clear message", on_click=on_btn_click)

with st.container():
    input = st.text_input("User Input:", on_change=on_input_change, key="user_input")