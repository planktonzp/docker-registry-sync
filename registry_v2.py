import os
import requests
from typing import Set, Tuple, Union
from dxf import DXF
from .exceptions import regsyncNotExitsError, regsyncError

def list_repositories_v2(registry: str):

    # list repositories
    r = requests.get("{}/v2/_catalog".format(registry),
                     timeout=2,
                     allow_redirects=False,
                     verify=False)
    return r.json().get("repositories", [])

__all__ = ("list_repositories_v2")
