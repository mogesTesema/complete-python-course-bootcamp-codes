from admin import Admin
from database import Database

a = Admin('rolf',"2323",3)
a.save()
print(Database.find('rolf'))