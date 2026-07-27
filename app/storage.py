class Storage:
    def __init__(self):
        self.files = {}

    def save(self, file_id, content):
        self.files[file_id] = content

    def get(self, file_id):
        return self.files[file_id]

    def delete(self, file_id):
        del self.files[file_id]

