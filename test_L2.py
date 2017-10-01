import L2

def test_L2():
    assert L2.L2([1.0], [1.0]) == 1.0

def test_L2_2():
    assert L2.L2([1, 2, 3, 4], [0.25, 0.25, 0.25, 0.25]) == 1.3693063937629153

def test_L2_types():
    try:
        L2.L2("black", "green")
    except TypeError as err:
        assert(type(err) == TypeError)

def test_L2_len():
    try:
        L2.L2([1.0], [0.5, 0.5])
    except ValueError as err:
        assert(type(err) == ValueError)