import os
import requests
from faker import Faker
from colorama import Fore
from bs4 import BeautifulSoup
import random
import string
from Leveragers import log
from pystyle import Colors, Colorate

fake = Faker('ru_RU')

Ransomuwu = """
   ▄████████ ███    █▄     ▄████████    ▄████████  ▄█     ▄████████ ███▄▄▄▄           ▄██████▄     ▄████████ ███▄▄▄▄   
  ███    ███ ███    ███   ███    ███   ███    ███ ███    ███    ███ ███▀▀▀██▄        ███    ███   ███    ███ ███▀▀▀██▄ 
  ███    ███ ███    ███   ███    █▀    ███    █▀  ███▌   ███    ███ ███   ███        ███    █▀    ███    █▀  ███   ███ 
 ▄███▄▄▄▄██▀ ███    ███   ███          ███        ███▌   ███    ███ ███   ███       ▄███         ▄███▄▄▄     ███   ███ 
▀▀███▀▀▀▀▀   ███    ███ ▀███████████ ▀███████████ ███▌ ▀███████████ ███   ███      ▀▀███ ████▄  ▀▀███▀▀▀     ███   ███ 
▀███████████ ███    ███          ███          ███ ███    ███    ███ ███   ███        ███    ███   ███    █▄  ███   ███ 
  ███    ███ ███    ███    ▄█    ███    ▄█    ███ ███    ███    ███ ███   ███        ███    ███   ███    ███ ███   ███ 
  ███    ███ ████████▀   ▄████████▀   ▄████████▀  █▀     ███    █▀   ▀█   █▀         ████████▀    ██████████  ▀█   █▀  
  ███    ███                                                                                                           
                                    
                                    DEV            : github.com/NotYourSkid
                                    SERVER         : discord.gg/Programmer
                                    HELPER         : github.com/AxZeRXd 
"""

def SDF(details, filename):
    with open(filename, 'a', encoding='utf-8') as file:
        for key, value in details.items():
            file.write(f"{key}: {value}\n-----------------------------------\n")

def GENMAIL():
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(8, 12)))
    domain = 'gamil.com'
    return f"{username}@{domain}"

def RUSS1AN():
    details = {
        'Name': fake.name_female(),
        'Age': fake.random_int(min=18, max=35),
        'City': fake.city(),
        'Phone Number': fake.phone_number(),
        'Email': GENMAIL(),
        'Address': fake.address(),
        'Occupation': fake.job(),
        'Blood Type': fake.random_element(elements=('A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-'))
    }

    R3TE = [6000, 7000, 9000, 12000, 15000, 18000, 20000]
    R3TE1NR = random.choice(R3TE)

    log.inf("Generated Russian Details:")
    for key, value in details.items():
        log.dbg(f"{key}: {value}")
    log.success(f"Rate in INR: {R3TE1NR}")

    SDF(details, "dtl.txt")

    headers = {"Authorization": f"Client-ID rBLIt4-EseXmsHzTkcG-Njf4Wxh06eDvqnGiw6eDh5o"}
    response = requests.get("https://api.unsplash.com/search/photos?query=Russian-teen-girl&per_page=10", headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data.get('results'):
            Imgurl = random.choice(data['results'])['urls']['regular']
            if Imgurl:
                Imgress = requests.get(Imgurl)
                if Imgress.status_code == 200:
                    with open("russian.jpg", 'wb') as img_file:
                        img_file.write(Imgress.content)
                    log.success("Generated Russian Girl Image.")
                    return
    log.err("Failed to generate image link")

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    print(Colorate.Horizontal(Colors.rainbow, Ransomuwu))
    os.system("title Russian Generator || Ransomuwu")
    RUSS1AN()
