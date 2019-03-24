import re
import urllib.request
from collections import Counter

def def02():
    url="http://www.pythonchallenge.com/pc/def/ocr.html"
    response=urllib.request.urlopen(url)
    data=str(response.read())

    groups = re.search("%%.*}\*", data)
    if groups:
        print([x for x in Counter(groups.group(0)).most_common() if x[1] == 1])

if __name__ == "__main__":
    def02()
