from Domain.Librarie import get_id, get_gen, get_titlu, get_pret, get_reducere, create_librarie

def aplicare_discount(librarie):
    """
       Aplica discount in functie de reducere
       :param lista: lista de vanzari
       :return: o lista continand atat vanzarile reduse cat si cele nemodificate
       """
    librarie_reducere = []
    for carte in librarie:
        if get_reducere(carte) == "silver":
            carte_noua = create_librarie(
                get_id(carte),
                get_titlu(carte),
                get_gen(carte),
                get_pret(carte) - 5 / 100 * get_pret(carte),
                get_reducere(carte)
            )
            librarie_reducere.append(carte_noua)
        elif get_reducere(carte) == "gold":
            carte_noua = create_librarie(
                get_id(carte),
                get_titlu(carte),
                get_gen(carte),
                get_pret(carte) - 1 / 10 * get_pret(carte),
                get_reducere(carte)
            )
            librarie_reducere.append(carte_noua)
        else:
            librarie_reducere.append(carte)

    return librarie_reducere