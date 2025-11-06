from typing import List
    

class Segment:
    def __init__(self,departure,destination):
        self.departure = departure
        self.destination = destination

class Flight:
    def __init__(self,segments:List[Segment]):
        self.segments = segments
    
    @property
    def departure_point(self):
        return self.segments[0].departure
    
    @departure_point.setter
    def departure_point(self,val):
        self.segments[0].departure = val


flight = Flight([Segment("GLA","ADD"),Segment("BDR","DESE")])
print("the flight is:\n",flight.departure_point)

flight.departure_point = "EDI"
print(f"flight updated: {flight.departure_point}")