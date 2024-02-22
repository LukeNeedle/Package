class check:
    def is_blank(variable:str):
        """
        Checks if the string entered is empty.

        Args:
            variable (string): The variable to be checked.

        Returns:
            Boolean: The result of the check.
        """
        if variable in ["", " ", "\a", "\r", "\0"] :
            return False
        return True
    
    def is_string(variable):
        """
        Checks if the variable entered is a string.

        Args:
            variable (any): The variable to be checked.

        Returns:
            Boolean: The result of the check.
        """
        result = check.is_blank(variable)
        if result == True:
            return False
        
        try:
            str(variable)
        except:
            return False
        return True
    
    def is_number(variable:str):
        """
        Checks if the variable entered is a number.

        Args:
            variable (string): The variable to be checked.

        Returns:
            Boolean: The result of the check.
        """
        result = check.is_blank(variable)
        if result != True:
            return False
        
        try:
            int(variable)
        except:
            return False
        return True

    def is_integer(variable:str):
        """
        Checks if the variable entered is an integer.

        Args:
            variable (string): The variable to be checked.

        Returns:
            Boolean: The result of the check.
        """
        result = check.is_number(variable)
        if result != True:
            return False
        
        if float(int(variable)) == float(variable):
            return True
        return False
    
    def is_decimal(variable:str):
        """
        Checks if the variable entered is a decimal (float).

        Args:
            variable (string): The variable to be checked.

        Returns:
            Boolean: The result of the check.
        """
        result = check.is_number(variable)
        if result != True:
            return False
        return True
    
    def is_boolean(variable:str):
        """
        Checks if the variable entered is a Boolean.

        Args:
            variable (string): The variable to be checked.

        Returns:
            Boolean: The result of the check.
        """
        result = check.is_blank(variable)
        if result == True:
            return False
        
        if variable in ["True", "False"]:
            return True
        return False
    
    def to_boolean(variable:str):
        """
        An alternate version of is_boolean, this function will check that the value is either True or False then return the variable in the correct type.

        Args:
            variable (string): The variable to be checked.

        Returns:
            Boolean: The result of the conversion. It will be None if the input wasn't valid.
        """
        result = check.is_blank(variable)
        if result == True:
            return None
        
        if result not in ["0", "1"]:
            result = check.is_boolean(variable)
            if result != True:
                return None
        
        if variable == "True" or variable == "1":
            return True
        elif variable == "False" or variable == "0":
            return False
    
    def valid_email(email):
        """
        Checks if the email provided is correct.

        Args:
            email (string): The email to be checked.

        Returns:
            Boolean: The result of the check.
        """
        result = check.is_string(email)
        if result == True:
            return False
        
        import re
        
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, email):
            return True
        return False
    
    def valid_uk_postcode(postcode):
        """
        Checks if the postcode provided is correct.

        Args:
            email (string): The email to be checked.

        Returns:
            Boolean: The result of the check.
        """
        result = check.is_string(postcode)
        if result == True:
            return False
        
        import re
        
        regex = r'[A-Z][A-Z]?[0-9]( )?([0-9]|[A-Z])?[0-9][A-Z][A-Z]'
        if re.fullmatch(regex, postcode):
            return True
        return False


class ask:
    def string(message:str, end=": "):
        variable = input(f"{message}{end}")
        
        valid = check.is_string(variable)
        if valid:
            return str(variable)
        return ask.string(message, end)
    
    def integer(message:str, end=": "):
        variable = input(f"{message}{end}")
        
        valid = check.is_integer(str(variable))
        if valid:
            return int(variable)
        return ask.integer(message, end)
    
    def boolean(message:str, end=": "):
        variable = input(f"{message}{end}")
        
        variable = check.to_boolean(str(variable))
        if variable == None:
            return ask.boolean(message, end)
        return variable

    def decimal(message:str, end=": "):
        variable = input(f"{message}{end}")
        
        valid = check.is_decimal(str(variable))
        if valid:
            return float(variable)
        return ask.decimal(message, end)