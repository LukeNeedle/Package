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
            return variable, True
    
    def integer(variable):
        variable, valid = check.blank(variable)
        if not valid:
            return variable, False        
        
        if not variable.isdigit():
            return variable, False
        else:
            return variable, True
class ask:
    def string(message:str):
        variable = input(message)
        variable, valid = check.string(variable)
        if valid:
            return str(variable)
        else:
            return str(ask.string(message))
    
    def integer(message:str):
        variable = input(message)
        variable, valid = check.integer(variable)
        if valid:
            return int(variable)
        else:
            return int(ask.integer(message))