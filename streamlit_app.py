import pandas
import streamlit
import requests

streamlit.title('My Hotel App Website')

streamlit.header('Breakfast Menu')

streamlit.text('Chicken Biryani £10.00')
streamlit.text('Mutton Biryani £15.00')
streamlit.text('FIsh Biryani £20.00')
streamlit.text('Tarang Special Biryani £50.00')


streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')



streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected] 

streamlit.dataframe(fruits_to_show)


streamlit.header('Fruity Vice Fruit Advise')
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())





