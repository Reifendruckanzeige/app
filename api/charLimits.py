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
    match level:
        case "1":
            return "10 até 20"
        case "2":
            return "21 até 30"
        case "3":
            return "31 até 40"
        case "4":
            return "41 até 50"
        case "5":
            return "51 até 60"
        case _:
            return "10 - 60"