import ast

x = int()
arr = []

def get_count_conditional_expression(node):
    count = 0
    for n in ast.walk(node):
        if isinstance(n, ast.If) or isinstance(n, ast.For) or isinstance(n, ast.While):
            count+=1
        if isinstance(n, ast.Match):
            cases = n.cases
            if 'value' in cases[-1].pattern._fields:
                count+=len(cases)
            else:
                count+=len(cases)-1
    return count


def get_depth_conditional_expression(node, depth=0, result=[]):
    for node_body in node.body:
        check_depth_conditional_expression(node_body, depth, result)

def check_depth_conditional_expression(node_body, depth=0, result=[]):
    if isinstance(node_body, ast.If):
        get_depth_conditional_expression(node_body, depth + 1, result)
        for else_node in node_body.orelse:
            check_depth_conditional_expression(else_node, depth=depth + 1, result=result)
    if isinstance(node_body, ast.Match):
        cases = node_body.cases
        for i in range(len(cases) - 1):
            get_depth_conditional_expression(cases[i], depth + i + 1, result)
        if 'value' in cases[-1].pattern._fields:
            get_depth_conditional_expression(cases[-1], depth + len(cases), result)
        else:
            get_depth_conditional_expression(cases[-1], depth + len(cases) - 1, result)
    elif isinstance(node_body, ast.For):
        get_depth_conditional_expression(node_body, depth=depth + 1, result=result)
    elif isinstance(node_body, ast.While):
        get_depth_conditional_expression(node_body, depth=depth + 1, result=result)

    result.append(depth)


def count_variables(node):
    sum = 0
    vars = dict()
    for n in ast.walk(node):
        if isinstance(n, ast.Attribute):
            tmp= n.attr
            s = ""
            while isinstance(n.value, ast.Attribute):
                s = n.value.attr + "." +s
                n = n.value
                try:
                    s = n.value.id + "." +s
                except AttributeError:
                    s = s
            if s[:-1] in vars.keys():
                vars[s[:-1] ] -= 1
            else:
                vars[s[:-1] ] = -1
            s+=tmp

            if s not in vars.keys():

                vars[s] = 1
            else:
                vars[s] +=1
        elif isinstance(n, ast.Constant):
            if str(n.value) not in vars.keys():

                vars[str(n.value)] = 1
            else:
                vars[str(n.value)] +=1
        elif isinstance(n, ast.Name):

            if   n.id not in vars.keys():
                vars[n.id] = 1
            else:
                vars[n.id] +=1

    return vars


for i in range(10):
    if x in arr:
        y = 0
    elif x == 0:
        y = 1
    elif x < 0.5:
        y = 2
    elif x < 1:
        y = 3
    else:
        y = 4


while True:

    if a == b:
        #1
        if 1 == 2:
            #2
            match method:
                case 1:
                    #3
                    selected_task = Task1()
                case 2:
                    #4
                    selected_task = Task2()
                case 3:
                    #5
                    selected_task = Task3()
                case 4:
                    #6
                    selected_task = Task4()
                case 5:
                    #7
                    selected_task = Task5()
                case -1:
                    #8
                    if True:
                        #9
                        pass
                case _:
                    #8
                    for i in range(10):
                        #9
                        while True:
                            #10
                            a = "In for"
                            if True:
                                #11
                                a = 3
                                v = 4
                                if True:
                                    #12
                                    a = 3
                                    v = 4

                                    if True:
                                        #13
                                        a = 3
                                        v = 4
                                        pass
                                    else:
                                        #13
                                        a = 3
                                        v = 4
                                        pass
                                elif True:
                                    #13
                                    a = 3
                                    v = 4
                                    pass
                                else:
                                    #13
                                    a = 3
                                    v = 4
                                    a = 3
                                    if True:
                                        #14
                                        a = 3
                                        v = 4
                                        pass

                    selected_task = None
                    print("Indefined request\n")
        else:
            for item in arr:
                print(str(item))
