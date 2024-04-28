from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import tkinter as tk
from tkinter import filedialog
from time import sleep

import winsound
from tqdm import tqdm

frequency  = 2000
duration  = 2000


# Opening the filename  
file_name = filedialog.askopenfile()

print("File Loaded : " + str(file_name.name))



loaded_rollnumbers  = []

readfile  = open(file_name.name , 'r')
line  = readfile.readline()

while True:
    
    # Get next line from file
    line = readfile.readline()
    # if line is empty
    # end of file is reached
    if not line:
        break
    loaded_rollnumbers.append(line)

print("File checked for Browser :  Total Count is : ")
print(len(loaded_rollnumbers))
print("Expected time to complete : " +  str(len(loaded_rollnumbers) / 6) + " Minutes")
print("Expected time to complete : " +  str(len(loaded_rollnumbers) / 360) + " Hours")
print("Expected time to complete : " +  str(len(loaded_rollnumbers) / 8640) + " Days")


# Make the bnowser and maximize it : But Before that wait for 21 seconds : 
sleep(2)


# Make the browser and maximize it 
options = webdriver.FirefoxOptions()
driver  = webdriver.Firefox()
driver.maximize_window()


print("Starting the Scrapping")



base_url = "https://result.mdurtk.in/postexam/result.aspx"



def checking_website(base_url):
    
    length  = len(loaded_rollnumbers)
    count  = 0
    for i in tqdm(range(length)):

        for each in loaded_rollnumbers:
            try:
                driver.get(base_url)
                driver.title == "Maharshi Dayanand University, Rohtak"
                registration  = driver.find_element(By.ID , "txtRegistrationNo")
                registration.send_keys("1171530224")
                roll_number  = driver.find_element(By.ID , "txtRollNo")
                roll_number.send_keys(each)
                proceed_button  = driver.find_element(By.ID , "cmdbtnProceed")
                proceed_button.click()
                sleep(2)
                try:
                        mobile_number  = driver.find_element(By.ID , "txtMobileNo")
                        mobile_number_confirmation  = driver.find_element(By.ID , "txtMobileNoCon")
                        email_id_confirmation  = driver.find_element(By.ID , "txtEMail")
                        confirm_click = driver.find_element(By.ID , "imgComfirm" )
                        mobile_number.send_keys("9650849971")
                        mobile_number_confirmation.send_keys("9650849971")
                        email_id_confirmation.send_keys("vinaypant24@gmail.com")
                        confirm_click.click()
                except:
                    None

                # This part will check if the page has the result or not : 
                try:
                    image_confirm  = driver.find_element(By.ID , "imgComfirm")
                    image_confirm.click()
                    with open('saved_rollnumber.txt', 'a') as file: file.write(each)
                except:
                    None

                # Check if the count is in 100's then save the data in another text file :
                count+=1 
                if count % 100:
                    for each in loaded_rollnumbers:
                        with open('saved_rollnumber.txt', 'a') as file: file.write(each)


            except:
                winsound.Beep(frequency , duration)
                loaded_rollnumbers.pop(0)
                checking_website(base_url)
            




checking_website(base_url)

