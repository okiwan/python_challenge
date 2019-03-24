import urllib.request
import pickle

def def05():
    url="http://www.pythonchallenge.com/pc/def/banner.p"

    response=urllib.request.urlopen(url)
    if response:
        data=response.read()
        object=pickle.loads(data)
        for line in object:
            print(''.join([char[0] * char[1] for char in line]))

if __name__ == "__main__":
    def05()
