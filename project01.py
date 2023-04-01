import requests

url_num_to_dollar = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso"

payload_num_to_dollar = """<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <NumberToDollars xmlns="http://www.dataaccess.com/webservicesserver/">
         <dNum>96</dNum>
      </NumberToDollars>
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

url_convert_temperature = "https://www.w3schools.com/xml/tempconvert.asmx"
payload_convert_temperature = """<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <CelsiusToFahrenheit xmlns="https://www.w3schools.com/xml/">
      <Celsius>20</Celsius>
    </CelsiusToFahrenheit>
  </soap12:Body>
</soap12:Envelope>"""


headers = {"Content-Type": "text/xml; charset=utf-8"}

response = requests.request("POST", url_country, headers=headers, data=payload_country)

print(response.status_code)
print(response.text)
