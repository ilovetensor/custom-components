import streamlit as st
from my_component2 import my_component

# and lose its current state. In this case, we want to vary the component's
# "name" argument without having it get recreated.
name_input = st.text_input("Enter a name", value="Streamlit")
num_clicks = my_component(name_input, key="foo")
st.markdown("You've clicked %s times!" % int(num_clicks))
