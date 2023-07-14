import streamlit as st
import plotly.express as px
import pandas as pd
from backend import backend

def frontend():
    st.title("Chemical Composition Input")

    # Layout
    col1, col2, col3, col4, col5 = st.columns(5)  # Divide the page into 5 columns


    # Input fields row 1
    with col1:
        st.write("c(Fe) (%)")
        st.write("rest")
    with col2:
        c_c = st.text_input("c(C) (%)")
    with col3:
        c_n = st.text_input("c(N) (%)")
    with col4:
        c_cr = st.text_input("c(Cr) (%)")
    with col5:
        c_ni = st.text_input("c(Ni) (%)")

    # Elements
    with col1:
        st.write("Mo")
    with col2:
        st.write("Al")
    with col3:
        st.write("Mn")
    with col4:
        st.write("Cu")
    with col5:
        st.write("Si")

    # Input fields row 2
    with col1:
        c_mo = st.text_input("c(Mo) (%)")
    with col2:
        c_al = st.text_input("c(Al) (%)")
    with col3:
        c_mn = st.text_input("c(Mn) (%)")
    with col4:
        c_cu = st.text_input("c(Cu) (%)")
    with col5:
        c_si = st.text_input("c(Si) (%)")

    # Calculate properties button
    calculate = st.button("Calculate Properties")

    # Handle button click
    if calculate:
        try:
            composition_dict = {
                "c(Fe) (%)": 0.0,  # Placeholder value for Fe
                "c(C) (%)": c_c,
                "c(N) (%)": c_n,
                "c(Cr) (%)": c_cr,
                "c(Ni) (%)": c_ni,
                "c(Mo) (%)": c_mo,
                "c(Al) (%)": c_al,
                "c(Mn) (%)": c_mn,
                "c(Cu) (%)": c_cu,
                "c(Si) (%)": c_si
            }
            total_sum = sum(composition_dict.values())
            if total_sum < 100:
                composition_dict["c(Fe) (%)"] = 100 - total_sum
            elif total_sum > 100:
                raise ValueError("Sum of composition exceeds 100%")
            else:
                pass  # Sum is exactly 100, no need to adjust "Fe"

            results = backend(**composition_dict)
            display_results(results)
        except ValueError as e:
            st.error(str(e))

