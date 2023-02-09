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
        if variable == "True":
            return True, True
        elif variable == "False":
            return False, True
        if variable not in ["True", "False"]:
            return variable, False

class ask:
    def string(message:str, end=": "):
        variable = input(f"{message}{end}")
        variable, valid = check.string(variable)
        if valid:
            return variable
        else:
            return ask.string(message, end)
    
    def integer(message:str, end=": "):
        variable = input(f"{message}{end}")
        variable, valid = check.integer(variable)
        if valid:
            return variable
        else:
            return ask.integer(message, end)
    
    def boolean(message:str, end=": "):
        variable = input(f"{message}{end}")
        variable, valid = check.boolean(variable)
        if valid:
            return variable
        else:
            return ask.boolean(message, end)

    def decimal(message:str, end=": "):
        variable = input(f"{message}{end}")
        variable, valid = check.decimal(variable)
        if valid:
            return variable
        else:
            return ask.decimal(message, end)