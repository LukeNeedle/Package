from Packages.inputs import check
from decimal import Decimal

def number(variable, mode = ",", decimals = 2):
    variable, valid = check.decimal(variable)
    if valid:
        if mode == ",":
            return('{:,}'.format(variable))

        elif mode == "readable":
            suffixes = [ "", "K", "M", "B", "T", "Qa", "Qu", "S", "Oc", "No", 
                        "D", "Ud", "Dd", "Td", "Qt", "Qi", "Se", "Od", "Nd","V", 
                        "Uv", "Dv", "Tv", "Qv", "Qx", "Sx", "Ox", "Nx", "Tn", "Qa",
                        "Qu", "S", "Oc", "No", "D", "Ud", "Dd", "Td", "Qt", "Qi",
                        "Se", "Od", "Nd", "V", "Uv", "Dv", "Tv", "Qv", "Qx", "Sx",
                        "Ox", "Nx", "Tn", "x", "xx", "xxx", "X", "XX", "XXX", "END"] 
            
            sci_expr = [1e0, 1e3, 1e6, 1e9, 1e12, 1e15, 1e18, 1e21, 1e24, 1e27, 
                        1e30, 1e33, 1e36, 1e39, 1e42, 1e45, 1e48, 1e51, 1e54, 1e57, 
                        1e60, 1e63, 1e66, 1e69, 1e72, 1e75, 1e78, 1e81, 1e84, 1e87, 
                        1e90, 1e93, 1e96, 1e99, 1e102, 1e105, 1e108, 1e111, 1e114, 1e117, 
                        1e120, 1e123, 1e126, 1e129, 1e132, 1e135, 1e138, 1e141, 1e144, 1e147, 
                        1e150, 1e153, 1e156, 1e159, 1e162, 1e165, 1e168, 1e171, 1e174, 1e177]
            minus_buff = variable
            variable=abs(variable)
            for x in range(len(sci_expr)):
                try:
                    if variable >= sci_expr[x] and variable < sci_expr[x+1]:
                        suffix = suffixes[x]
                        if variable >= 1e3:
                            n=Decimal(variable/sci_expr[x])
                            num = str(n.to_integral() if n == n.to_integral() else round(n.normalize(), decimals))
                        else:
                            num = str(variable)
                        return num + suffix if minus_buff > 0 else "-" + num + suffix
                except IndexError:
                    print("You've reached the end")
        elif mode == "standard form":
            suffixes = [ "", "3", "6", "9", "12", "15", "18", "21", "24", "27", 
                        "30", "33", "36", "39", "42", "45", "48", "51", "54","57", 
                        "60", "63", "66", "69", "72", "75", "78", "81", "84", "87",
                        "90", "93", "96", "99", "102", "105", "108", "111", "114", "117",
                        "120", "123", "126", "129", "132", "135", "138", "141", "144", "147",
                        "150", "153", "156", "159", "162", "165", "168", "171", "174", "END"] 
            
            sci_expr = [1e0, 1e3, 1e6, 1e9, 1e12, 1e15, 1e18, 1e21, 1e24, 1e27, 
                        1e30, 1e33, 1e36, 1e39, 1e42, 1e45, 1e48, 1e51, 1e54, 1e57, 
                        1e60, 1e63, 1e66, 1e69, 1e72, 1e75, 1e78, 1e81, 1e84, 1e87, 
                        1e90, 1e93, 1e96, 1e99, 1e102, 1e105, 1e108, 1e111, 1e114, 1e117, 
                        1e120, 1e123, 1e126, 1e129, 1e132, 1e135, 1e138, 1e141, 1e144, 1e147, 
                        1e150, 1e153, 1e156, 1e159, 1e162, 1e165, 1e168, 1e171, 1e174, 1e177]
            minus_buff = variable
            variable=abs(variable)
            for x in range(len(sci_expr)):
                try:
                    if variable >= sci_expr[x] and variable < sci_expr[x+1]:
                        suffix = suffixes[x]
                        if variable >= 1e3:
                            n=Decimal(variable/sci_expr[x])
                            num = str(n)
                        else:
                            num = str(variable)
                        return num + "x10^" + suffix if minus_buff > 0 else "-" + num + "x10^-" + suffix
                except IndexError:
                    print("You've reached the end")

def string(variable, mode:str):
    variable, valid = check.string(variable)
    if valid:
        mode = mode.lower()
        if mode == "capitalize":
            return variable.capitalize()
        elif mode == "title":
            return variable.title()
        elif mode == "lower":
            return variable.lower()
        elif mode == "upper":
            return variable.upper()