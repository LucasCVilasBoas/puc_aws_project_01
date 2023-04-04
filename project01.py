from requests import request

headers = {"Content-Type": "text/xml; charset=utf-8"}


# Checa se um ISBN13 é válido
url_isbn13 = "http://webservices.daehosting.com/services/isbnservice.wso"

payload_isbn13 = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <IsValidISBN13 xmlns="http://webservices.daehosting.com/ISBN">
      <sISBN>978-1-4612-9090-2</sISBN>
    </IsValidISBN13>
  </soap:Body>
</soap:Envelope>
"""

response_isbn13 = request("POST", url_isbn13, headers=headers, data=payload_isbn13)
print(response_isbn13.status_code)


# Efetua a multiplicação de 2 números inteiros
url_mult = "http://www.dneonline.com/calculator.asmx"

payload_mult = """<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
   <soap:Body>
      <Multiply xmlns="http://tempuri.org/">
         <intA>5</intA>
         <intB>5</intB>
      </Multiply>
   </soap:Body>
</soap:Envelope>
"""

response_mult = request("POST", url_mult, headers=headers, data=payload_mult)
print(response_mult.status_code)


# Retorna uma lista dos países do mundo com seus respectivos códigos ISO
url_country = (
    "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
)

payload_country = """<?xml version="1.0" encoding="utf-8"?>
    <soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
    <soap12:Body>
        <ListOfCountryNamesByName xmlns="http://www.oorsprong.org/websamples.countryinfo">
        </ListOfCountryNamesByName>
    </soap12:Body>
</soap12:Envelope>
"""

response_countries = request("POST", url_country, headers=headers, data=payload_country)
print(response_countries.status_code)


# Retorna uma lista das moedas do mundo com seus respectivos códigos ISO
url_currency = (
    "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
)

payload_curr = """<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <ListOfCurrenciesByName xmlns="http://www.oorsprong.org/websamples.countryinfo">
    </ListOfCurrenciesByName>
  </soap12:Body>
</soap12:Envelope>
"""

response_currency = request("POST", url_currency, headers=headers, data=payload_curr)
print(response_currency.status_code)


# Converte uma temperatura em Fahrenheit para Celsius
url_temp = "http://webservices.daehosting.com/services/temperatureconversions.wso?op=FahrenheitToCelsius"
payload_temp = """<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <FahrenheitToCelsius xmlns="http://webservices.daehosting.com/temperature">
      <nFahrenheit>212</nFahrenheit>
    </FahrenheitToCelsius>
  </soap12:Body>
</soap12:Envelope>"""


response_temp = request("POST", url_temp, headers=headers, data=payload_temp)
print(response_temp.status_code)
