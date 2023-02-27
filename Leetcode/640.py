import re

class Solution:
    def solveEquation(self, equation: str) -> str:
        ptn = re.compile("(\=?)|(\+|\-|)?(\-|\d+)?(x|\d+)?")
        # text = "x+15-3+x=6+x-2"
        quads = ptn.findall(equation)
        
        # convert to ax+agg_value=0
        x = 0
        sign = 1
        agg_value = 0
        for e, op, val, is_x in quads:
            if e == "" and op == "" and val == "" and is_x == "":
                continue
            if  op == "":
                op = "+"
            if e == "=":
                sign = -1
                continue
                
            val_sign = -1 if op == "-" else 1
            val_sign *= sign
            if is_x == "":
                agg_value += val_sign * int(val)
            else:
                if val == "":
                    val = 1
                x += val_sign * int(val)
        
        if x == 0:
            if agg_value != 0:
                return "No solution"
            else:
                return "Infinite solutions"
        else:
            return f"x={int(-agg_value/x)}"
                
        