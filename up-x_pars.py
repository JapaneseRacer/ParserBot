from selenium import webdriver
import lxml
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import json

def get_data(url):
    s = Service(executable_path="./chromedriver.exe")
    driver = webdriver.Chrome(service=s)

    try:
        while True:
            driver.get(url)
            time.sleep(2)
            with open("index.html", "w", encoding="utf-8") as file:
                file.write(driver.page_source)
            with open("index.html", encoding="utf-8") as file:
                src = file.read()
            soup = BeautifulSoup(src, "lxml")
            items_list = soup.find("div", class_="history-block__mobile").find_all("div", class_="history-block__item")
            res_list = []
            for item in items_list:
                res = item.find("span").text
                res = res.replace(' ', '')
                res = res.replace('X', '')
                res_list.append(float(res))
            print(res_list)
            
            with open('new.json', 'w', encoding='utf-8') as f:
                json.dump(res_list, f, ensure_ascii=False, indent=4)
    
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

        

def main():
    get_data(url="https://up-x.luxe/games/crash")

if __name__ == "__main__":
    main()
