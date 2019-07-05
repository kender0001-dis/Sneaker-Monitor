import requests
from bs4 import BeautifulSoup
import pandas as pd
import psycopg2
import random
import datetime

# connecting to the database
conn = psycopg2.connect(dbname='sneakerdb', user='postgres', password = None)
cur = conn.cursor()
# cur.execute("USE sneakerdb")
random.seed(datetime.datetime.now())
def store(sneaker_title, sneaker_price, sneaker_image):
   cur.execute('INSERT INTO scrapy_tabe (title, price, image) VALUES (%s,%s,%s)', (sneaker_title, sneaker_price, sneaker_image))
   cur.connection.commit()

shoe_store_url = 'https://www.obeezi.com/sneakers?product_list_limit=120'

#Load html's plain data into a variable
plain_html_text = requests.get(shoe_store_url)

#parse the data
soup = BeautifulSoup(plain_html_text.text, 'lxml')
sneaker_containers = soup.find_all('div', class_='product-item-info', limit=4)

# Lists to store the scraped data in
sneaker_titles = []
sneaker_prices = []
sneaker_images = []
big_data = []

for sneaker in sneaker_containers:
    mini_dict = {}
    mini_dict['title'] = sneaker.strong.a.text.replace('\n', '')
    mini_dict['price'] = sneaker.find('span', class_='price').get_text()
    mini_dict['image'] = sneaker.find('img', class_='product-image-photo')['src']
    big_data.append(mini_dict)

print(big_data[0])

#store items into the database
for data in big_data:
    store(data['title'], data['price'], data['image'])


#optional: store data in pandas data frame
test_df = pd.DataFrame(
{
    'sneaker': sneaker_titles,
    'image_url': sneaker_images,
    'price': sneaker_prices,
})
print(test_df.info())
test_df
webhook = DiscordWebhook(url='your webhook url')

# create embed for webhook
embed = DiscordEmbed(title='REPLACE ME WITH PROPER TITLE', description='title, price, image_url', color=369824)

# add embed to webhook
webhook.add_embed(embed)

webhook.execute(ADD WEBHOOK HERE)

cur.close()
conn.close()
