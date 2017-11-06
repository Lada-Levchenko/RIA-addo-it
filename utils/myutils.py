from IAPDclasses import GeneratedsSuper


def recursive_representation(rootObject, iteration=-1):
    iteration += 1
    tab = '  '*iteration
    print(tab + '{')
    iteration = 0
    for key, value in rootObject.__dict__.iteritems():
        print(tab + '"' + key + '": ')
        if isinstance(value, GeneratedsSuper):
            recursive_representation(value, iteration)
        elif type(value) is list:
            print(tab + '[')
            for index in range(len(value)):
                if isinstance(value[index], GeneratedsSuper):
                    recursive_representation(value[index], iteration)
                else:
                    print(tab + str(value[index]) + '"')
                if index < len(value) - 1:
                    print(',')
            print(tab + ']')
        else:
            print(tab + '    "' + str(value) + '"')
        if iteration < len(rootObject.__dict__.items()) - 1:
            print(tab + ',')
        iteration += 1
    print(tab + '}')