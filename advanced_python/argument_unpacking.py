class User:
    def __init__(self, username,password):
        self.username = username
        self.password = password
    def from_dict(cls,data):
        return cls(data["username"],data["password"])

users = [
    {'username':"rolf",'password':"2323"},
    {'username':"Tecladoi",'password':"youteclado"}
]
user_objects = map(User.from_dict,users)
print("print one",user_objects("data"))
for usered in user_objects:
    print("print one.one",usered)

user_obj_two = [User(data["username"],data["password"]) for data in users]
user_obj_two = [User(**data) for data in users]
users_two = [
    ('rolf','123'),
    ('huze','2323')
]

user_obj_three = [User(*data) for data in users_two]
print("print two",user_obj_three)
for user in user_obj_three:
    print("print three",user)