tva=float(input("entrer la valeur:"))
remise=float(input("entrer la valeur:"))
n_clients=int(input("entrer le num de client:"))
nom=[]
facture=[]
for  i in range(1,n_clients +1):
    nom_complet=input(f"\nentrer le nom complet de client num (i):")
    nom.append(nom_complet)
    n_element=int(input(f"entrer l element:"))
    sum=0
    for j in range(1, n_element+1):
        pht=float(input(f"entrer le prix hors taxe:"))
        ttc=pht* (1 + tva/100)
        sum+=ttc
    total=sum-sum*remise/100
    facture.append(total)
print("\nfacture:", total)
for a in range (0,n_clients):
    print(f"facture total de client",{nom[a]},"est",{facture[a]:.2f})