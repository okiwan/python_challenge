import re
import urllib.request

from collections import Counter

def def03():
    url="http://www.pythonchallenge.com/pc/def/equality.html"
    response=urllib.request.urlopen(url)
    result=''

    if response:
        data=str(response.read())
        print(''.join([x[3] for x in re.findall("(?<![A-Z])[A-Z]{3}[a-z][A-Z]{3}(?![A-Z])", data)]))


if __name__ == "__main__":
    def03()
