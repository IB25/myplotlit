# Streamlit live coding script
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy


# First some MPG Data Exploration
@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    return df


mpg_df_raw = load_data(path="mpg.csv")
mpg_df = deepcopy(mpg_df_raw)

# Add title and header
st.title("Introduction to Streamlit")
st.header("MPG Data Exploration")

st.dataframe(data=mpg_df)

plot_type=st.radio("Choose Plot Type", ["Matplotlib", "Plotly"])
# scatter plot of displ vs bwyfor year = 2008
# matplotlib

# In Matplotlib
if plot_type=="Matplotlib":
    m_fig, ax = plt.subplots(figsize=(10, 8))
    ax.scatter(mpg_df.loc[mpg_df['year']== 2008, 'displ'], 
                        mpg_df.loc[mpg_df['year']== 2008, 'hwy'], alpha=0.7)
    ax.set_title("Engine Size vs. Higway Fuel Mileange")
    ax.set_xlabel('Displacement (Liters)')
    ax.set_ylabel('MPG')

    st.pyplot(m_fig)



if plot_type=="Plotly":

    # In Plotly
    p_fig = px.scatter(mpg_df, x='displ', y='hwy', opacity=0.5,
                    range_x=[1, 8], range_y=[10, 50],
                    width=750, height=600,
                    labels={"displ": "Displacement (Liters)",
                            "hwy": "MPG"},
                    title="Engine Size vs. Highway Fuel Mileage")
    p_fig.update_layout(title_font_size=22)

    st.plotly_chart(p_fig)