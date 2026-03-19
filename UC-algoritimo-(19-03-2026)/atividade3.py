fogo = bool(input("magia de fogo? (True/False): "))
agua = bool(input("magia de água? (True/False): "))

def tipo_magia(fogo, agua):
    if fogo and agua:
        return 
        print("vapor")
    elif fogo and not agua:
        return
        print("fogo")
    elif not fogo and agua:
        return 
        print("água")
    else:
        return 
        print("sem magia")