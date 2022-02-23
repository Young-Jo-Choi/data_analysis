from selenium import webdriver
from bs4 import BeautifulSoup as soups
import os
from tqdm import tqdm_notebook

# webdriver를 다운받은 뒤 경로를 올바로 설정하시오.
driver_path = 'C:/Users/Choi/Desktop/jupyter/chromedriver.exe'

def search_selenium(search_name, search_limit) :
    search_url = "https://www.google.com/search?q=" + str(search_name) + "&hl=ko&tbm=isch"
    
    browser = webdriver.Chrome(driver_path)
    browser.get(search_url)    

    browser.implicitly_wait(2)
    
    # 경로를 올바로 설정하시오.
    if os.path.isdir("images/"+search_name)==False:
        os.makedirs("images/"+search_name)
        
    for i in range(search_limit) :
        try:
            image = browser.find_elements_by_tag_name("img")[i]
            # 경로를 올바로 설정하시오.
            temp_str = str("C:/Users/Choi/Desktop/jupyter/images/"+search_name +'/'+ str(i) + ".png")
            image.screenshot(temp_str)
        except:
            pass

    browser.close()
    
if __name__ == '__main__':
    search_list1 = ['CRH5','itx-새마을','KTX','mugunghwa','Railjet','SRT','TGV','신칸센','증기기관','지하철']
    search_list2 = ['alligator', 'ball', 'car', 'cat', 'dog', 'shoes', 'tank', 'tiger']

    for equip_name in tqdm_notebook(search_list1):
        search_name = equip_name
        search_limit = 500
        #search_maybe(search_name, search_limit)
        search_selenium(search_name, search_limit)

