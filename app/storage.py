import time
from threading import Lock

class Storage:
    def __init__(self):
        self.files = {}
        self.lock = Lock()

    def save(self, file_id, content):
        with self.lock:
            time.sleep(0.01)
            self.files[file_id] = content

    def get(self, file_id):
        return self.files[file_id]

    def delete(self, file_id):
        del self.files[file_id]

