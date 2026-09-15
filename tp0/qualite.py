"""Fonctions de calcul du coût énergétique avec une qualité de code améliorée."""

COEFFICIENTS_TERRAIN = {
    "R": 1.0,
    "H": 1.5,
    "S": 2.0,
}
COEFFICIENT_TERRAIN_INCONNU = 3.0


def calculer_distance(x1, y1, x2, y2):
    """
    Calcule la distance euclidienne entre deux points.
    """
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def cout_deplacement_propre(type_terrain, x1, y1, x2, y2):
    """
    Calcule le coût énergétique d'un déplacement selon le type de terrain.
    """
    distance = calculer_distance(x1, y1, x2, y2)
    coefficient = COEFFICIENTS_TERRAIN.get(type_terrain, COEFFICIENT_TERRAIN_INCONNU)
    return distance * coefficient
