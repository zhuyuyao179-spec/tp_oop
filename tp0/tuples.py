"""Journal de bord d'un robot explorateur avec des tuples."""
def afficher_releve(releve):
    """
    Retourne une description textuelle d'un relevé capteur.
    """
    nom_capteur, valeur, unite = releve
    return f"Capteur {nom_capteur} : {valeur} {unite}"


def recalibrer(releves, nom_capteur, nouvelle_valeur):
    """
    Reconstruit la liste des relevés avec une nouvelle valeur pour un capteur.
    """
    nouveaux_releves = []
    for releve in releves:
        nom, _, unite = releve
        if nom == nom_capteur:
            nouveaux_releves.append((nom, nouvelle_valeur, unite))
        else:
            nouveaux_releves.append(releve)
    return nouveaux_releves
