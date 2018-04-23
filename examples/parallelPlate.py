import flor

ex = flor.Experiment('plate_demo')

ex.groundClient('git')

ones = ex.literal([3, 4, 5], "ones")
ones.forEach()

tens = ex.literal([10, 100], "tens")
tens.forEach()

@flor.func
def multiply(x, y):
    z = x*y
    print(z)
    return z

doMultiply = ex.action(multiply, [ones, tens])
product = ex.artifact('product.txt', doMultiply)

product.parallelPull()
# product.plot()
