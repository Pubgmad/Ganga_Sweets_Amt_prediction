import streamlit as st
import pandas as pd
import os

logo_path = "abcLogo.jpg"
if os.path.exists(logo_path):
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image(logo_path, width=200)
else:
    st.warning("Logo image not found. Please check the file path.")

st.markdown(
    "<h1 style='text-align: center; color: black;'>Ganga Sweets</h1>",
    unsafe_allow_html=True
)

process = st.selectbox(
    "Select Process",
    ("Select...", "Dosa Prediction", "Sweet Prediction")
)

dosa_outputs = [
    ("Predicted vs Actuals", r"G:\ganga abc\Output\Dosa prediction vs actuals.xlsx"),
    ("Overall Dosa Prediction", r"G:\ganga abc\Output\Overall Dosa prediction.xlsx")
]
sweet_outputs = [
    ("Predicted vs Actuals", r"G:\ganga abc\Output\Jamun predicted_vs_actuals.xlsx"),
    ("Overall Jamun Prediction", r"G:\ganga abc\Output\Jamun Overall Jamun sales predicted.xlsx")
]

def run_dosa_prediction():
    os.system('jupyter nbconvert --to notebook --execute "Dosa Prediction.ipynb" --output "Dosa Prediction Output.ipynb"')

def run_sweet_prediction():
    os.system('jupyter nbconvert --to notebook --execute "sweet prediction.ipynb" --output "sweet prediction Output.ipynb"')

output_files = []

if process == "Dosa Prediction":
    run_dosa_prediction()
    output_files = dosa_outputs

elif process == "Sweet Prediction":
    run_sweet_prediction()
    output_files = sweet_outputs

if output_files:
    for label, path in output_files:
        st.subheader(label)
        if os.path.exists(path):
            df = pd.read_excel(path)
            st.dataframe(df)
            with open(path, "rb") as f:
                st.download_button(
                    label=f"Download {label}",
                    data=f,
                    file_name=os.path.basename(path),
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
        else:
            st.warning(f"{label} file not found: {os.path.basename(path)}")
elif process != "Select...":
    st.warning("Output files not found. Please make sure the notebook/script runs and generates the output.")