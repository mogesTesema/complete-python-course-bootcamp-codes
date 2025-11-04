from exception import CustomPermissionError


user = {
    "name":"Micheal Nielson",
    "access_level":"admin"

}

def user_has_permission(func):
    if user.get('access_level') == 'admin':
        return func
    raise CustomPermissionError

def my_function():
    return "password for admin panel is 1234."
user_has_permission(my_function)()
print("\n"*5)
try:
    my_secure_function = user_has_permission(my_function)
    print("function has been called")
    print(my_secure_function())
except CustomPermissionError as e:
    print(f"a permission error occured in custompermissionerror: {e}")
except Exception as e:
    print(f"something went wrong: {e}")
