import streamlit as st
import numpy as np
import plotly.express as pe
st.markdown(
    """
    <style>
    .main{
    background-color: #40E0D0;
    color: black;
    }
    </style>
    """,
    unsafe_allow_html=True)
st.title("aaja oye")
a=st.text_input("ID bhar sheti")
b=st.text_input("password tera fuffar bharuga, bhar b*******")
if st.button("Sign in"):
    if a=="kridham08" and b=="ridham_08":
        st.write("shukar tenu yaad aa")
    else:
        st.write(" chal saaleya bhorti ")

st.title("Tax calculator")
name=st.text_input("tera naam ki ae")
val=st.number_input("tu kamaana kinna ae ")
tax=0
if st.button("Calculator"):
    if val<500000:
        tax=0
    elif val<750000:
        tax=val*5/100
    else:
        tax=val*10/100
    st.subheader(f"tere kolo har saal enne paise lene ae = {tax}")

st.title("EMI calculator")
loan=st.number_input("kinne karze thalle lgga ")
time=st.slider("kinne saal lyi de riha ",0,10,2)
interest=8.75
emi=(loan*interest*time/100)+loan
emi=emi/(time*12)
st.subheader(f"kinni de riha {int(emi)}")
