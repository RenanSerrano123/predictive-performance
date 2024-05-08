VP = int(input())
FN = int(input())
FP = int(input())
VN = int(input())  
def acuracia(VP, FN, FP, VN):
    AC = float((VP+VN) / (VP + VN + FP + FN))
    return AC
def precisao(VP, FN, FP, VN):
    PR =  float(VP / (VP + FP))
    return PR
def sensibilidade(VP, FN, FP, VN):
    SENS = float(VP / (VP + FN))
    return SENS
print ("%.2f"%acuracia(VP, FN, FP, VN))
print ("%.2f"%precisao(VP, FN, FP, VN))
print ("%.2f"%sensibilidade(VP, FN, FP, VN))