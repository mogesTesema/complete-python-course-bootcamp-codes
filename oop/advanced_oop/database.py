class Database:
    content = {"users":[]}
    @classmethod
    def insert(cls,data):
        cls.content["users"].append(data)
    
    @classmethod
    def finder(cls,find):
        return [user for user in cls.content["users"] if user == find]
        
    @classmethod
    def remove(cls):
        cls.content["users"] = [user for user in cls.content["users"] if not self.finder(user)]
