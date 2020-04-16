import re
import requests


r = requests.get('https://www.onet.pl')
html_text: str = r.text

sciezka_nrb = r'https://?[-a-zA-Z0-9@:%.[\"|\'].*\.(?i:jpg|gif|png|bmp)[\"|\']'
dopasowanie_nrb = re.findall(sciezka_nrb, r.text)

list1 = []
counter = 0
for i in dopasowanie_nrb:
    print(i)


# 'https://(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&\/\/=]*)'
#
# "[\"|\'].*\.(?i:jpg|gif|png|bmp)[\"|\']"
#
#
# 'https://(www\.)?[-a-zA-Z0-9@:%.[\"|\'].*\.(?i:jpg|gif|png|bmp)[\"|\']'






















# r = requests.get('https://www.tekstowo.pl/piosenka,el_mudo,chacarron_macarron.html')
# html_text: str = r.text
#
# sciezka_nrb = r'Chaccaron'
# dopasowanie_nrb = re.findall(sciezka_nrb, r.text)
#
# list1 = []
# counter = 0
# for i in dopasowanie_nrb:
#     list1.append(i)
#
# print("""W piosence "Chaccaron", słowo "Chaccaron" występuje""", len(list1), "razy")



# sciezka_nrb = r'\d\d+ +\d\d\d\d+ +\d\d\d\d+ +\d\d\d\d+ +\d\d\d\d+ +\d\d\d\d+ +\d\d\d\d'
# dopasowanie_nrb = re.findall(sciezka_nrb, r.text)
#
# for i in dopasowanie_nrb:
#     print("NRB:", i)




# tekst = """Konta dla darczyńców indywidualnych
# 07 1240 6247 1111 0000 4975 0683
# 2020-04-03
# 75 1240 6247 1111 0000 4979 7183 """
#
# sciezka_nrb = r'\d\d+ +\d\d\d\d+ +\d\d\d\d+ +\d\d\d\d+ +\d\d\d\d+ +\d\d\d\d+ +\d\d\d\d'
# dopasowanie_nrb = re.findall(sciezka_nrb, tekst)
#
# for i in dopasowanie_nrb:
#     print("NRB:", i)
#
#
# sciezka_data = re.search(r'\d{4}-\d{2}-\d{2}', tekst)
#
# if sciezka_data:
#     numer = sciezka_data.group()
#     print("data umowy:", numer)