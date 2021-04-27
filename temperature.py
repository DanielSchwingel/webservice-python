import requests
import xml.etree.ElementTree as ET

fahrenheit = input('Informe a temperatura em Fahrenheit (ºF):')
print('Fazendo a convesão...Aguarde')
url = 'https://www.w3schools.com/xml/tempconvert.asmx'
header = {'Content-Type' : 'application/soap+xml; charset=utf-8'}
body = """<?xml version='1.0' encoding='utf-8'?>
   <soap12:Envelope xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xmlns:xsd='http://www.w3.org/2001/XMLSchema' xmlns:soap12='http://www.w3.org/2003/05/soap-envelope'>
      <soap12:Body>
         <FahrenheitToCelsius xmlns='https://www.w3schools.com/xml/'>
            <Fahrenheit>""" + fahrenheit +"""</Fahrenheit>
         </FahrenheitToCelsius>
      </soap12:Body>
</soap12:Envelope>
"""

response = requests.post(url, headers=header, data=body)
response_xml = ET.fromstring(response.content)

for child in response_xml.iter('*'):
   if child.tag == '{https://www.w3schools.com/xml/}FahrenheitToCelsiusResult':
      print('A temperatura em Celsius é {}ºC'.format(child.text))
   