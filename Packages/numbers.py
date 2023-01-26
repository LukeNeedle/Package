from Packages.inputs import check

class format:
    def number(variable):
        variable, valid = check.decimal(variable)
        if valid:
            return('{:,}'.format(variable))
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