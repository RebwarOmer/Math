def bisection_method(f, a, b, tol):
    """
    Bisection method to find the root of the function f(x) in the interval [a, b]
    with a given tolerance tol.
    """
    if f(a) * f(b) > 0:
        raise ValueError("The function values at the interval endpoints must have opposite signs.")

    iteration = 0
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iteration += 1

    root = (a + b) / 2
    return root, iteration

# Get user input for the equation, interval [a, b], and tolerance E
equation = input("Enter the equation in terms of 'x' (e.g., x**3 - x - 1): ")
f = lambda x: eval(equation)  # Convert the input string to a function

a = float(input("Enter the lower bound of the interval: "))
b = float(input("Enter the upper bound of the interval: "))
E = float(input("Enter the tolerance (E): "))

# Find the root using the bisection method
root, iterations = bisection_method(f, a, b, E)

# Print the result
print(f"Root found: {root}")
print(f"Iterations: {iterations}")