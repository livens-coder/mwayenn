while True:

    print("Pwogram sa ka kalkile mwayenn ou epi klasifyew")
    print("***********************************************************************")
    nbre=int(input("konbyen not wap rantre: "))
    if nbre<1:
        print(" Fok ou rantre pou pi piti yon not")
        nbre=int(input("konbyen not wap rantre: "))
    n=0
    list_not=[]
    somme=0
    for n in range(nbre):
        nott=float(input("rantre yon not:   "))
        if nott<0 or nott>100:
            print("Tanpri, rantre yon not ki varye ant 0 a 100")
            nott=float(input("rantre yon not:   "))
        list_not.append(nott)
        n+=1
    #print(list_not) 
    for n in list_not:
        somme+=n 
    mwayenn=somme/nbre
    print("-------------")
    print ("Ou fe mwayenn", mwayenn ,"/100" )
    if mwayenn >= 90:
        print(" mansyon ** A **")
    elif mwayenn < 90 and mwayenn >= 80:
         print(" mansyon ** B **")
    elif mwayenn < 80 and  mwayenn >= 70:
        print(" mansyon ** C **")
    elif mwayenn < 70 and mwayenn >= 60:
        print(" mansyon ** D **")
    else :
        print(" mansyon ** E **")
    

    print("..................................................................................")
    vol=input("Eske ou vle fe lot kalkil? (w/n): ")
    if vol.lower() != "w":
        print("Mesi paske ou t itilize pwogram sa pou fe kalkil mwayenn")
        break
 
