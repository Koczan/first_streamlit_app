import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit') 

streamlit.title('My parents new healthy Diner');

streamlit.header('Breakfast Favorites');
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal');
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie');
streamlit.text('🐔 Hard-Boiled Free-Range Egg');
streamlit.text('🥑🍞 Avocado Toast');

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇');
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries']);
fruits_to_show = my_fruit_list.loc[fruits_selected];

# Display the table on the page.
# streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)

# new section to display fruityvice api details
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized);

# dont run anything past here while we troubleshoot
streamlit.stop();

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)

fruit_choice = streamlit.text_input("What fruit would you like to add?", "jackfruit");
streamlit.text("Thanks for adding " + fruit_choice);

#this will not work correctly, but just go with it for now
my_cur.execute("insert into fruit_load_list values ('from streamlit')");


# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
#streamlit.write('The user entered ', fruit_choice)
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# streamlit.text(fruityvice_response.json())

# normalize JSON
# fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# show table using pandas
#streamlit.dataframe(fruityvice_normalized)
