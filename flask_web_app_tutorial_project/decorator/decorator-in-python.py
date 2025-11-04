from exception import CustomPermissionError


user = {
    "name":"Micheal Nielson",
    "access_level":"admin"

}

def user_has_permission(func):
    def secure_func():
        if user.get('access_level') == 'admin':
            return func()
        
        raise CustomPermissionError
    return secure_func
@user_has_permission
def my_function():
    return "password for admin panel is 1234."
print(my_function())
print("\n"*5)
try:
    print("function has been called")
    print(my_function())
except CustomPermissionError as e:
    print(f"a permission error occured in custompermissionerror: {e}")
except Exception as e:
    print(f"something went wrong: {e}")

print(my_function.__name__)

