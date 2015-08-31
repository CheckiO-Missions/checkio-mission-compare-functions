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
                     'def g(hello,world="world):\n'
                     '  return hello + " " + world\n'
                     'c = checkio(f,g)\n'
                     'result = c("hallo",world="earth")\n',
                     "RET['code_result'] = (result==('hallo earth','same')), str(result)",
                     None,
                     "checkio(f,g)('hallo',world='earth') = ('hallo earth','same')"),
        prepare_test('def f(hello="hello",world="world"):\n'
                     '  return hello + " " + world\n'
                     'def g(hello,world="world):\n'
                     '  return hello + " " + world\n'
                     'c = checkio(f,g)\n'
                     'result = c("hallo",world="earth")\n',
                     "RET['code_result'] = (result==('hallo earth','same')), str(result)",
                     None,
                     "checkio(f,g)('hallo',world='earth') = ('hallo earth','same')"),
        prepare_test('def f(hello="hello",world="world"):\n'
                     '  return hello + " " + world\n'
                     'def g(hello,world="world):\n'
                     '  return hello + " " + world\n'
                     'c = checkio(f,g)\n'
                     'result = c(hello="aloha")\n',
                     "RET['code_result'] = (result==('aloha world','same')), str(result)",
                     None,
                     "checkio(f,g)(hello='aloha') = ('aloha world','same')"),
        prepare_test('def f(hello="hello",world="world"):\n'
                     '  return hello + " " + world\n'
                     'def g(hello,world="world):\n'
                     '  return hello + " " + world\n'
                     'c = checkio(f,g)\n'
                     'result = c("planet",hello="ahoi")\n',
                     "RET['code_result'] = (result==(None,'both_error')), str(result)",
                     None,
                     "checkio(f,g)('planet',hello='ahoi') = (None,'both_error')"),
        prepare_test('def f(hello="hello",world="world"):\n'
                     '  return hello + " " + world\n'
                     'def g(hello,world="world):\n'
                     '  return hello + " " + world\n'
                     'c = checkio(f,g)\n'
                     'result = c()\n',
                     "RET['code_result'] = (result==('hello_world','g_error')), str(result)",
                     None,
                     "checkio(f,g)() = (None,'g_error')"),                       
    ],
    "4. Names": [
        prepare_test(
            'f = Friends(({"nikola", "sophia"}, {"stephen", "robot"}, {"sophia", "pilot"}))\n'
            'n = f.names()\n',
            'RET["code_result"] = (n == {"nikola", "sophia", "robot", "pilot", "stephen"}, str(n))',
            'f = Friends(({"nikola", "sophia"}, {"stephen", "robot"}, {"sophia", "pilot"}))\n'
            'f.names()',
            '{"nikola", "sophia", "robot", "pilot", "stephen"}'),
        prepare_test(
            'f = Friends(({"nikola", "sophia"}, {"stephen", "robot"}, {"sophia", "pilot"}))\n'
            'f.remove({"stephen", "robot"})\n'
            'n = f.names()\n',
            'RET["code_result"] = (n == {"nikola", "sophia", "pilot"}, str(n))',
            'f = Friends(({"nikola", "sophia"}, {"stephen", "robot"}, {"sophia", "pilot"}))\n'
            'f.remove({"stephen", "robot"})\n'
            'f.names()',
            '{"nikola", "sophia", "pilot"}'),

    ],
    "5. Connected": [
        prepare_test(
            'f = Friends(({"nikola", "sophia"}, {"stephen", "robot"}, {"sophia", "pilot"}))\n'
            'n = f.connected("nikola")\n',
            'RET["code_result"] = (n == {"sophia"}, str(n))',
            'f = Friends(({"nikola", "sophia"}, {"stephen", "robot"}, {"sophia", "pilot"}))\n'
            'f.connected("nikola")',
            '{"sophia"}'),
        prepare_test(
            'f = Friends(({"nikola", "sophia"}, {"stephen", "robot"}, {"sophia", "pilot"}))\n'
            'n = f.connected("sophia")\n',
            'RET["code_result"] = (n == {"nikola", "pilot"}, str(n))',
            'f = Friends(({"nikola", "sophia"}, {"stephen", "robot"}, {"sophia", "pilot"}))\n'
            'f.connected("sophia")',
            '{"nikola", "pilot"}'),
        prepare_test(
            'f = Friends(({"nikola", "sophia"}, {"stephen", "robot"}, {"sophia", "pilot"}))\n'
            'n = f.connected("DDD")\n',
            'RET["code_result"] = (n == set(), str(n))',
            'f = Friends(({"nikola", "sophia"}, {"stephen", "robot"}, {"sophia", "pilot"}))\n'
            'f.connected("DDD")',
            'set()'),
        prepare_test(
            'f = Friends(({"nikola", "sophia"}, {"stephen", "robot"}, {"sophia", "pilot"}))\n'
            'f.add({"sophia", "stephen"})\n'
            'f.remove({"sophia", "nikola"})\n'
            'n = f.connected("sophia")\n',
            'RET["code_result"] = (n == {"stephen", "pilot"}, str(n))',
            'f = Friends(({"nikola", "sophia"}, {"stephen", "robot"}, {"sophia", "pilot"}))\n'
            'f.add({"sophia", "stephen"})\n'
            'f.remove({"sophia", "nikola"})\n'
            'f.connected("sophia")\n',
            '{"stephen", "pilot"}'),


    ]




    #     prepare_test(test="str(Building(1, 1, 2, 2))",
    #                  answer="Building(1, 1, 2, 2, 10)", ),
    #     prepare_test(test="str(Building(0.2, 1, 2, 2.2, 3.5))",
    #                  answer="Building(0.2, 1, 2, 2.2, 3.5)", ),
    # ],
    # "3. Corners": [
    #     prepare_test(test="Building(1, 1, 2, 2).corners()",
    #                  answer={"south-west": [1, 1], "north-west": [3, 1], "north-east": [3, 3],
    #                          "south-east": [1, 3]}),
    #     prepare_test(test="Building(100.5, 0.5, 24.3, 12.2, 3).corners()",
    #                  answer={"north-east": [112.7, 24.8], "north-west": [112.7, 0.5],
    #                          "south-west": [100.5, 0.5], "south-east": [100.5, 24.8]}),
    # ],
    # "4. Area, Volume": [
    #     prepare_test(test="Building(1, 1, 2, 2, 100).area()",
    #                  answer=4),
    #     prepare_test(test="Building(100, 100, 135.5, 2000.1).area()",
    #                  answer=271013.55),
    #     prepare_test(test="Building(1, 1, 2, 2, 100).volume()",
    #                  answer=400),
    #     prepare_test(test="Building(100, 100, 135.5, 2000.1).volume()",
    #                  answer=2710135.5),
    # ]

}
