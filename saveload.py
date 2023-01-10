############################
# IMPORT
############################

import json
import os
import time
import dataclasses
from datetime import datetime
import glob

############################
# SAVELOAD
############################

@dataclasses.dataclass()
class Save:
    created: datetime
    updated: datetime
    version: int
    data: dict
    

def save(fileName: str, data: dict):
    if not os.path.isdir("saves"):
        os.mkdir("saves")
    
    dataFormated = {
        "createdTime": time.time(),
        "updatedTime": time.time(),
        "version": 1,
        "data": data
    }


    if os.path.exists(fileName + ".save"):
        with open(fileName + ".save", "r") as f:
            dataFormated = json.load(f)

        dataFormated["data"] = data
        dataFormated["version"] = dataFormated["version"] + 1
        dataFormated["updatedTime"] = time.time()

    with open(fileName + ".save", "w") as f:
        f.write(json.dumps(dataFormated))

def load(fileName: str) -> Save:
    data = None

    with open(fileName + ".save", "r") as f:
        data = json.load(f)

    return Save(
        data["createdTime"],
        data["updatedTime"],
        data["version"],
        data["data"]
    )

def findSaves(dir: str) -> list[str]:
    if not os.path.isdir(dir):
        return []

    return glob.glob(dir + "/*.save")
