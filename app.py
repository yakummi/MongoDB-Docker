from storage import MongoService
from uuid import uuid4
import time

storage = MongoService.get_instance()

for _ in range(5):
    dto = {
        "_id": str(uuid4()),
        "payload": str(uuid4()),
        "field2": str(int(time.time()))
    }
    storage.save_data(dto)

for data in storage.get_data():
    print(data)