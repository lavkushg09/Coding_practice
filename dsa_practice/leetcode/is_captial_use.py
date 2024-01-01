class IsCapitalUse:
    def is_capital_use(self, str_ins):
        count = 0 
        for i in range(len(str_ins)):
            if str_ins[i] >= chr(65) and str_ins[i] < chr(91):
                count +=1

        if count == len(str_ins):
            return True
        elif count == 0:
            return True
        elif count == 1 and str_ins[0] >= chr(65) and str_ins[0] < chr(91):
            return True
        else:
            return False