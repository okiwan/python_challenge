"""
Manual steps:
    1) Retrieve the ZIP file (channel.zip)
    2) Decompress in this path and run the procedure
"""

import zipfile
import re
import os

def def06():
    current_file="90052"
    current_extension="txt"
    done=False
    comments=[]

    with zipfile.ZipFile("{}/Downloads/channel.zip".format(os.environ['HOME']), "r") as myzip:
        while not done:
            data=myzip.read("{}.{}".format(current_file, current_extension))
            result=re.search("nothing is ([0-9]*)$", data.decode("utf-8"))
            if result:
                comments.append(myzip.getinfo("{}.{}".format(current_file, current_extension)).comment)
                current_file=result.group(1)
                print("Next ID: {}".format(current_file))
            else:
                print(data)
                done=True

    print(''.join([x.decode("utf-8") for x in comments]))

if __name__ == "__main__":
    def06()
