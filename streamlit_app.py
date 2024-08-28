import streamlit as st
import pandas as pd
import numpy as np

st.title('🎈 My First Streamlit App')

# Generate some random data
data = pd.DataFrame({
    'x': range(1, 11),
    'y': np.random.randn(10)
})

# Display the data as a table
st.write("Here's our data:")
st.dataframe(data)

# Create a line chart
st.line_chart(data)
