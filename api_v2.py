#!/bin/python3.6
import requests


def list_repositories_v2(registry):
    d_img = {}
    r = requests.get("{}/v2/_catalog".format(registry))
    i = list(r.json().get("repositories", []))
    for x in i:
        d_img[x] = []
    return d_img


def list_tags_v2(registry):
    imgs = list_repositories_v2(registry)
    for img in sorted(imgs.keys()):
        t = requests.get("{}/v2/{}/tags/list".format(registry, img))
        imgs[img] = (list(t.json().get("tags", [])))
    return imgs

# print(list_repositories_v2("http://hub.bonc:5000"))
print(list_tags_v2("http://hub.bonc:5000"))
# print(tree_img_tags_v2("http://hub.bonc:5000"))
# print(list(map(list_tags_v2, list_repositories_v2("http://hub.bonc:5000"))))
