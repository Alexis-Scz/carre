taille=int(input("Taille du caré : "))
print("carré plein : ")
for n in range(1,taille):   
    print("*"*taille)  
print("Carré vide : ") 
for i in range(1,taille+1):
    if i ==1 or i==taille:  
        print("*"*taille)
    else:
        print("*"," "*(taille-2),"*")    