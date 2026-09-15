"""Vérifie que toutes les assertions du sujet TP0 passent."""

from tp0.dictionnaires import (
    ajouter_modele,
    consommer_piece,
    quantite_piece,
    total_pieces,
)
from tp0.ensembles import (
    ajouter_robot_mission,
    retirer_robot_mission,
    robots_double_mission,
    robots_exploration_seulement,
    robots_toutes_missions,
)
from tp0.qualite import cout_deplacement_propre
from tp0.tuples import afficher_releve, recalibrer


def verifier_exercice_3():
    """Vérifie les tuples."""
    releve1 = ("laser_avant", 2.35, "m")
    releve2 = ("laser_arriere", 1.10, "m")
    releve3 = ("gyroscope", 87.5, "deg")
    releves = [releve1, releve2, releve3]
    assert len(releves) == 3
    assert releves[0][0] == "laser_avant"
    assert afficher_releve(releve1) == "Capteur laser_avant : 2.35 m"

    nouveaux_releves = recalibrer(releves, "laser_avant", 2.40)
    assert nouveaux_releves[0] == ("laser_avant", 2.40, "m")
    assert nouveaux_releves[1] == releve2
    assert nouveaux_releves[2] == releve3


def verifier_exercice_4():
    """Vérifie les ensembles."""
    robots_exploration = {"R2", "R5", "R7"}
    robots_transport = {"R5", "R9", "R7", "R3"}

    double_mission = robots_double_mission(robots_exploration, robots_transport)
    toutes_missions = robots_toutes_missions(robots_exploration, robots_transport)
    exploration_seule = robots_exploration_seulement(
        robots_exploration, robots_transport
    )
    assert double_mission == {"R5", "R7"}
    assert toutes_missions == {"R2", "R3", "R5", "R7", "R9"}
    assert exploration_seule == {"R2"}

    ajout = ajouter_robot_mission(robots_exploration, "R8")
    retrait = retirer_robot_mission(robots_transport, "R9")
    assert ajout == {"R2", "R5", "R7", "R8"}
    assert retrait == {"R3", "R5", "R7"}
    assert robots_transport == {"R5", "R9", "R7", "R3"}


def verifier_exercice_5():
    """Vérifie les dictionnaires."""
    pieces_stock = {
        "ModeleA": {"moteurs": 10, "capteurs": 25, "roues": 40},
        "ModeleB": {"moteurs": 6, "capteurs": 15, "roues": 24},
    }
    assert quantite_piece(pieces_stock, "ModeleA", "moteurs") == 10

    consommer_piece(pieces_stock, "ModeleA", "moteurs", 3)
    assert pieces_stock["ModeleA"]["moteurs"] == 7

    ajouter_modele(pieces_stock, "ModeleC", moteurs=4, capteurs=10, roues=16)
    assert pieces_stock["ModeleC"] == {"moteurs": 4, "capteurs": 10, "roues": 16}

    totaux = total_pieces(pieces_stock)
    assert totaux == {"moteurs": 17, "capteurs": 50, "roues": 80}


def verifier_exercice_6():
    """Vérifie la fonction refactorisée."""
    assert cout_deplacement_propre("R", 0, 0, 3, 4) == 5.0
    assert cout_deplacement_propre("H", 0, 0, 3, 4) == 7.5


if __name__ == "__main__":
    verifier_exercice_3()
    print("Exercice 3 : OK")
    verifier_exercice_4()
    print("Exercice 4 : OK")
    verifier_exercice_5()
    print("Exercice 5 : OK")
    verifier_exercice_6()
    print("Exercice 6 : OK")
    print("Toutes les vérifications du sujet passent.")
