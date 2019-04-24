# Napisi program, ki izpise vsa prastevila majnsa od 200
   
# def je_prastevilo(n):
#     if n % (!=n) == 0 and (x != 1):
#         return False
#     else:
#         return True
#  seznam = []
# def prastevila(stevila):
#     if je_prastevilo(n)
def je_prastevilo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for x in range(2, 201):
    if je_prastevilo(x):
        print(y)
