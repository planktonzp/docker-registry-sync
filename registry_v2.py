import os
import requests
from typing import Set, Tuple, Union
from dxf import DXF
from .exceptions import regsyncNotExitsError, regsyncError

def list_repositories_v2(registry: str):

    r = requests.get("{}/v2/_catalog".format(registry),
                     timeout=2,
                     allow_redirects=False,
                     verify=False)
    return r.json().get("repositories", [])
def list_tags_v2(registry, i):
    i = r.json().get([])
    t = requests.get("{}/v2/{}/tags/list".format(registry, i),
                     timeout=2,
                     allow_redirects=False,
                     verify=False)

__all__ = ("list_repositories_v2", "list_tags_v2")
