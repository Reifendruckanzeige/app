def getAttrsLimits(level):
    if level == "1":
        return "-2 até 4"
    elif level == "2":
        return "5 até 8"
    elif level == "3":
        return "9 até 12"
    elif level == "4":
        return "13 até 16"
    elif level == "5":
        return "17 até 20"
    else:
        return "0 - 20"
    
def getHpLimits(level):
    if level == "1":
        result = "10 até 20"
    elif level == "2":
        result = "21 até 30"
    elif level == "3":
        result = "31 até 40"
    elif level == "4":
        result = "41 até 50"
    elif level == "5":
        result = "51 até 60"
    else:
        result = "10 - 60"
