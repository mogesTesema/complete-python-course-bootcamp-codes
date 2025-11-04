import functools
from exception import CustomPermissionError


user = {
    "name":"Micheal Nielson",
    "access_level":"admin"

}

def user_has_permission(func):
    @functools.wraps(func) # hey secure_func keep the name and doc information of this function func instead of injecting your's information, just you are wrapper function.
    def secure_func(*args,**kwargs):
        if user.get('access_level') == 'admin':
            return func(*args,**kwargs)
        
        raise CustomPermissionError
    return secure_func
@user_has_permission
def my_function(panel):
    return f"password for {panel} panel is 1234."

def another():
    return "another function"
print(my_function("movies"))
print(another())
print("\n"*5)
try:
    print("function has been called")
    print(my_function("admin's"))
except CustomPermissionError as e:
    print(f"a permission error occured in custompermissionerror: {e}")
except Exception as e:
    print(f"something went wrong: {e}")

print(my_function.__name__)

