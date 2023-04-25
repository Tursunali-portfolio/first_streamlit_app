import os
from PIL import Image
import requests
from io import BytesIO

import snowflake.connector
import streamlit


conn = snowflake.connector.connect(**streamlit.secrets["snowflake_zena"])

with conn.cursor() as cursor:
  cursor.execute("SELECT * FROM ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE;")
  data = cursor.fetch_pandas_all()

sweatsuit_list = data.set_index('COLOR_OR_STYLE')

streamlit.dataframe(sweatsuit_list.index)

selected_suits = streamlit.selectbox('Pick a sweatsuit color or style:', list(sweatsuit_list.index), ["Pink"])

# streamlit.dataframe(sweatsuit_list.loc[selected_suits])
