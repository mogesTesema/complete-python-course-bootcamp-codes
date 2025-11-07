
class PrinterError(Exception):
    def __init__(self):
        super().__init__()
class Printer:
    def __init__(self,pages_per_s:float,capacity:int):
        self.pages_per_s = pages_per_s
        self.capacity = capacity
    
    def print(self,pages):
        if pages > self.capacity:
            raise PrinterError("printer does not have enough capacity for all these pages.")
        self.capacity -= pages
        return f"printer {pages}, pages in {pages/self.pages_per_s:.2f} seconds."
# raise PrinterError