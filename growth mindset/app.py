from io import BytesIO
import streamlit as st
import pandas as pd
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Setup
st.set_page_config(page_title="Data Sweeper", layout='wide')
st.title("Data Sweeper")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization!")

uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        # Process each file separately
        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file type: {file_ext}")
            continue  # Skip unsupported files
        
        # Display the dataframe
        st.write(f"### 📂 File Name: {file.name}")
        st.write(f"👕 **File Size:** {file.size / 1024:.2f} KB")
        st.write("Preview the head of the Dataframe")
        st.dataframe(df.head())

        # Summary Report
        st.subheader("📊 Data Summary Report")
        st.write(f"**Total Rows:** {df.shape[0]}")
        st.write(f"**Total Columns:** {df.shape[1]}")
        st.write(f"**Missing Values:** {df.isnull().sum().sum()}")
        st.write(f"**Duplicate Rows:** {df.duplicated().sum()}")

        # Options for data cleaning
        st.subheader("Data Cleaning Options")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("✅ Duplicates Removed!")

            with col2:
                if st.button(f"Fill Missing Values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())        
                    st.write("✅ Missing Values Filled!")

            st.subheader("Select Columns to Convert")
            columns = st.multiselect(f"Choose Columns for {file.name}", df.columns, default=df.columns)
            df = df[columns]

        # Convert the File CSV to Excel
        st.subheader("Conversion Options")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=str(hash(file.name)))

        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()

            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"
            elif conversion_type == "Excel":
                df.to_excel(buffer, index=False, engine='xlsxwriter')
                file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

            buffer.seek(0)

            # Download Button
            st.download_button(
                label=f"Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )

        # Generate PDF Report
        def generate_pdf_report(data, file_name):
            buffer = BytesIO()
            c = canvas.Canvas(buffer, pagesize=letter)
            c.drawString(100, 750, f"Data Cleaning Report for {file_name}")
            c.drawString(100, 730, f"Total Rows: {data.shape[0]}")
            c.drawString(100, 710, f"Total Columns: {data.shape[1]}")
            c.drawString(100, 690, f"Missing Values: {data.isnull().sum().sum()}")
            c.drawString(100, 670, f"Duplicate Rows: {data.duplicated().sum()}")
            c.showPage()
            c.save()
            buffer.seek(0)
            return buffer

        if st.button(f"Generate Cleaning Report (PDF) for {file.name}"):
            pdf_report = generate_pdf_report(df, file.name)
            st.download_button(
                label="Download Cleaning Report",
                data=pdf_report,
                file_name=f"Cleaning_Report_{file.name}.pdf",
                mime="application/pdf"
            )

    st.success("✅ All Files Processed!")

