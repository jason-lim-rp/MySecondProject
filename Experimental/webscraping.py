from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

url = "https://www.haze.gov.sg/"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urlopen(req)
parsed = BeautifulSoup(response)

list_of_divs = parsed.findAll('div')
for z in list_of_divs:
    if z.get('id') == "box-one":
        t = z.findAll('div')
        print(len(t))
        for y in t:
            #print (y.get('class'))
            if y.get("class") == ['map', 'map-psi']:
                u = y.findAll('span')
                for x in u:
                    print (x.get('id'))

            #print (y, "##################\n#####################\n#########")1