import os
import time
from datetime import datetime, date
from datetime import time as datetimetime
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
import urllib, winsound
import urllib.error
import urllib.request
import json
import schedule
import requests


#funzione per inviare il messaggio al gruppo
def telegram_bot_sendtext(bot_message):

    #bot_token = '912915432:AAESgJBQlqSbo2aGeAh8Uko7n7UJehDexI4'
    new_bot_token='1099352917:AAH7qrpH-QJ-N1vV1iLA2OZOl32ck7Mps4M'

   params ={
        "chat_id":'-490364520', #chat id gruppo ProduceICT_FreePBX_MissedCalls
        "text":bot_message,
        "parse_mode":"HTML"
    }

    #send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    send_text = 'https://api.telegram.org/bot' + new_bot_token + '/sendMessage'
    response = requests.get(send_text, params=params)

    return response.json()

#funzione che controlla le chiamate perse e manda messaggio al gruppo telegram
def schedule_every_720_min():

    #definire path per driver chrome e restanti argomenti per permetterne l'esecuzione in background
    driver_path=r"C:\Users\produceict\Desktop\Python-Update\chromedriver.exe"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless') #questo parametro evita l'apertura del browser
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    prefs = {"credentials_enable_service": False ,
            "profile.password_manager_enabled" : False
            }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"]);
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("--disable-infobars")

    browser = webdriver.Chrome(driver_path, options=chrome_options);
    browser.get("https://172.31.255.206");
    browser.delete_all_cookies()
    #browser.fullscreen_window()

    #autenticazione
    #access_button=browser.find_element_by_xpath('//*[@id="login_admin"]').click();#cambio placeholder
    #https://172.31.255.206-->find_element

    #username= WebDriverWait(browser, 1).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="loginform"]/div[1]/input')))
    username = browser.find_element_by_xpath('/html/body/div[7]/form/fieldset/div[3]/input')
    username.send_keys('produceict')

    password = browser.find_element_by_xpath('/html/body/div[7]/form/fieldset/div[5]/input')
    password.send_keys('?ipotenusa-206.To')

    #time.sleep(1)

    login_button = browser.find_element_by_xpath('/html/body/div[7]/div/button[1]').click()
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
    #inserimento parametri per ricerca chiamate perse
    #start_day=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/table/tbody/tr/td/form/fieldset/table/tbody/tr[2]/td[2]/input[1]')
    #start_day.send_keys(2*Keys.BACKSPACE)
    # start_day.send_keys(13) comment
    #start_day.send_keys(datetime.now().day)

    #callerID=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/table[1]/tbody/tr/td/form/fieldset/table/tbody/tr[4]/td[2]/input[1]')
    #callerID.send_keys('External')

    #disposition=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/table/tbody/tr/td/form/fieldset/table/tbody/tr[12]/td[2]/select/option[5]').click()

    #last_time = datetimetime(8, 30)

    #ciclo che termina dopo le ore 18, invia messaggi delle chiamate
    #while True:

        #search_button=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/table/tbody/tr/td/form/fieldset/table/tbody/tr[13]/td[2]/table/tbody/tr/td[2]/input').click()
        #clock = datetime.now()

        #ricerca la tabella, se non ci fosse (perchè nessuna chiamata) va direttamente all'except
        #try:
            #table=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/table[2]')
            #rows = table.find_elements(By.CLASS_NAME, "record") # get all of the rows in the table

            #salva le chiamate in calls

            #calls = []

            #for row in rows:
                #col = row.find_elements(By.TAG_NAME, "td")
                #time_call, caller_id = col[0], col[3]
                #calls.append((time_call.text, caller_id.text))


            #se l'orario dell'ultima chiamata persa è superiore a last_time, salva le nuove chiamate perse in missed calls

            #missed_calls = []

            #for t, c in calls:

                #orario = datetimetime( int(t[-5:][:2]), int(t[-5:][3:]))

                #if orario > last_time:
                    #missed_calls.append((t[-5:], c))

            #print("*"*30)
            #print(missed_calls)

            #se ci sono chiamate perse invia messaggio e aggiorna il parametro last_time per evitare di ripetere quelle già comunicate
            #if missed_calls:
                #telegram_bot_sendtext("<b>Il giorno {}/{} alle ore {} sono state registrate le seguenti chiamate perse:</b>".format(clock.day, clock.month, clock.strftime("%H:%M")))
                #last_time = datetimetime( int(missed_calls[0][0][-5:][:2]), int(missed_calls[0][0][-5:][3:]))
                #corpus = ""
                #for m in missed_calls:
                    #corpus += "{}, {}\n".format(m[0], m[1].split("<")[-1].split(">")[0])
                #telegram_bot_sendtext(corpus)
            #else:
                #se l'orario è diverso dalle 13 e non ci sono chiamate perse invia il messaggio
                #if clock.hour != 13:
                    #telegram_bot_sendtext("<b>Nessuna nuova chiamata alle {}</b>".format(clock.strftime("%H:%M")))

        #except:
            #se l'orario è diverso dalle 13 e non ci sono chiamate perse invia il messaggio
            #if clock.hour != 13:
                #telegram_bot_sendtext("<b>Nessuna nuova chiamata alle {}</b>".format(clock.strftime("%H:%M")))

        #se l'orario supera le 18 allora chiude il ciclo perchè non dovrà controllare più nulla fino al giorno dopo
        #if clock.hour >= 18:
            #break
        #time.sleep(1800)


    #settings=browser.find_element_by_xpath('/html/body/div[1]/div[1]/nav/div/ul/li[2]/button/i').click()
    #logout=browser.find_element_by_xpath('/html/body/div[1]/div[1]/nav/div/ul/li[2]/ul/li[3]/a').click()


    #browser.quit()


# schedule_every_30_min()


#if __name__ == "__main__":
#    schedule_every_720_min()

#observium
#$ os = "cisco-spa";
#$ config ['os'] [$ os] ['text'] = "Cisco SPA";
#$ config ['os'] [$ os] ['type'] = "voip";
#$ config ['os'] [$ os] ['vendor'] = "Cisco Small Business";
#$ config ['os'] [$ os] ['icon'] = "ciscosb";
#$ config ['os'] [$ os] ['sysObjectID'] [] = ".1.3.6.1.4.1.9.6.1.23.1.1";
#$ config ['os'] [$ os] ['sysDescr'] [] = "/ ^ CISCO SPA /";
