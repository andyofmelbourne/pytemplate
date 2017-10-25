import os
import sys
me = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(me, '../../')))

import pytemplate

# Note capfd is a wierd pytest thing called a 'fixture' 
# it is automatically discovered and given to the test
# function. So in this case 'out' caputures the print function
# output to std out in hello()

def test_h(capfd):
    pytemplate.hello_world.hello()
    
    out, err = capfd.readouterr()
    assert out == 'hello world!\n'

