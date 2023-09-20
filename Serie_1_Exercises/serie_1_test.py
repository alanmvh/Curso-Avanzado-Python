
# Import counter class from file serie_1
from serie_1 import Counter

def test_exercise_1():
    var_counter = Counter(0)
    var_counter.inc()
    var_counter.inc()
    var_counter.inc()
    var_counter.dec()
    print(var_counter.count) # Output value : 2
    assert var_counter.count == 2

def test_exercise_2():
    var_counter = Counter(100)
    var_counter.inc()
    var_counter.inc()
    var_counter.inc()
    var_counter.dec()
    print(var_counter.count) # Output value : 2
    assert var_counter.count == 102 

def test_exercise_3():
    
    var_counter = Counter(99)
    var_counter.inc()
    assert str(var_counter) == "COUNTER: 100"
    
# Unit test to increase 10 times the count variable
def test_increase_10_times():
    # Initialize/Instantiate of Counter class
    var_counter1 = Counter(20)
    
    # For loop that iterates 10 times(0-9)
    for _ in range(10):
        # .inc() method call to increase 'count' variable
        var_counter1.inc()
    
    # boolean expression that checks flag statement (true || false) statement -> var_counter1.count == 40
    assert var_counter1.count == 30

# Unit test to decrease 300 times
def test_decrease_300_times():
    # Initialize/Instantiate of Counter class
    var_counter2 = Counter(0)
    
    # For loop that iterates 10 times(0-299)
    for _ in range(300):
        # .dec() method call to decrease 'count' variable
        var_counter2.dec()
    
    # boolean expression that checks flag statement (true || false) statement -> var_counter2.count == -600
    assert var_counter2.count == -300

# Function that increases 2 million times variable 'count'
def increase_2_000_000_times():
    
    # Initialize/Instantiate of Counter class
    var_counter3 = Counter(0)
    for _ in range(2_000_000):
        var_counter3.inc()
    
    # boolean expression that checks flag statement (true || false) statement -> var_counter3.count == 2_000_000
    assert var_counter3.count == 2_000_000

def test_increase_1_000_000_times():
    
    # Initialize/Instantiate of Counter class
    var_coiunter4 = Counter(0)
    for _ in range(1_000_000):
        var_coiunter4.inc()
    
    # boolean expression that checks flag statement (true || false) statement -> var_coiunter4.count == 1_000_000
    assert var_coiunter4.count == 1_000_000

def test_exercise_7():
    var_counter7 = Counter(0)
            
    def increase_to(n):
        while var_counter7.count != n:
            var_counter7.inc()

    def decrease_to(n):
        while var_counter7.count != n:
            var_counter7.dec()

    increase_to(100)
    decrease_to(50)
    
    assert var_counter7.count == 50


def test_benchmark(benchmark):
    benchmark(increase_2_000_000_times)

test_exercise_7()