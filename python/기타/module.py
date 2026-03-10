from math import pi as p, sqrt as s
import urllib.request as r

print(p)
print(s(4.0))
print(s(2.0))

response = r.urlopen('http://www.google.co.kr')
print(response.status)
