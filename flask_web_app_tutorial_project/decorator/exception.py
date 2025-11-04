class CustomPermissionError(PermissionError):
    def __init__(self,message="accessing the admin level function calling not allowed"):
        super().__init__(message)    
    
    def __str__(self):
        return super().__str__()