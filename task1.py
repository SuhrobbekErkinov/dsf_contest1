def kwargsAcceptFun(**kwargs):
    print("The received keyword arguments are:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")