# class AstuError(TypeError):
#     def __repr__(self,message,code):
#         super().__init__(message)
#         self.code = code
#         self.message = message
#     def __perp__(self):
#         return f'<user defined {self.___class__.__name__} Error>'
#     def add(self, a,b):
#        raise AstuError(f"{self.__class__.__name__} unexpected final exam Error. universty name and actual universty clashing. unexpected sleeping.",self.code)
# raise AstuError("this is testing error",5500)

class MyCustomError(TypeError):
    """
    this is custom error to handle 500 internal server error issue.
    """
    def __init__(self,message,code):
        super().__init__(f"Error code {code}: {message}")
        self.code = code
        self.message = message
error = MyCustomError("OUCH! An error happend.", 500)
print(error.__doc__)
raise error

