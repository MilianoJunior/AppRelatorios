# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 16:10:03 2022

@author: jrmfi
"""
# import requests

# url = 'http://localhost/api/test'


# params = {
#     'email': 'jrmfilho23@gmail.com',
#     'senha':'123456'
#     }

# res = requests.get(url, params=params)

# print(res.content)
import random
chave = {}
def cryptografia(texto):
    global chave
    chave = {
        'a': random.normalvariate(mu=4.0, sigma=1.0),
        'b': random.normalvariate(mu=4.0, sigma=1.0),
        'c': random.normalvariate(mu=4.0, sigma=1.0),
        'd': random.normalvariate(mu=4.0, sigma=1.0),
        'e': random.normalvariate(mu=4.0, sigma=1.0),
        'f': random.normalvariate(mu=4.0, sigma=1.0),
        'g': random.normalvariate(mu=4.0, sigma=1.0),
        'h': random.normalvariate(mu=4.0, sigma=1.0),
        'i': random.normalvariate(mu=4.0, sigma=1.0),
        'j': random.normalvariate(mu=4.0, sigma=1.0),
        'k': random.normalvariate(mu=4.0, sigma=1.0),
        'l': random.normalvariate(mu=4.0, sigma=1.0),
        'm': random.normalvariate(mu=4.0, sigma=1.0),
        'n': random.normalvariate(mu=4.0, sigma=1.0),
        'o': random.normalvariate(mu=4.0, sigma=1.0),
        'p': random.normalvariate(mu=4.0, sigma=1.0),
        'q': random.normalvariate(mu=4.0, sigma=1.0),
        'r': random.normalvariate(mu=4.0, sigma=1.0),
        's': random.normalvariate(mu=4.0, sigma=1.0),
        't': random.normalvariate(mu=4.0, sigma=1.0),
        'u': random.normalvariate(mu=4.0, sigma=1.0),
        'v': random.normalvariate(mu=4.0, sigma=1.0),
        'w': random.normalvariate(mu=4.0, sigma=1.0),
        'x': random.normalvariate(mu=4.0, sigma=1.0),
        'y': random.normalvariate(mu=4.0, sigma=1.0),
        'z': random.normalvariate(mu=4.0, sigma=1.0),
        ' ': random.normalvariate(mu=4.0, sigma=1.0),
        '.': random.normalvariate(mu=4.0, sigma=1.0),
        ',': random.normalvariate(mu=4.0, sigma=1.0),
    }
    msg = ''
    for s in texto:
        msg += '-' + str(round(chave[s],3))
    return msg, chave
texto = cryptografia('ola mundo, nao existe liberdade nas redes, nao acredite no que leem')
print(texto)
'''-1.541-3.673-4.247-3.484-3.574-4.468-3.103-2.566-1.541-3.984-3.484-3.103-4.247-1.541-3.484-3.799-5.858-3.179-3.516-2.659-3.799-3.484-3.673-3.179-1.664-3.799-4.362-2.566-4.247-2.566-3.799-3.484-3.103-4.247-3.516-3.484-4.362-3.799-2.566-3.799-3.516-3.984-3.484-3.103-4.247-1.541-3.484-4.247-2.758-4.362-3.799-2.566-3.179-2.659-3.799-3.484-3.103-1.541-3.484-4.047-4.468-3.799-3.484-3.673-3.799-3.799-3.574'''
print(chave)
'''{'a': 4.247299840332793, 'b': 1.6640447669397451, 'c': 2.7578923300030294, 'd': 2.566271320036757, 'e': 3.7985959714044357, 'f': 5.819396476263208, 'g': 3.4142459508863627, 'h': 2.833487380421487, 'i': 3.178695119212798, 'j': 3.9271885646302067, 'k': 5.189553882912428, 'l': 3.673053055653828, 'm': 3.574029229917533, 'n': 3.103013379619031, 'o': 1.5405192126281642, 'p': 3.3015307421029023, 'q': 4.0470174681683, 'r': 4.361547737252456, 's': 3.5156265397763256, 't': 2.659114800569947, 'u': 4.467798335948142, 'v': 3.22417960315188, 'w': 3.6328518451445553, 'x': 5.857597032557168, 'y': 5.021308388111994, 'z': 5.003679081802732, ' ': 3.4844986667860276, '.': 5.976403524046585, ',': 3.9843921741432493})
{'a': 4.247299840332793, 'b': 1.6640447669397451, 'c': 2.7578923300030294, 'd': 2.566271320036757, 'e': 3.7985959714044357, 'f': 5.819396476263208, 'g': 3.4142459508863627, 'h': 2.833487380421487, 'i': 3.178695119212798, 'j': 3.9271885646302067, 'k': 5.189553882912428, 'l': 3.673053055653828, 'm': 3.574029229917533, 'n': 3.103013379619031, 'o': 1.5405192126281642, 'p': 3.3015307421029023, 'q': 4.0470174681683, 'r': 4.361547737252456, 's': 3.5156265397763256, 't': 2.659114800569947, 'u': 4.467798335948142, 'v': 3.22417960315188, 'w': 3.6328518451445553, 'x': 5.857597032557168, 'y': 5.021308388111994, 'z': 5.003679081802732, ' ': 3.4844986667860276, '.': 5.976403524046585, ',': 3.9843921741432493}'''