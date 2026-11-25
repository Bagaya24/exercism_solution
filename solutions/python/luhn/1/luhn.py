"""
The Global Verification Authority modul
"""
class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        """
        This function dermine whether a number is valid according to the Luhn formula
        """
        inverse_card = list(self.card_num[::-1].replace(" ", ""))
        
        if len(inverse_card) <= 1:
            return False
        for num in inverse_card:
            if not num.isalnum():
                return False
        
            
        double = 1
        index = 1
        somme = 0
        
        for num in inverse_card[1::2]:
        
            double = int(num) * 2
            if double > 9:
                double = double - 9
            inverse_card[index] = str(double)
            index += 2
        for num in inverse_card:
            if not num.isdigit():
                return False
            somme += int(num)
        if somme % 10 == 0:
            return True
        return False
        
