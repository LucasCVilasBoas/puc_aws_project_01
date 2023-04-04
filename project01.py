import requests

url_valid_isbn13 = "http://webservices.daehosting.com/services/isbnservice.wso"

payload_valid_isbn13 = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <IsValidISBN13 xmlns="http://webservices.daehosting.com/ISBN">
      <sISBN>978-1-4612-9090-2</sISBN>
    </IsValidISBN13>
  </soap:Body>
</soap:Envelope>
"""

url_multiply = "http://www.dneonline.com/calculator.asmx"

payload_multiply = """<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
   <soap:Body>
      <Multiply xmlns="http://tempuri.org/">
         <intA>5</intA>
         <intB>5</intB>
      </Multiply>
   </soap:Body>
</soap:Envelope>
"""


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

url_list_currencies = (
    "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
)

payload_list_currencies = """<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <ListOfCurrenciesByName xmlns="http://www.oorsprong.org/websamples.countryinfo">
    </ListOfCurrenciesByName>
  </soap12:Body>
</soap12:Envelope>
"""

url_convert_temperature = "http://webservices.daehosting.com/services/temperatureconversions.wso?op=FahrenheitToCelsius"
payload_convert_temperature = """<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <FahrenheitToCelsius xmlns="http://webservices.daehosting.com/temperature">
      <nFahrenheit>212</nFahrenheit>
    </FahrenheitToCelsius>
  </soap12:Body>
</soap12:Envelope>"""


headers = {"Content-Type": "text/xml; charset=utf-8"}

response_multiply = requests.request(
    "POST", url_multiply, headers=headers, data=payload_multiply
)
print(response_multiply.status_code)


response_list_country = requests.request(
    "POST", url_country, headers=headers, data=payload_country
)
print(response_list_country.status_code)


response_list_currencies = requests.request(
    "POST", url_list_currencies, headers=headers, data=payload_list_currencies
)
print(response_list_currencies.status_code)


response_convert_temperature = requests.request(
    "POST", url_convert_temperature, headers=headers, data=payload_convert_temperature
)
print(response_convert_temperature.status_code)


response_valid_isbn13 = requests.request(
    "POST", url_valid_isbn13, headers=headers, data=payload_valid_isbn13
)
print(response_valid_isbn13.status_code)
