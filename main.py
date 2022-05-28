import requests as kanye
import os as lamar
import time

def anotha_quote():
    anotha = input("Would you like to see anotha quote by the man the myth the legend, kanye lamar? y/n ")
    if anotha == "y":
        kanye_quote()
    else:
        print("leaving the kanye lamar quote generator...")
        time.sleep(2)
        lamar.system("exit")


def kanye_quote():
        kanye_response = kanye.get("https://api.kanye.rest/")
        variable = kanye_response.json()["quote"]

        print(variable)
        anotha_quote()

kanye_quote()