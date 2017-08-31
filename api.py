#!/bin/python3.6
import requests


def list_repositories_v2(registry):
    r = requests.get("{}/v2/_catalog".format(registry))
    print(r.url)
    return r.json().get("repositories", [])

print(list(map(list_repositories_v2, ["http://hub.bonc:5000"])))
