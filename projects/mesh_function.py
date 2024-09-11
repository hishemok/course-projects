import numpy as np


def mesh_function(f, t):
    return np.array([f(i) for i in t])

def func(t):
    if t <= 3 & t > 0:
        return np.exp(-t)
    elif t > 3 & t <= 4:
        return np.exp(-3*t)

def test_mesh_function():
    t = np.array([1, 2, 3, 4])
    f = np.array([np.exp(-1), np.exp(-2), np.exp(-3), np.exp(-12)])
    fun = mesh_function(func, t)
    assert np.allclose(fun, f)

if __name__ == '__main__':
    test_mesh_function()

