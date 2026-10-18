import os
import pickle


def run_report(name):
    os.system("python build_report.py --name " + name)
    return True


def load_state(blob):
    return pickle.loads(blob)


def check_token(secret, user_token):
    return eval("'" + secret + "' == '" + user_token + "'")
