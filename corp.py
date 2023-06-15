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
        df['Policy Months to date'] = ((df['Maturity Date'] - df['Start Date']) / np.timedelta64(1, 'M')).astype(int)
        df["Monthly Premium"] = (df["Annual Premium"] / 12)
        df["Units Paid"] = df["Premium Received"]/df["Monthly Premium"]
        df["Units Outstanding"] = df['Policy Months to date'] - df["Units Paid"]        
        df["Expected Payment(as at today)"] = df['Monthly Premium'] * df['Policy Months to date']        
        df["Premium Outstanding"] = df["Expected Payment(as at today)"] - df["Premium Received"]     

       
        
        df['Maturity Year'] = df['Maturity Date'].dt.year       
       
        df['Maturity Month'] = df['Maturity Date'].dt.month_name()                                       
          
    except Exception as e:
        st.write("Error:", e)
        
        
# Define chart selection dropdown
chart_select = st.sidebar.selectbox(
            label="SELECT",
            options=["January 2023", "February 2023", "March 2023", "April 2023", "May 2023", "June 2023", "July 2023", "August 2023", "September 2023", "October 2023", "November 2023", "December 2023"]
        )

if uploaded_file is not None:
    if chart_select == "January 2023":
        # maturing in Jan 2023
        Jan = df[(df['Maturity Month'] == 'January') & (df['Maturity Year'] == 2023 )]
        Jan_number = len(Jan['Policy No'])

        # Select desired columns
        Jan = Jan.loc[:, ['Policy No', 'Insured', 'Status','Start Date', 'Maturity Date', 'Sum Insured', 'Premium Received', 'Units Paid', 'Units Outstanding']]
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
        Feb = Feb.loc[:, ['Policy No', 'Insured', 'Status','Start Date', 'Maturity Date', 'Sum Insured', 'Premium Received', 'Units Paid', 'Units Outstanding']]
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
        Mar_number = len(Mar['Policy No'])

        # Select desired columns
        Mar = Mar.loc[:, ['Policy No', 'Insured', 'Status','Start Date', 'Maturity Date', 'Sum Insured', 'Premium Received', 'Units Paid', 'Units Outstanding']]
        Mar = Mar.to_html(index=False)
        # Add inline CSS to change font size
        Mar = Mar.replace('<table', '<table style="font-size: 11px;"')
       
       
        # Display the DataFrame
        st.subheader(f"First Maturity in March 2023")
        st.markdown (f"Total number of policies: **{Mar_number}**")                     
        st.markdown(Mar, unsafe_allow_html=True)

    elif chart_select == "April 2023":
        # maturing in April
        Apr = df[(df['Maturity Month'] == 'April') & (df['Maturity Year'] == 2023 )]
        Apr_number = len(Apr['Policy No'])

        # Select desired columns
        Apr = Apr.loc[:, ['Policy No', 'Insured', 'Status','Start Date', 'Maturity Date', 'Sum Insured', 'Premium Received','Units Paid', 'Units Outstanding']]
        Apr = Apr.to_html(index=False)
        # Add inline CSS to change font size
        Apr = Apr.replace('<table', '<table style="font-size: 11px;"')
       
       
        # Display the DataFrame
        st.subheader(f"First Maturity in April 2023")
        st.markdown (f"Total number of policies: **{Apr_number}**")                     
        st.markdown(Apr, unsafe_allow_html=True)

    elif chart_select == "May 2023":
        # maturing in May
        May = df[(df['Maturity Month'] == 'May') & (df['Maturity Year'] == 2023 )]
        May_number = len(May['Policy No'])

        # Select desired columns
        May = May.loc[:, ['Policy No', 'Insured', 'Status','Start Date', 'Maturity Date', 'Sum Insured', 'Premium Received','Units Paid', 'Units Outstanding']]
        May = May.to_html(index=False)
        # Add inline CSS to change font size
        May = May.replace('<table', '<table style="font-size: 11px;"')
       
       
        # Display the DataFrame
        st.subheader(f"First Maturity in May 2023")
        st.markdown (f"Total number of policies: **{May_number}**")                     
        st.markdown(May, unsafe_allow_html=True)

    elif chart_select == "June 2023":
        # maturing in June
        Jun = df[(df['Maturity Month'] == 'June') & (df['Maturity Year'] == 2023 )]
        Jun_number = len(Jun['Policy No'])

        # Select desired columns
        Jun = Jun.loc[:, ['Policy No', 'Insured', 'Status','Start Date', 'Maturity Date', 'Sum Insured', 'Premium Received', 'Policy Months to date', 'Units Paid', 'Units Outstanding']]
        Jun = Jun.to_html(index=False)
        # Add inline CSS to change font size
        Jun = Jun.replace('<table', '<table style="font-size: 11px;"')
       
       
        # Display the DataFrame
        st.subheader(f"First Maturity in June 2023")
        st.markdown (f"Total number of policies: **{Jun_number}**")                     
        st.markdown(Jun, unsafe_allow_html=True)

    elif chart_select == "July 2023":
        # maturing in July
        Jul = df[(df['Maturity Month'] == 'July') & (df['Maturity Year'] == 2023 )]
        Jul_number = len(Jul['Policy No'])

        # Select desired columns
        Jul = Jul.loc[:, ['Policy No', 'Insured', 'Status','Start Date', 'Maturity Date', 'Sum Insured', 'Premium Received', 'Units Paid', 'Units Outstanding']]
        Jul = Jul.to_html(index=False)
        # Add inline CSS to change font size
        Jul = Jul.replace('<table', '<table style="font-size: 11px;"')
       
       
        # Display the DataFrame
        st.subheader(f"First Maturity in July 2023")
        st.markdown (f"Total number of policies: **{Jul_number}**")                     
        st.markdown(Jul, unsafe_allow_html=True)

    elif chart_select == "August 2023":
        # maturing in August
        Aug = df[(df['Maturity Month'] == 'August') & (df['Maturity Year'] == 2023 )]
        Aug_number = len(Aug['Policy No'])

        # Select desired columns
        Aug = Aug.loc[:, ['Policy No', 'Insured', 'Status','Start Date', 'Maturity Date', 'Sum Insured', 'Premium Received', 'Units Paid', 'Units Outstanding']]
        Aug = Aug.to_html(index=False)
        # Add inline CSS to change font size
        Aug = Aug.replace('<table', '<table style="font-size: 11px;"')
       
       
        # Display the DataFrame
        st.subheader(f"First Maturity in August 2023")
        st.markdown (f"Total number of policies: **{Aug_number}**")                     
        st.markdown(Aug, unsafe_allow_html=True)

    elif chart_select == "September 2023":
        # maturing in September
        Sep = df[(df['Maturity Month'] == 'September') & (df['Maturity Year'] == 2023 )]
        Sep_number = len(Sep['Policy No'])

        # Select desired columns
        Sep = Sep.loc[:, ['Policy No', 'Insured', 'Status','Start Date', 'Maturity Date', 'Sum Insured', 'Premium Received', 'Units Paid', 'Units Outstanding']]
        Sep = Sep.to_html(index=False)
        # Add inline CSS to change font size
        Sep = Sep.replace('<table', '<table style="font-size: 11px;"')
       
       
        # Display the DataFrame
        st.subheader(f"First Maturity in September 2023")
        st.markdown (f"Total number of policies: **{Sep_number}**")                     
        st.markdown(Sep, unsafe_allow_html=True)

    elif chart_select == "October 2023":
        # maturing in October
        Oct = df[(df['Maturity Month'] == 'October') & (df['Maturity Year'] == 2023 )]
        Oct_number = len(Oct['Policy No'])

        Oct = Oct.loc[:, ['Policy No', 'Insured', 'Status','Start Date', 'Maturity Date', 'Sum Insured', 'Premium Received', 'Units Paid', 'Units Outstanding']]
        Oct = Oct.to_html(index=False)
        # Add inline CSS to change font size
        Oct = Oct.replace('<table', '<table style="font-size: 11px;"')
        
         # Display the DataFrame
        st.subheader(f"First Maturity in October 2023")
        st.markdown (f"Total number of policies: **{Oct_number}**")                     
        st.markdown(Oct, unsafe_allow_html=True)

    elif chart_select == "November 2023":
        # maturing in November
        Nov = df[(df['Maturity Month'] == 'November') & (df['Maturity Year'] == 2023 )]
        Nov_number = len(Nov['Policy No'])

        # Select desired colum
        Nov = Nov.loc[:, ['Policy No', 'Insured', 'Status','Start Date', 'Maturity Date', 'Sum Insured', 'Premium Received', 'Units Paid', 'Units Outstanding']]
        Nov = Nov.to_html(index=False)
        # Add inline CSS to change font size
        Nov = Nov.replace('<table', '<table style="font-size: 11px;"')
        
         # Display the DataFrame
        st.subheader(f"First Maturity in November 2023")
        st.markdown (f"Total number of policies: **{Nov_number}**")                     
        st.markdown(Nov, unsafe_allow_html=True)

    elif chart_select == "December 2023":
        # maturing in December
        Dec = df[(df['Maturity Month'] == 'December') & (df['Maturity Year'] == 2023 )]
        Dec_number = len(Dec['Policy No'])

        # Select desired column       
        Dec = Dec.loc[:, ['Policy No', 'Insured', 'Status','Start Date', 'Maturity Date', 'Sum Insured', 'Premium Received', 'Units Paid', 'Units Outstanding']]
        Dec = Dec.to_html(index=False)
        
        # Add inline CSS to change font size
        Dec = Dec.replace('<table', '<table style="font-size: 11px;"')
        
         # Display the DataFrame
        st.subheader(f"First Maturity in December 2023")
        st.markdown (f"Total number of policies: **{Dec_number}**")                     
        st.markdown(Dec, unsafe_allow_html=True)

    else:
        st.write("Failed to load data from the uploaded file.")

else:
    st.write("Please upload a file to visualize.")
