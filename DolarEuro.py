
print("1 de dolares a euros")
print("2 de euros a dolares")

print ("")
hl=int(input("Elija su opción: "))
print ("")

if hl==1:
    dol3=int(input("introdusca cantidad de dolares: "))
    euros=dol3*0.96
    print("")
    print("dolares=", euros)
if hl==2:
    euros1=int(input("introduzca dolares:"))
    dol4=euros1/1.04
    print("")
    print("euros=", dol4)

