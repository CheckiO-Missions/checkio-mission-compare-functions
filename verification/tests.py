init_code = """
if not "checkio" in USER_GLOBAL:
    raise NotImplementedError("Where is 'checkio'?")

checkio = USER_GLOBAL['checkio']
"""

#PASS_CODE = """
#RET['code_result'] = True, "Ok"
#"""


def prepare_test(middle_code, test_code, show_code, show_answer):
    if show_code is None:
        show_code = middle_code
    return {"test_code": {"python-3": init_code + middle_code + test_code,
                          "python-27": init_code + middle_code + test_code},
            "show": {"python-3": show_code,
                     "python-27": show_code},
            "answer": show_answer}


TESTS = {
    "1. Absolute Value": [
        prepare_test('f = lambda x: abs(x)\n'
                     'def g(x):\n'
                     '  if x>0:\n'
                     '    return x\n'
                     '  elif x<0:\n'
                     '    return -x\n'
                     'c = checkio(f,g)\n'
                     'result = c(1)\n',
                     "RET['code_result'] = (result==(1,'same')), str(result)",
                     None,
                     "checkio(f,g)(1) = (1,'same')"),
        prepare_test('f = lambda x: abs(x)\n'
                     'def g(x):\n'
                     '  if x>0:\n'
                     '    return x\n'
                     '  elif x<0:\n'
                     '    return -x\n'
                     'c = checkio(f,g)\n'
                     'result = c(2.3)\n',
                     "RET['code_result'] = (result==(2.3,'same')), str(result)",
                     None,
                     "checkio(f,g)(2.3) = (2.3,'same')"),                     
        prepare_test('f = lambda x: abs(x)\n'
                     'def g(x):\n'
                     '  if x>0:\n'
                     '    return x\n'
                     '  elif x<0:\n'
                     '    return -x\n'
                     'c = checkio(f,g)\n'
                     'result = c(-1)\n',
                     "RET['code_result'] = (result==(1,'same')), str(result)",
                     None,
                     "checkio(f,g)(1) = (1,'same')"),
        prepare_test('f = lambda x: abs(x)\n'
                     'def g(x):\n'
                     '  if x>0:\n'
                     '    return x\n'
                     '  elif x<0:\n'
                     '    return -x\n'
                     'c = checkio(f,g)\n'
                     'result = c(0)\n',
                     "RET['code_result'] = (result==(0,'g_error')), str(result)",
                     None,
                     "checkio(f,g)(0) = (0,'g_error')"),
        prepare_test('def f(x):\n'
                     '  if x>0:\n'
                     '    return x\n'
                     '  elif x<0:\n'
                     '    return -x\n'
                     'g = lambda x: abs(x)\n'
                     'c = checkio(f,g)\n'
                     'result = c(0)\n',
                     "RET['code_result'] = (result==(0,'f_error')), str(result)",
                     None,
                     "checkio(f,g)(1) = (0,'f_error')"),                     
    ],
    "2. Remove Elements From List": [
        prepare_test('f = lambda lst,rmv: [x for x in lst if x!=rmv]\n'
                     'g = lambda lst,rmv: lst.remove(rmv) or lst\n'
                     'c = checkio(f,g)\n'
                     'result = c([3,2,3,4,3],2)\n',
                     "RET['code_result'] = (result==([3,3,4,3],'same')), str(result)",
                     None,
                     "checkio(f,g)([3,2,3,4,3],3) = ([3,3,4,3],'same')"),          
        prepare_test('f = lambda lst,rmv: [x for x in lst if x!=rmv]\n'
                     'g = lambda lst,rmv: lst.remove(rmv) or lst\n'
                     'c = checkio(f,g)\n'
                     'result = c([3,2,3,4,3],3)\n',
                     "RET['code_result'] = (result==([2,4],'different')), str(result)",
                     None,
                     "checkio(f,g)([3,2,3,4,3],3) = ([2,4],'different')"),
        prepare_test('f = lambda lst,rmv: [x for x in lst if x!=rmv]\n'
                     'g = lambda lst,rmv: lst.remove(rmv) or lst\n'
                     'c = checkio(f,g)\n'
                     'result = c([3,2,3,4,3],5)\n',
                     "RET['code_result'] = (result==([3,2,3,4,3],'g_error')), str(result)",
                     None,
                     "checkio(f,g)([3,2,3,4,3],5) = ([3,2,3,4,3],'g_error')")
    ],
    "3. Hello World": [
        prepare_test('def f(hello="hello",world="world"):\n'
                     '  return hello + " " + world\n'
                     'def g(hello,world="world"):\n'
                     '  return hello + " " + world\n'
                     'c = checkio(f,g)\n'
                     'result = c("hallo",world="earth")\n',
                     "RET['code_result'] = (result==('hallo earth','same')), str(result)",
                     None,
                     "checkio(f,g)('hallo',world='earth') = ('hallo earth','same')"),
        prepare_test('def f(hello="hello",world="world"):\n'
                     '  return hello + " " + world\n'
                     'def g(hello,world="world"):\n'
                     '  return hello + " " + world\n'
                     'c = checkio(f,g)\n'
                     'result = c(hello="aloha")\n',
                     "RET['code_result'] = (result==('aloha world','same')), str(result)",
                     None,
                     "checkio(f,g)(hello='aloha') = ('aloha world','same')"),
        prepare_test('def f(hello="hello",world="world"):\n'
                     '  return hello + " " + world\n'
                     'def g(hello,world="world"):\n'
                     '  return hello + " " + world\n'
                     'c = checkio(f,g)\n'
                     'result = c("planet",hello="ahoi")\n',
                     "RET['code_result'] = (result==(None,'both_error')), str(result)",
                     None,
                     "checkio(f,g)('planet',hello='ahoi') = (None,'both_error')"),
        prepare_test('def f(hello="hello",world="world"):\n'
                     '  return hello + " " + world\n'
                     'def g(hello,world="world"):\n'
                     '  return hello + " " + world\n'
                     'c = checkio(f,g)\n'
                     'result = c()\n',
                     "RET['code_result'] = (result==('hello_world','g_error')), str(result)",
                     None,
                     "checkio(f,g)() = ('hello world','g_error')"),
        prepare_test('def f(hello="hello",world="WORLD"):\n'
                     '  return hello + " " + world\n'
                     'def g(hello="hello",world="world"):\n'
                     '  return hello + " " + world\n'
                     'c = checkio(f,g)\n'
                     'result = c("ahoi")\n',
                     "RET['code_result'] = (result==('ahoi WORLD','different')), str(result)",
                     None,
                     "checkio(f,g)() = ('ahoi WORLD','different')"),                      
    ]

}
