class check:
    def blank(variable):
        if variable == "":
            return variable, False
        if variable == " ":
            return variable, False
        else:
            return variable, True
    
    def string(variable):
        variable, valid = check.blank(variable)
        if not valid:
            return variable, False
        
        if not variable.isalpha():
            return variable, False
        else:
            return str(variable), True
    
    def number(variable):
        variable, valid = check.blank(variable)
        if not valid:
            return variable, False        
        try:
            variable = int(variable)
        except:
            try:
                variable = float(variable)
            except:
                return variable, False
            else:
                return variable, True
        else:
            return variable, True

    def integer(variable):
        variable, valid = check.blank(variable)
        if not valid:
            return variable, False        
        
        variable, valid = check.number(variable)
        if not valid:
            return variable, False
        
        if variable % 1 != 0:
            return variable, False
        else:
            return int(variable), True
    
    def decimal(variable):
        variable, valid = check.blank(variable)
        if not valid:
            return variable, False
        
        variable, valid = check.number(variable)
        if not valid:
            return variable, False
        else:
            return float(variable), True
    
    def boolean(variable):
        if variable not in ["True", "False"]:
            return variable, False
        else:
            return bool(variable), True

class ask:
    def string(message:str):
        variable = input(f"{message}: ")
        variable, valid = check.string(variable)
        if valid:
            return variable
        else:
            return ask.string(message)
    
    def integer(message:str):
        variable = input(f"{message}: ")
        variable, valid = check.integer(variable)
        if valid:
            return variable
        else:
            return ask.integer(message)
    
    def boolean(message:str):
        variable = input(f"{message}: ")
        variable, valid = check.boolean(variable)
        if valid:
            return variable
        else:
            return ask.boolean(message)

    def decimal(message:str):
        variable = input(f"{message}: ")
        variable, valid = check.decimal(variable)
        if valid:
            return variable
        else:
            return ask.decimal(message)