import requests
from bs4 import BeautifulSoup
import smtplib
import time
# from smtplib import server

URL = "https://www.amazon.in/gp/product/B0BY8JZ22K/ref=s9_acss_bw_cg_Budget_8a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-11&pf_rd_r=552BCYPBDSWSJB919APR&pf_rd_t=101&pf_rd_p=8b5f405a-ce96-4204-8621-43118626b3ad&pf_rd_i=1389401031&th=1"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62"}
Required_price = 20000
EMAIL_ADDRESS = "unknowngotknown1@gmail.com"
TO_EMAIL = "iit2020065@iiita.ac.in"



def compare():
    price = int(TitlePrice())
    if price >= Required_price:
        diff = price - Required_price
        print("the price is still expensive")

        # @app.route("/")
        # def hello():
        #     return "Mail has not been sent"

        # hello()
        # print(f"the required price is still {}".format(diff))
    else:
        print("the price of the product is cheaper now ... Hurry Up !!!")
        sendmail()

        # @app.route("/")
        # def hello():
        #     return "Check your mailBox"

        # hello()


def TitlePrice():
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, "html.parser")  # Corrected parser type
    title = soup.find(id="productTitle").get_text().strip()
    price_element = soup.find('span', {'class': 'a-price-whole'})  # Find the span with class 'a-price-whole'
    price = 0
    if price_element:
        price_text = price_element.get_text().replace('₹', '').replace(',', '').replace('.', '')  # Remove currency symbol and commas
        price = float(price_text)  # Convert cleaned price text to float
        # print(f"Price: ₹{price:.2f}")
        # print(f"Price: ₹{price}")
        return price
    else:
        print("Price not found.")
        price = -1;
        # return None
    # price = soup.find(classmethod="a-price-whole").get_text().strip()  # Use the correct ID for price
    print(title)
    print(price)
    return price


def sendmail():
    subject = f"Hey there bud!! The price has been dropped for {URL}... Hurry up!!!"
    body = "subject:" + subject + '\n\n' + URL
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls() 
    server.login(EMAIL_ADDRESS, 'zhcdprqzcuamxqkt')   
    server.sendmail(EMAIL_ADDRESS, TO_EMAIL, body)
    print("mail sent successfully")
    pass
# TitlePrice()


if __name__ == "__main__":
    # app.run()
    while True:
        compare()
        time.sleep(40)