import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import base64

# configuration
st.set_option('deprecation.showfileUploaderEncoding', False)

# title of the app
st.title("Life Insurance Analytics ")

# Add a sidebar
st.sidebar.image('corplogo.PNG', use_column_width=True)
st.sidebar.subheader("Visualization Settings")


# Setup file upload
uploaded_file = st.sidebar.file_uploader(
    label="Upload your CSV or Excel file. (200MB max)",
    type=['csv', 'xlsx', 'xls']
)


if uploaded_file is not None:
    try:
        if uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            data_types = {'Policy No': str}
            df = pd.read_excel(uploaded_file, dtype = data_types , header = 4)
                      
        elif uploaded_file.type == "text/csv":
            df = pd.read_csv(uploaded_file, header=4)
            
        
        df.dropna(subset=['Policy No'], inplace = True)
        

        df['Start Date'] = pd.to_datetime(df['Start Date'], format='%d/%m/%Y')

        # Change the format to year-month-day
        df['Start Date'] = df['Start Date'].dt.strftime('%Y-%m-%d')

        df['Start Date'] = pd.to_datetime(df['Start Date'])


        df['Maturity Date'] = pd.to_datetime(df['Maturity Date'], format='%d/%m/%Y')

        # Change the format to year-month-day
        df['Maturity Date'] = df['Maturity Date'].dt.strftime('%Y-%m-%d')

        df['Maturity Date'] = pd.to_datetime(df['Maturity Date'])

        #today = pd.Timestamp(datetime.today())
        today = datetime.today().strftime('%Y-%m-%d')
        df['Today'] = today
        df['Today'] = df['Today'].astype('datetime64[ns]')

        # Calculate the number of months
        df['nb_months'] = ((df['Today'] - df['Start Date']) / np.timedelta64(1, 'M')).astype(int)


        df["Monthly Premium"] = (df["Annual Premium"] / 12)

        df["Scheduled Payment(as at today)"] = df['Monthly Premium'] * df['nb_months']

        df["Premium Outstanding"] = df["Scheduled Payment(as at today)"] - df["Premium Received"]

        newdf["Maturity Date"].dt.year
        newdf['Maturity Year'] = newdf['Maturity Date'].dt.year
        
        newdf["Maturity Date"].dt.month_name()
        newdf['Maturity Month'] = newdf['Maturity Date'].dt.month_name()                                       
          
    except Exception as e:
        st.write("Error:", e)
        
        
# Define chart selection dropdown
chart_select = st.sidebar.selectbox(
            label="SELECT",
            options=["January 2023", "February 2023", "March 2023"]
        )

if uploaded_file is not None:
    if chart_select == "January 2023":
        # maturing in Jan 2023
        Jan = df[(df['Maturity Month'] == 'January') & (df['Maturity Year'] == 2023 )]
        Jan_number = len(Jan['Policy No'])

        # Select desired columns
        Jan = Jan.loc[:, ['Policy No', 'Insured', 'Status','Start Date', 'Maturity Date', 'Sum Insured', 'Premium Received']]
        Jan = Jan.to_html(index=False)
        # Add inline CSS to change font size
        Jan = Jan.replace('<table', '<table style="font-size: 11px;"')
       
       
        # Display the DataFrame
        st.subheader(f"First Maturity in January 2023")
        st.markdown (f"Total number of policies: **{Jan_number}**")
                     
        st.markdown(Jan, unsafe_allow_html=True)
               

    elif chart_select == "February 2023":
        # maturing in Feb
        Feb = df[(df['Maturity Month'] == 'February') & (df['Maturity Year'] == 2023 )]
        Feb_number = len(Feb['Policy No'])

        # Select desired columns
        Feb = Feb.loc[:, ['Policy No', 'Insured', 'Status','Start Date', 'Maturity Date', 'Sum Insured', 'Premium Received']]
        Feb = Feb.to_html(index=False)
        # Add inline CSS to change font size
        Feb = Feb.replace('<table', '<table style="font-size: 11px;"')
       
       
        # Display the DataFrame
        st.subheader(f"First Maturity in February 2023")
        st.markdown (f"Total number of policies: **{Feb_number}**")
                     
        st.markdown(Feb, unsafe_allow_html=True)
       
    elif chart_select == "March 2023":
        # maturing in March
        Mar = df[(df['Maturity Month'] == 'March') & (df['Maturity Year'] == 2023 )]
        Mar_number = len(Feb['Policy No'])

        # Select desired columns
        Mar = Mar.loc[:, ['Policy No', 'Insured', 'Status','Start Date', 'Maturity Date', 'Sum Insured', 'Premium Received']]
        Mar = Mar.to_html(index=False)
        # Add inline CSS to change font size
        Mar = Mar.replace('<table', '<table style="font-size: 11px;"')
       
       
        # Display the DataFrame
        st.subheader(f"First Maturity in March 2023")
        st.markdown (f"Total number of policies: **{Mar_number}**")
                     
        st.markdown(Mar, unsafe_allow_html=True)
       
    else:
        st.write("Failed to load data from the uploaded file.")
else:
    st.write("Please upload a file to visualize.")
