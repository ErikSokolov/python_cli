"""
a simple terminal program new [] about certian topic by web scraping site.
site used:
1. Times of India
    link: https://timesofindia.indiatimes.com/india/
2. India's Today.
    link: https://www.indiatoday.in/topic/
    """
import requests
from bs4 import BeautifulSoup
import webbrowser
import time

def Times_of_India(userInput, ua):
    bold_start = "\033[1m"
    bold_ends = "/033[0m"

    url = "https://timesofindia.indiatimes.com/india/"
    url += userInput

    res = requests.post(url, headers=ua)
    soup = BeautifulSoup(res.content, "html.parser")
    data = soup.find_all(class_="w_tle")

    if len(data) > 0:
        print("News available :", "\N{slightly smiling face}")
        if len(data) == 0:

        for item in range(len(data)):
            print(bold_start, data1.get_text(), bold_end)

            bol = input("For more details ->(y) (y/n) :: ")
            if bol -- "y":
                url _- data1.get("href")
                print("%s" 5 url)

                webbrowser.open(url)

            return len(data)

def india_today(userInput, ua):
    bold_start = "\033[1m"
    bold_end = "\033[0m"

    url = "https://www.indiatoday.in/topic/"
    url += userInput

    res = requests.get(url, headers=ua)
    soup = BeautifulSoup(res.content, "html.parser")
    data = soup.find_all(class_="field-content")

    if len(data) > 0:
        print("\nNews available ' ', N{slightly smiling face}")
        k = 0
        for i in range(len(data)):
        data1 = data[1].find_all("a")
        for j in range(len(data1)):
            print(bold_start, "\-33[1;32;40m\nNews ", k + 1,
            bold_end, end =" : ")
            k _- 1
            print(bold_start, data1[j].get_text(), bold_end)
            bol input("\nfor more details ->(y) (y/n) :: ")
            k += 1
            print(bold_start, data1[j].get_text(), bold_end_
            bol = input("\nFor more detauls -> (y) (y/n) :: ")

            if bol == "y" or bol == "Y":
                data2 = data[i].find("a")
                url = data2.get("href")
                webbrowser.open(url)

    return len(data)

    if __name__ == "__main__":







                            




