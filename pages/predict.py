### Import libraries
import pickle
import streamlit as st
import pandas as pd

st.title("How light are the chatbot penguins? 🐧")
# Load the model model_penguins.pkl
with open('./pages/model_penguins.pkl', 'rb') as file:
     model = pickle.load(file)

# Task2:
# Set the value of flipper_length to a number between 160 and 240
flipper_lenght = st.sidebar.slider(label="yo choose a flipper lenght?",
                           min_value= 160,
                           max_value=200,
                           step=10
                        )

# Set the value of species to one of the possible options 'Adelie','Chinstrap','Gentoo'
species = st.sidebar.selectbox(label='yo choose a species',
                               options=['Adelie','Chinstrap','Gentoo'])

# Set the value of sex to 'Female' or 'Male'
sex = st.sidebar.selectbox(label='yo choose a sex',
                               options=['Male','Female'])

# Task3:
# Let's create a dictionary having as keys the input features 
# (see initial doc string at the top) 
# and corresponding values the one we have set just above
input_dict_X = {'flipper_length_mm': flipper_lenght, 'species': species, 'sex': sex
}
print(input_dict_X)

# Task4:
# create a dataframe from the input_dict_X 
input_X = pd.DataFrame(input_dict_X, index = ['new_index'])

# Task5:
# make prediction with the model


if st.button("Please click this to get prediction"):
    # Make prediction
    y_pred = model.predict(input_X)
    # Display the prediction below the button
    st.write(f'The predicted weight is: {y_pred[0]}')







