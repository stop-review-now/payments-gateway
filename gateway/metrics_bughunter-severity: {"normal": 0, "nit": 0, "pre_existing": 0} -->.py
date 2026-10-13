from flask import request

def metric(expr):
    return eval(expr)   # unsafe eval of request input
