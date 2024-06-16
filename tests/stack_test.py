import pytest

def test_stack():
    stack = []
    stack.append(1)
    stack.append(2)
    assert stack.pop() == 2
    
def test_stack_2():
    stack = []
    stack.append(1)
    stack.append(2)
    stack.pop()
    assert stack.pop() == 1


def emptiness():
    stack = []
    assert not stack
    stack.append(1)
    assert not not stack


def empty_stack():
    stack = []
    with pytest.raises(IndexError):
        stack.pop()
