import re
import urllib.request


def def04():
    base_url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    current_id="12345"

    response=urllib.request.urlopen(base_url+current_id)
    while response:
        data=response.read().decode("utf-8")
        groups=re.search("next nothing is ([0-9]*)", data)
        if groups:
            current_id=groups.group(1)
            print("New ID found: {}".format(current_id))
        else:
            if data == "Yes. Divide by two and keep going.":
                current_id=str(int(current_id)>>1)
            else:
                print(data)
                return

        response=urllib.request.urlopen(base_url+current_id)

if __name__ == "__main__":
    def04()
