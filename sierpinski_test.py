# Author: Dante Bianco
# Date: October 30, 2019
# Description: The code for testin gthe sierpinski triangle thing A4

import sierpinski

def check_equal(fn_name, expected, result):
    """ Print the outcome of a test. Prints either PASS or FAIL, based
        on whether expected == result, followed by fn_name (the name
        of the function being tested), followed by expected and result
        values. """
    if expected == result:
        outcome = "PASS"
    else:
        outcome = "FAIL"
        
    print(outcome, fn_name, expected, result)


def test_midpoint():
    """ Tests the midpoint function """
    result = sierpinski.midpoint((0, 0), (2, 2))
    expected = (1.0, 1.0)
    check_equal("midpoint", expected, result)
    
    result = sierpinski.midpoint((4, 4), (0, 0))
    expected = (2.0, 2.0)
    check_equal("midpoint", expected, result)
    
    result = sierpinski.midpoint((0, 4), (0, 0))
    expected = (0.0, 2.0)
    check_equal("midpoint", expected, result)
    
    result = sierpinski.midpoint((4, 0), (0, 0))
    expected = (2.0, 0.0)
    check_equal("midpoint", expected, result)
    
    
# Testing the distance function from sierpinski.py
def test_distance():
    """Tests the distnace function from my sierpinski file.
        Postconditions: Print the integer value of the maximum distance from the given
        integers
    """
    import math
    
    result = int(sierpinski.distance(75, 100))
    expected = 125
    check_equal("distance", expected, result)
    
    result = int(sierpinski.distance(100, 250))
    expected = 269
    check_equal("distance", expected, result)
    
    result = int(sierpinski.distance(300, 300))
    expected = 424
    check_equal("distance", expected, result)
    
    result = int(sierpinski.distance(275, 120))
    expected = 300
    check_equal("distance", expected, result)
    
    
if __name__ == "__main__":
    
    test_midpoint()
    test_distance()