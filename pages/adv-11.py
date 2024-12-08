import streamlit as st

st.title("adv-11 page")
st.write("Hello World")
st.text("This is a text")
st.markdown(
    """
    # This is a markdown
    ## This is a markdown
    ### This is a markdown
"""
)

st.text(
    """
    # This is a markdown
    ## This is a markdown
    ### This is a markdown
"""
)

st.write(
    """
    # This is a markdown
    ## This is a markdown
    ### This is a markdown
"""
)

d = {"a": 1, "b": 2}
st.markdown(d)
st.write(d)

st.write("# expander 展開元件")
with st.expander("這是一個展開元件"):
    st.write("這是展開元件裡面的內容")

st.write("這是展開元件的外面")

st.write("---")

st.write("# number_input 數字輸入元件")
number = st.number_input("請輸入一個數字", min_value=0, max_value=100, value=50, step=5)
st.write(f"你輸入的數字是: {number}")

st.write("---")

st.write("# text_input 文字輸入元件")
text = st.text_input("請輸入一些文字", value="Hello World")
st.write(f"你輸入的文字是: {text}")

st.write("---")

st.write("# st.button 按鈕元件")
if st.button("按我", key="btn1"):
    st.write("你按了我")
    st.balloons()

st.write("---")

st.write("# st.columns 欄位元件")
col1, col2 = st.columns(2)  # 2個欄位
col1.write("這是第一個欄位")
if col1.button("按我", key="btn2"):
    col1.balloons()

col2.write("這是第二個欄位")
if col2.button("按我", key="btn3"):
    col2.balloons()
