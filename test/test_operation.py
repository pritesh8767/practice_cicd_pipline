from src.math_operation import add,sub,mul,div
def test_add():
    assert add(2,3)==5
    assert add(8,5)==13
    assert add(6,3)==9

def test_sub():
    assert sub(6,4)==2
    assert sub(9,3)==6
    assert sub(2,1)==1

def test_mul():
    assert mul(3,4)==12
    assert mul(7,5)==35
    assert mul(9,2)==18

def test_div():
    assert div(4,2)==2
    assert div(18,3)==6
    assert div(20,4)==5
