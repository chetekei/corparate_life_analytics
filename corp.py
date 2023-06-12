import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime
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
            df = pd.read_excel(uploaded_file, header=8)
        elif uploaded_file.type == "text/csv":
            df = pd.read_csv(uploaded_file, header=8)
                      

        # convert date column to month name
        df = df.iloc[1:]
        df['Month'] = pd.to_datetime(df['Loss Date']).dt.strftime('%B')
        df['Day'] = pd.to_datetime(df['Loss Date']).dt.day_name()
        df['Year'] = pd.to_datetime(df['Loss Date']).dt.year
        df.dropna(subset=['Claim No'], inplace=True)
        mask = df['Claim Type'].str.startswith('Work Injury')
        df.loc[mask, 'Claim Type'] = 'WIBA'

        df['Frequency'] = np.bool_(1)
        
        # convert timestamp to datetime
        df['timestamp'] = pd.to_datetime(df['Time of Loss'])

        # group by 3-hour intervals
        df['time_interval'] = pd.cut(df['timestamp'].dt.hour + df['timestamp'].dt.minute/60, 
                                     bins=np.arange(0, 24.01, 3), 
                                     labels=[f"{i:02d}:00-{i+2:02d}:59" for i in range(0, 24, 3)])
        grouped_data = df.groupby('time_interval').size().reset_index(name='count')

               
          
    except Exception as e:
        st.write("Error:", e)
