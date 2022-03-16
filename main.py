# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import sys

def getJson(username='wlyenlin'):
    params={'sort':'created','type':'owner'}
    response = requests.get("https://api.github.com/users/%s/repos?sort=created?type=owner" % username,params)
    return response.json()

def printName(json):
    for repo in json:
        print(repo['name'])

if __name__ == '__main__':

    added = sys.argv[1:]

    if added:
        for n in added:
            json = getJson(n)
            printName(json)

    else:
        json=getJson()
        printName(json)

