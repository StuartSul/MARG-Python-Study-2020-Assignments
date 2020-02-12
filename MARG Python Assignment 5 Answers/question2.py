variables = {}
error_msg = 'Error: undefined syntax'

while True:
    print(variables)
    command = input('>> ')
    command = command.strip()
    command = command.split("'")
    if len(command) == 1:
        command = ''.join(command[0].split())
    elif len(command) == 3:
        command = ''.join(command[0].split() + ["'" + command[1] + "'"] + command[2].split())
    else:
        print(error_msg)
        continue
    if '=' in command:
        values = command.split('=')
        if len(values) == 2 and values[1][0] == "'" and values[1][-1] == "'":
            variable_name = values[0]
            variable_value = values[1][1:-1]
            variables[variable_name] = variable_value
        else:
            print(error_msg)
    elif command.startswith('print('):
        variable = command.split('(')
        if len(variable) == 2 and variable[1][-1] == ')' and "'" not in variable[1]:
            variable = variable[1][:-1]
            try:
                if '+' in variable:
                    variable_names = variable.split('+')
                    variable_value = ''
                    for variable_name in variable_names:
                        variable_value += variables[variable_name]
                else:
                    variable_value = variables[variable]
            except KeyError:
                print(error_msg)
                continue
            print(variable_value)
        else:
            print(error_msg)
    elif command == 'quit()':
        break
    else:
        print(error_msg)