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

selected_suit = streamlit.selectbox('Pick a sweatsuit color or style:', sweatsuit_list.index)

df= sweatsuit_list.loc[selected_suit]

url = df.DIRECT_URL

response = requests.get(url)

image = Image.open(BytesIO(response.content))

streamlit.image(image=image)

streamlit.write('Price: ', df.PRICE)
streamlit.write('Sizes Available: ', df.SIZE_LIST)
streamlit.write(df.UPSELL_PRODUCT_DESC)
