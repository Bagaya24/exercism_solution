def leap_year(year):
    """
        This function see if a year is leap or not
        :param year(int)
        :return boolean
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False
    
