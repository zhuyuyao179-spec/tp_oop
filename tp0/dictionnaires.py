"""Inventaire de pièces détachées avec des dictionnaires."""


def quantite_piece(pieces_stock, modele, piece):
    """
    Retourne la quantité disponible d'une pièce pour un modèle donné
    """
    return pieces_stock[modele][piece]


def consommer_piece(pieces_stock, modele, piece, quantite):
    """
    Retire des pièces du stock 
    """
    pieces_stock[modele][piece] -= quantite


def ajouter_modele(pieces_stock, nom_modele, moteurs, capteurs, roues):
    """
    Enregistre un nouveau modèle de robot avec son stock initial.
    """
    pieces_stock[nom_modele] = {
        "moteurs": moteurs,
        "capteurs": capteurs,
        "roues": roues,
    }


def total_pieces(pieces_stock):
    """
    Calcule le total de chaque type de pièce 
    """
    totaux = {"moteurs": 0, "capteurs": 0, "roues": 0}
    for stock_modele in pieces_stock.values():
        for piece, quantite in stock_modele.items():
            totaux[piece] += quantite
    return totaux
