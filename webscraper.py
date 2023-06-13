# import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions  as EC
from dotenv import load_dotenv
load_dotenv()   
import os

#poti sa stergi chestiile de dupa egaluri si doar sa-ti pui tu acolo ce trebuie, nu tre sa ai traba cu env variables
url= os.getenv("URL")
inviteCode = os.getenv("CODE")
email  = os.getenv("EMAIL")
password = os.getenv("PASSWORD")



options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--user-data-dir=/Users/viktorashi/Library/Application Support/Google/Chrome/")
options.add_argument('--profile-directory=Profile 1')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


#asta de jos de deprecated
# driver = webdriver.Chrome(executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", options=options)


def iaBiletlol(w):
    w.get(url)
    try:
        #COCKies
    
        w.find_element('xpath', '//*[@id="cp-yes"]/a').click()
    except:
        pass
    #apasa sa deschizi casuta in care sa bagi codul
    w.find_element('xpath', '/html/body/div[1]/div[2]/div[3]/div[1]/div/form/div[3]/div[3]/div[1]/div/div[1]/a').click()
    #dai click pe ea si scrii codu
    try:
        #cred ca e interacitibl da nu detecteaza chestia asta deci pot doar sa-l fac sa dea click pe el daca il vede doar
        WebDriverWait(w, 10).until(EC.visibility_of_element_located(('xpath',  '//*[@id="BookingHandler_voucherCode"]'))).click()
    except:
        WebDriverWait(w, 10).until(EC.visibility_of_element_located(('xpath',  '/html/body/div[1]/div[2]/div[3]/div[1]/div/form/div[3]/div[3]/div[1]/div/div[1]/a'))).click()
        print('nu a mers clickul pe casuta')
        
    
    w.find_element('xpath', '//*[@id="BookingHandler_voucherCode"]').send_keys(inviteCode)
    #il trimiti sa ti-l verifice
    w.find_element('xpath', '//*[@id="orderForm"]/div[3]/div[3]/div[1]/div/div[2]/div/span/button').click()
    
#da click sa adaugi in cart
    try:
        WebDriverWait(w, 10).until(EC.visibility_of_element_located(("xpath", '//*[@id="orderForm"]/div[3]/div[3]/div[3]/div/a[2]/span'))).click()
    except:
        WebDriverWait(w, 10).until(EC.visibility_of_element_located(("xpath", '/html/body/div[1]/div[2]/div[3]/div[1]/div/form/div[3]/div[3]/div[3]/div/a[2]/span'))).click()

    
    w.find_element('xpath', '/html/body/div[1]/div[2]/div[3]/div[1]/div/form/div[3]/div[4]/div[3]/button').click()
     
    
    WebDriverWait(w, 10).until(EC.visibility_of_element_located(("xpath",'/html/body/section/div/div/div[2]/div/div[1]/div/a'))).click()

    

    
    try:
        #daca esti deja logat probabil nu trebuie sa asctepti deoc asa ca nu mai fac cu wait
        # WebDriverWait(w, 3).until(lambda x : x.find_element('xpath', '/html/body/section/div/div/div[2]/div/ul/li[2]/a')).click()
        w.find_element('xpath', '/html/body/section/div/div/div[2]/div/ul/li[2]/a').click()
        w.find_element('xpath', '/html/body/section/div/div/div[2]/div/div/div[2]/div[1]/form/div[2]/div[1]/input').send_keys(email)
        
        w.find_element('xpath', '/html/body/section/div/div/div[2]/div/div/div[2]/div[1]/form/div[2]/div[2]/input').send_keys(password)
        
        w.find_element('xpath', '/html/body/section/div/div/div[2]/div/div/div[2]/div[1]/form/div[3]/button').click()
        
    except:
        print("Esti logat deja")
        pass

    
    #alege detalii de contact
    w.find_element('xpath', '/html/body/section/div/div[2]/div[2]/div/form/table/tbody/tr[1]/td[2]/button').click()
    
    #accepta termenii si conditiile
    WebDriverWait(w, 10).until(EC.visibility_of_element_located(('xpath', '/html/body/section/div/div[2]/div[2]/div/form/div[2]/div/div[2]/label/input[2]'))).click()

    
    
    #continua
    w.find_element('xpath', '/html/body/section/div/div[2]/div[2]/div/form/div[3]/div/input[1]').click()
    #alege voucher
    WebDriverWait(w, 10).until(EC.visibility_of_element_located(('xpath', '/html/body/section/div/div[2]/div[2]/div[1]/form/div[2]/div[1]/div[2]/button'))).click()
    


    #sunt de acord
    WebDriverWait(w, 10).until(EC.visibility_of_element_located(('xpath',  '/html/body/div[4]/div/div/div[2]/button[1]'))).click()
    
 
    



     

for i in range(1000):   
    iaBiletlol(driver)
    






