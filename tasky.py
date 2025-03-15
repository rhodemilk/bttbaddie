from pydantic import BaseModel
#Basemodel is our parent class to transfer objects back and forth

cur_id = 0 #initalizing current id = 0
def increment():
    global cur_id #this is referring to the variable outside of the scope
    cur_id += 1 
    return cur_id

class Task(BaseModel):
    id: int
    description: str = ""
    is_complete: bool = False

#self is like this in java
#**data whatever paramters assigns it to data
    def __init__(self, **data):
        super().__init__(id = increment(), **data)
        #second **data u can seperate each datatype like with functions
        #super calls the constructor from the parent class and adding in our own 

