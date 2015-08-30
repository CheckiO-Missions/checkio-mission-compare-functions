init_code = """
if not "checkio" in USER_GLOBAL:
    raise NotImplementedError("Where is 'checkio'?")

checkio = USER_GLOBAL['checkio']
"""

PASS_CODE = """
RET['code_result'] = True, "Ok"
"""


def prepare_test(middle_code, test_code, show_code, show_answer):
    if show_code is None:
        show_code = middle_code
    return {"test_code": {"python-3": init_code + middle_code + test_code,
                          "python-27": init_code + middle_code + test_code},
            "show": {"python-3": show_code,
                     "python-27": show_code},
            "answer": show_answer}


TESTS = {
    "1. Init": [
        prepare_test(
            'f = lambda: 0\n'
            'g = lambda: 0\n'
            'RET["code_result"] = True',
            'SHOWC',
            'SHOWA')
    ]}
