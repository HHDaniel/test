#import std libraries
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st 
import seaborn as sns
import plotly.express as px

choice = st.sidebar.radio('Hope this was intersting',['yes','no'])
if choice == 'yes':
    # Write a title
    st.title('Penguin explorer')
    # Write data taken from https://allisonhorst.github.io/palmerpenguins/
    st.write('**Little** *app* for exploring `penguin` [datset](https://allisonhorst.github.io/palmerpenguins/)')
    # Put image https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/man/figures/lter_penguins.png
    st.image('https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/man/figures/lter_penguins.png')

    # Write heading for Data
    st.header('Data')
    # Read csv file and output a sample of 20 data points
    df =pd.read_csv('penguins_extra.csv')
    st.write('Display a sample of data points from `penguins dataset`',df.sample(20))
    # to upload csv files
    file =  st.file_uploader('Upload a file')
    file = pd.read_csv(file)
    st.write(file.head())
    # Add a selectbox for species
    species = st.selectbox('Choose which species to display',df.species.unique())
    df_species = df.loc[df.species==species]
    # Display a sample of 20 data points according to the species selected with corresponding title
    st.write(f'Displaying subset for {species} penguins',df_species.sample(20))
    # Plotting seaborn
    st.subheader('Plotting')
    fig,ax = plt.subplots()
    ax = sns.scatterplot(data=df, x='bill_length_mm',y='bill_depth_mm',hue='species',size='sex')
    st.pyplot(fig)

    # Plotting plotly
    st.subheader('Creating interactive plots with plotly')
    fig = px.scatter(df, x ='bill_length_mm',y='flipper_length_mm',color='species',animation_frame='species',hover_name='name',range_x=[30,70],range_y=[150,300])
    st.plotly_chart(fig)
    # Bar chart count of species per island
    st.bar_chart(df.groupby('species')['island'].count())
    # Maps
    st.map(df)
    # Reference https://deckgl.readthedocs.io/en/latest/
    st.write('If you are interested to explore mapping checkout [pydeck](https://deckgl.readthedocs.io/en/latest/)')
    # sidebar comment

    name = st.text_input('Write name')
    st.write(name)
else:
    st.write('select yess')