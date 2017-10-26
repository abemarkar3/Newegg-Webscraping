from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup



#Choosing a url
my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'
print(my_url)

# grabbing the page
uClient = uReq(my_url)

# storing read data in a variable
page_html = uClient.read()

# closing the connection between console and url server or else console will crash
uClient.close()

# Parsing html data
page_soup = soup(page_html, 'html.parser')

#grabs product reference from line
containers = page_soup.findAll('div', {'class':'item-container'})

print("There are {} {}".format(len(containers), 'graphics cards'))

filename = 'output.csv'
f = open(filename, 'w')

headers = "brand, product_name, price\n"

f.write(headers)

for container in containers:
    priceContainer = container.findAll("li", {"class":"price-current"})
    priceContainer = priceContainer[0]

    brand = container.div.div.a.img["title"]
    product = container.img["alt"]
    price = priceContainer.strong.string
    price = '$'+price

    f.write(brand.replace(',',"|") + "," + product.replace(',',"|") + "," + price.replace(',',"") + "\n")

f.close()
