import requests

r1 = requests.get('http://localhost:5001/', data={'key':'value'})
print(r1)
print(r1.text)

r3 = requests.get('http://localhost:5002/', data={'key':'value'})
print(r3)
print(r3.text)

r3 = requests.get('http://localhost:5001/run', data={'key':'value'})
print(r3)
print(r3.text)