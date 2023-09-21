# Create class 'Counter'
class Counter:
    
    # Default constructor 
    # initial value : Parameter that initializes the object with an assigned value by the user - taken of the argument while is instantiated
    def __init__(self, initial_value):
        
        
        # Variable initial_value taken as class parameter when the object is initialized
        self.count = initial_value
    
    # Method that increases in 2 integers the actual value of count variable
    def inc(self):
        self.count += 1
    
    # Self word used as method parameter to get current context of the object
    # and get access to object values
    # self -> Instance of class -> Attribute value(get/set)
    
    # Method that substract 2 integers of actual value of count variable
    def dec(self):
        self.count -= 1

    # Overrides method string to return custom format
    def __str__(self):
        return "COUNTER: {}".format(self.count)

def test_increase_1_000_000_times():
    
    # Initialize/Instantiate of Counter class
    var_counter4 = Counter(0)
    for _ in range(1_000_000):
        var_counter4.inc()
    
    # boolean expression that checks flag statement (true || false) statement -> var_counter4.count == 1_000_000
    assert var_counter4.count == 1_000_000


# Uncomment in case that needs to run the function
# test_increase_1_000_000_times()

