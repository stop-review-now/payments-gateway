import ast

def metric(expr: str):
    """Parse a metric expression as a Python literal; never executes code."""
    return ast.literal_eval(expr)
