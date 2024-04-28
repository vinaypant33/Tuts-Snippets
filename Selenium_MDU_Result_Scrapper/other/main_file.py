from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()  # Chrome to be used for navigation  : 



'''
steps in the exec


'''



def visit_page(url):
    driver.get(url = url)
    input("")







if __name__ == '__main__':

    # url_name  = input("Paste the Url of the Website : ")
    visit_page(url="https://result.mdurtk.in/postexam/result.aspx")