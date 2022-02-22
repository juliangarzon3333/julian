invitados=[]
for i in range (10):
    invitados .append(input("invitados "))
print(invitados)

otro=input("¿quiere añadir mas invitados? ")

while otro =="si":
    invitados.append(input("nombre delinvitados"))
    print(invitados)
    otro=input("desea agregar otro")
print("usted tiene ",len(invitados),"invitados")
invitados.sort()
print(invitados)





