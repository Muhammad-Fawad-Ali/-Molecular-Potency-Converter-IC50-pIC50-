import streamlit as st
import numpy as np

# Conversion functions
def ic50_to_pIC50(value):
    value = value * (10**-9)  # Convert IC50 to molar concentration
    return -np.log10(value)  # Convert to pIC50

def pIC50_to_IC50(value):
    ic50_value = 10 ** -value  # Convert pIC50 to molar concentration
    return ic50_value * 1e9  # Convert to nM

# Streamlit app layout
st.title("Molecular Potency Converter: IC50 & pIC50")
st.write("Convert between IC50 and pIC50 values with ease.")
st.write("This app was developed to provide quick, precise molecular potency conversions for researchers.")
# Option selection
option = st.radio("Select the conversion type:", ["IC50 to pIC50", "pIC50 to IC50"])

# Conversion and output
if option == "IC50 to pIC50":
    ic50_value = st.number_input("Enter IC50 value (nM):", min_value=0.0, format="%.2f")
    if st.button("Convert to pIC50"):
        pIC50_value = ic50_to_pIC50(ic50_value)
        st.success(f"{ic50_value} nM is approximately {pIC50_value:.2f} pIC50")
elif option == "pIC50 to IC50":
    pic50_value = st.number_input("Enter pIC50 value:", format="%.2f")
    if st.button("Convert to IC50"):
        ic50_value = pIC50_to_IC50(pic50_value)
        st.success(f"{pic50_value} pIC50 is approximately {ic50_value:.2f} nM")

st.markdown("---")
st.write("## About the Developer")
st.write("This app was developed Muhammad Fawad Ali, I am graduate student with major in Biochemistry.")
st.write("My research foucus on Computer aided drug design.")
st.write("Research skills set include Machine learning, AI, Molecular docking, pharmocophore modelling, ADMET and MD simulation.")
st.write("[GitHub Link](https://github.com/Muhammad-Fawad-Ali)")

st.markdown(
    """
    <style>
    /* Full-page background with a gradient and molecular pattern */
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(to right, #f0f8ff, #e0ecf8), 
                    url(''), 
                    url('');
        background-size: 100%, 150px, 200px;
        background-repeat: no-repeat, repeat, repeat;
        background-position: center, left top, right bottom;
        background-attachment: fixed;
        color: #333333;
    }

    /* Light opacity and rounded style for widgets */
    .stNumberInput, .stRadio, .stButton, .stTextInput {
        background: rgba(255, 255, 255, 0.8); /* Slight transparency */
        border-radius: 10px;
        padding: 10px;
    }

    /* Style for the conversion button */
    .stButton>button {
        color: white;
        background-color: #1E90FF;
        border-radius: 8px;
        font-size: 16px;
        padding: 10px 20px;
    }

    /* Styling for title and text */
    h1, h2, h3 {
        color: #1E90FF;
        font-family: 'Arial', sans-serif;
        font-weight: bold;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True
)