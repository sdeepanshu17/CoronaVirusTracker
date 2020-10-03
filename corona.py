import requests
from bs4 import BeautifulSoup
import pyttsx3

print("Please wait for a while(It may take a minute or so)")
print("Extracting Data")
URL = "https://www.worldometers.info/coronavirus/country/india/"
r = requests.get(URL)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
soup = BeautifulSoup(r.content, 'html5lib')

data=soup.find_all('div' , class_="maincounter-number")

Total_cases=data[0].text.strip()
Deaths=data[1].text.strip()
Recovered=data[2].text.strip()
print("Data Extracted!")

t="Total Corona Virus Cases in India are "+str(Total_cases)
d="Total Deaths: "+ str(Deaths)
r="Total Recovered Cases: "+str(Recovered)
print("Processing")

print("Success!")

def main():
    print("Welcome to Live CoronaVirus Tracker!")
    engine.say("Welcome to Laive  CoronaVirus Tracker!")
    engine.runAndWait()

def numbers():
    print("Total Cases in India: ", Total_cases)
    engine.say(t)
    engine.runAndWait()

    print("Total Deaths: ", Deaths)
    engine.say(d)
    engine.runAndWait()

    print("Total Recovered Cases: ", Recovered)
    engine.say(r)
    engine.runAndWait()

    engine.say("If you wish to listen Data again enter 1   and to exit enter 0")
    engine.runAndWait()
    x = input("If you wish to listen Data again enter 1 and to exit enter 0: ")
    if x== "1":
        numbers()
    else:
        engine.say("Thank You for using this App. This software is developed by Dipanshu Singh. For latest CoronaVirus updates visit again!")
        engine.runAndWait()
        exit()

main()
numbers()
