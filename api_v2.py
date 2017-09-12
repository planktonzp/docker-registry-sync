#!/bin/python3.6
import requests
# import os


def list_repositories_v2(registry):
    d_img = {}
    r = requests.get("{}/v2/_catalog".format(registry))
    i = list(r.json().get("repositories", []))
    for x in i:
        d_img[x] = []
    return d_img


def list_tags_v2(registry):
    d_imgs = list_repositories_v2(registry)
    for img in sorted(d_imgs.keys()):
        t = requests.get("{}/v2/{}/tags/list".format(registry, img))
        d_imgs[img] = (list(t.json().get("tags", [])))
    return d_imgs


def compare_v2(registry1, registry2):
    d_imgs1 = list_tags_v2(registry1)
    d_imgs2 = list_tags_v2(registry2)
    pull_imgs = {}
    for img in sorted(d_imgs1.keys()):
        if img in d_imgs2:
            # IMG which need pull
            pull_imgs[img] = sorted(set(d_imgs1[img]) - set(d_imgs2[img]))
            # IMG which need del
            # del_list = set(d_imgs2[img]) - set(d_imgs1[img])
    return pull_imgs


def sync_img(registry1, registry2):
    d_pulls = compare_v2(registry1, registry2)
    for i in d_pulls:
        print("dict[%s]=" % i, dict[i])

# print(list_repositories_v2("http://hub.bonc:5000"))
# print(list_tags_v2("http://hub.bonc:5000"))
# print(compare_v2("http://hub.bonc:5000", "http://hub.bonc:5000"))
print(sync_img("http://hub.bonc:5000", "http://hub.bonc:5000"))
