import requests


url = 'http://www.webscrapingfordatascience.com/basichttp'
r = requests.get(url)


print(r.text)


r.status_code


r.reason


r.headers


r.request


r.request.headers


r.text


url = 'http://www.webscrapingfordatascience.com/paramhttp/?query=test'
r = requests.get(url)


r.request.url


r.text


from urllib.parse import quote, quote_plus


raw_string = 'a query with /, spaces and?&'


quote(raw_string)


quote_plus(raw_string)


r = requests.get(url + quote(raw_string))


r.url


r.text



