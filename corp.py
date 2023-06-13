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

        # Get the current date and calculate the date 30 days ahead
        thirty_days =  df['Today'] + timedelta(days=30)
        #get one entry from the thirty days column
        thirty = thirty_days[5].date()
        long_date_thirty = thirty.strftime("%A, %B %d, %Y")
        df['Thirty'] = thirty_days
        df['Thirty'] = df['Thirty'].astype('datetime64[ns]')

        sixty_days =  df['Today'] + timedelta(days=60)
        #get one entry from the sixty days column
        sixty = sixty_days[5].date()
        long_date_sixty = sixty.strftime("%A, %B %d, %Y")
        df['Sixty'] = sixty_days
        df['Sixty'] = df['Sixty'].astype('datetime64[ns]')

        ninety_days =  df['Today'] + timedelta(days=90)
        #get one entry from the ninety days column
        ninety = ninety_days[5].date()
        long_date_ninety = ninety.strftime("%A, %B %d, %Y")
        df['Ninety'] = ninety_days
        df['Ninety'] = df['Ninety'].astype('datetime64[ns]')                                        
          
    except Exception as e:
        st.write("Error:", e)
        
        
# Define chart selection dropdown
chart_select = st.sidebar.selectbox(
            label="SELECT",
            options=["Output as per the filtered dates", "Maturity in next 30 days", "Maturity in next 60 days", "Maturity in next 90 days"]
        )

if uploaded_file is not None:
    if chart_select == "Maturity in next 30 days":
        # maturing in the next thirty days
        Matured_policies_30 = df[(df['Maturity Date'] >= df['Today']) & (df['Maturity Date'] <= df['Thirty'])]
        number_30 = len(Matured_policies_30['Policy No'])

        # Select desired columns
        Matured_policies_30 = Matured_policies_30.loc[:, ['Policy No', 'Insured', 'Status','Start Date', 'Maturity Date', 'Sum Insured', 'Premium Received']]
        Matured_policies_30 = Matured_policies_30.to_html(index=False)
       
       
        # Display the DataFrame
        st.subheader(f"First Maturity in 30 days as from today to {long_date_thirty}")
        st.markdown (f"Total number of policies: **{number_30}**")
                     
        st.markdown(Matured_policies_30, unsafe_allow_html=True)
               

    elif chart_select == "Maturity in next 60 days":
        # maturing in the next thirty days
        Matured_policies_60 = df[(df['Maturity Date'] >= df['Today']) & (df['Maturity Date'] <= df['Sixty'])]
        number_60 = len(Matured_policies_60['Policy No'])

        # Select desired columns
        Matured_policies_60 = Matured_policies_60.loc[:, ['Policy No', 'Insured', 'Status', 'Start Date', 'Maturity Date', 'Sum Insured', 'Premium Received']]
        Matured_policies_60 = Matured_policies_60.to_html(index=False)
       
        # Display the DataFrame
        st.subheader(f"First Maturity in 60 days as from today to {long_date_sixty}")
        st.markdown (f"Total number of policies: **{number_60}**")
       
        st.markdown(Matured_policies_60,unsafe_allow_html=True )
       
    elif chart_select == "Maturity in next 90 days":
        # maturing in the next thirty days
        Matured_policies_90 = df[(df['Maturity Date'] >= df['Today']) & (df['Maturity Date'] <= df['Ninety'])]
        number_90 = len(Matured_policies_90['Policy No'])

        # Select desired columns
        Matured_policies_90 = Matured_policies_90.loc[:, ['Policy No', 'Insured', 'Status', 'Start Date', 'Maturity Date', 'Sum Insured', 'Premium Received']]
        Matured_policies_90 = Matured_policies_90.to_html(index=False)
       
        # Display the DataFrame
        st.subheader(f"First Maturity in 90 days as from today to {long_date_ninety}")
        st.markdown (f"Total number of policies: **{number_90}**")
               
        st.markdown(Matured_policies_90, unsafe_allow_html=True )
       
    else:
        st.write("Failed to load data from the uploaded file.")
else:
    st.write("Please upload a file to visualize.")
