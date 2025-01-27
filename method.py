def trapezoidal_rule(f, a, b, n):
    """
    Numerically integrates a function f(x) over the interval [a, b]
    using the trapezoidal rule with n subintervals.

    Parameters:
        f (function): The function to integrate.
        a (float): The start of the interval.
        b (float): The end of the interval.
        n (int): The number of subintervals.

    Returns:
        float: The approximate integral of f(x) from a to b.
    """
    h = (b - a) / n  # Step size
    x = [a + i * h for i in range(n + 1)]  # Subinterval points
    y = [f(xi) for xi in x]  # Function values at the points

    # Apply the trapezoidal formula
    integral = h * (0.5 * y[0] + sum(y[1:-1]) + 0.5 * y[-1])
    return integral


def simpsons_one_third_rule(f, a, b, n):
    """
    Numerically integrates a function f(x) over the interval [a, b]
    using Simpson's one-third rule with n subintervals.

    Parameters:
        f (function): The function to integrate.
        a (float): The start of the interval.
        b (float): The end of the interval.
        n (int): The number of subintervals (must be even).

    Returns:
        float: The approximate integral of f(x) from a to b.
    """
    if n % 2 != 0:
        raise ValueError("Number of subintervals (n) must be even.")

    h = (b - a) / n  # Step size
    x = [a + i * h for i in range(n + 1)]  # Subinterval points
    y = [f(xi) for xi in x]  # Function values at the points

    # Apply Simpson's one-third formula
    integral = h / 3 * (y[0] + y[-1] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-2:2]))
    return integral


def simpsons_three_eighth_rule(f, a, b, n):
    """
    Numerically integrates a function f(x) over the interval [a, b]
    using Simpson's three-eighth rule with n subintervals.

    Parameters:
        f (function): The function to integrate.
        a (float): The start of the interval.
        b (float): The end of the interval.
        n (int): The number of subintervals (must be a multiple of 3).

    Returns:
        float: The approximate integral of f(x) from a to b.
    """
    if n % 3 != 0:
        raise ValueError("Number of subintervals (n) must be a multiple of 3.")

    h = (b - a) / n  # Step size
    x = [a + i * h for i in range(n + 1)]  # Subinterval points
    y = [f(xi) for xi in x]  # Function values at the points

    # Apply Simpson's three-eighth rule formula
    integral = (3 * h / 8) * (
        y[0] + y[-1] +
        3 * sum(y[1:-1:3] + y[2:-1:3]) +
        2 * sum(y[3:-3:3])
    )
    return integral


def boole_rule(f, a, b, n):
    """
    Approximates the integral of f(x) over [a, b] using Boole's Rule.

    Parameters:
        f (function): The function to integrate.
        a (float): The lower bound of integration.
        b (float): The upper bound of integration.
        n (int): The number of subintervals (must be a multiple of 4).

    Returns:
        float: Approximation of the integral.
    """
    if n % 4 != 0:
        raise ValueError("The number of subintervals (n) must be a multiple of 4.")

    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [f(xi) for xi in x]

    # Apply Boole's Rule
    integral = 0
    for i in range(0, n, 4):
        integral += (2 * h / 45) * (
                7 * y[i] + 32 * y[i + 1] + 12 * y[i + 2] + 32 * y[i + 3] + 7 * y[i + 4]
        )

    return integral


def weddle_rule(f, a, b, n):
    """
    Approximates the integral of f(x) over [a, b] using Weddle's Rule.

    Parameters:
        f (function): The function to integrate.
        a (float): The lower bound of integration.
        b (float): The upper bound of integration.
        n (int): The number of subintervals (must be a multiple of 6).

    Returns:
        float: Approximation of the integral.
    """
    if n % 6 != 0:
        raise ValueError("The number of subintervals (n) must be a multiple of 6.")

    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [f(xi) for xi in x]

    # Apply Weddle's Rule
    integral = 0
    for i in range(0, n, 6):
        integral += (3 * h / 10) * (
                y[i] + 5 * y[i + 1] + y[i + 2] + 6 * y[i + 3] +
                y[i + 4] + 5 * y[i + 5] + y[i + 6]
        )

    return integral

def line():
    print('='*50)
