pro={

}

cat={

}

dr={
    
}
ncat = int(input("Número de categorías "))

for ncat in range(ncat) :

    idc = input("Digite el id categoria ")
    nomcat = input("Digite el nombre de la categoría ")
    cat[ncat+1]={
    "ID categoría":idc,
    "Nombre categoría":nomcat    
    }

print(cat)


np = int(input("Número de productos"))

for np in range(np):

    npro = input("Digite nombre del producto ")
    idpro = input("Digite el id del producto ")
    ppro = input("Digite el precio del producto ")
    idc = input("Digite la categoria del producto ")
    pro[np+1]={
    "Nombre del producto":npro,
    "ID del producto":idpro,
    "Precio del producto":ppro,
    "Categoría del producto":idc}


print(pro)

print("")
print("")

for a in range(len(pro)):
    for b in range(len(cat)):
        if pro[a+1]["Categoría del producto"] in cat [b+1]["ID categoría"]:
            idn = pro[a+1]["ID del producto"]
            nombrepro = pro[a+1]["Nombre del producto"]
            nombrecat = cat[b+1]["Nombre categoría"]
            dr[a+1]={
                "Nombre del producto":nombrepro,
                "ID del producto":idn,
                "Nombre de la categoría":nombrecat

            }
            
print(dr)



  




        