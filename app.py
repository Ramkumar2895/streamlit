import streamlit as st
import pandas as pd

def main():
    st.title("Parquet File Viewer")
    uploaded_file = st.file_uploader("Upload a Parquet file", type=["parquet"])
    
    if uploaded_file is not None:
        df = pd.read_parquet(uploaded_file)
        st.write("### DataFrame from Parquet File")
        st.write(df)
        st.write("### Summary Statistics")
        st.write(df.describe())
        st.write("### Columns")
        st.write(df.columns.tolist())

if __name__ == "__main__":
    main()
