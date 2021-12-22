while True:
    idstr = input("请输入需要分配密码的用户ID，以空格键分隔：")
    idls = idstr.split(' ')
    idt = tuple(idls)
    for i in idt:
        idls.remove(i)
        if i in idls:
            val = False
            break
        else:
            val = True
            continue
    if val:
        print(list(idt))
        break
    else:
        print("您输入用户ID有重复，请重新输入！")
        continue