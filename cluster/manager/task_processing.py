import json
import time
from random import randint


def create_new_task():
    with open("cluster/manager/task_ids.json", "r") as fp:
        data = json.load(fp)
    new_task_id = hex(randint(0, 16_777_216))[2:]  # arbitrary 6 digit hex
    while new_task_id in data:
        new_task_id = hex(randint(0, 16_777_216))[2:]

    data[new_task_id] = {
        "creation_time": time.time(),
        "active": True,
    }  # TODO how to mark as inactive
    with open("cluster/manager/task_ids.json", "w") as fp:
        json.dump(data, fp, indent=4)

    return new_task_id
