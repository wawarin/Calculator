def cal():
    while True:
        eq = (input(">>"))
        if type(eq) == int or float:
            print(eval(eq))
        else:
            print("Syntax Error")
            break
cal()