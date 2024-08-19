### Import libraries
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title("Masala Penguins 🐧")
st.image("penguins.png")
st.write("Hey yo we are the chatbot penguins")

st.markdown("---")
st.header("Hey yo we present the data here")

df = pd.read_csv("./data/penguins_pimped.csv")
df_sample = df.sample(5)

st.dataframe(df_sample)

st.subheader("Selecting an Island")

island = df['island'].unique()



### 2.2 Display the data for an island you choose from the dataframe 

my_island = st.selectbox(label="Select an Island?",options=island)

my_island_df = df[df['island'] == my_island]

if st.checkbox(label="But do you really want to see the dataframe? are you sure?"):
    st.dataframe(my_island_df)

st.write("---")
st.header("Yo Data Visualisation 📈")
st.subheader("Yo yo this is matplotlib vis chart")

fig, ax = plt.subplots()
ax = sns.scatterplot(
     data=df,
     x="bill_depth_mm",
     y="bill_length_mm",
     hue='species' # set to species
     )

st.pyplot(fig=fig)

st.subheader("Yo yo this is plotly vis chart")

figure = px.scatter(data_frame=df,
           x="bill_depth_mm",
           y="bill_length_mm",
           color='species',
           animation_frame="sex")

st.plotly_chart(figure)

st.balloons()