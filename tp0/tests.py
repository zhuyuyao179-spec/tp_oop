"""Tests unitaires pour le TP0."""
import copy
import unittest

from tp0.dictionnaires import consommer_piece, total_pieces
from tp0.ensembles import ajouter_robot_mission, robots_double_mission
from tp0.tuples import afficher_releve, recalibrer


class TestJournalDeBord(unittest.TestCase):
    """Tests pour les fonctions sur les relevés.""" 

    def setUp(self):
        """Prépare des relevés."""
        self.releve1 = ("laser_avant", 2.35, "m")
        self.releve2 = ("laser_arriere", 1.10, "m")
        self.releve3 = ("gyroscope", 87.5, "deg")
        self.releves = [self.releve1, self.releve2, self.releve3]

    def test_afficher_releve(self):
        """affichage d'un relevé capteur."""
        resultat = afficher_releve(self.releve1)
        self.assertEqual(resultat, "Capteur laser_avant : 2.35 m")

    def test_recalibrer_capteur_existant(self):
        """recalibrage d'un capteur présent."""
        nouveaux_releves = recalibrer(self.releves, "laser_avant", 2.40)
        self.assertEqual(nouveaux_releves[0], ("laser_avant", 2.40, "m"))
        self.assertEqual(nouveaux_releves[1], self.releve2)
        self.assertEqual(nouveaux_releves[2], self.releve3)

    def test_recalibrer_capteur_absent(self):
        """le capteur demandé n'existe pas."""
        nouveaux_releves = recalibrer(self.releves, "camera", 1.0)
        self.assertEqual(nouveaux_releves, self.releves)

    def test_recalibrer_liste_originale_inchangee(self):
        """la liste d'origine ne doit pas être modifiée."""
        releves_copie = list(self.releves)
        recalibrer(self.releves, "laser_avant", 2.40)
        self.assertEqual(self.releves, releves_copie)


class TestFlotteRobots(unittest.TestCase):
    """Tests pour les fonctions sur les ensembles de robots."""

    def setUp(self):
        """Prépare les ensembles de robots de test."""
        self.robots_exploration = {"R2", "R5", "R7"}
        self.robots_transport = {"R5", "R9", "R7", "R3"}

    def test_robots_double_mission(self):
        """robots affectés aux deux missions."""
        double_mission = robots_double_mission(
            self.robots_exploration, self.robots_transport
        )
        self.assertEqual(double_mission, {"R5", "R7"})

    def test_ajouter_robot_mission_nouveau(self):
        """ajout d'un robot absent de la mission."""
        ajout = ajouter_robot_mission(self.robots_exploration, "R8")
        self.assertEqual(ajout, {"R2", "R5", "R7", "R8"})
        self.assertEqual(self.robots_exploration, {"R2", "R5", "R7"})

    def test_ajouter_robot_mission_deja_present(self):
        """ajout d'un robot déjà présent dans l'ensemble."""
        ajout = ajouter_robot_mission(self.robots_exploration, "R5")
        self.assertEqual(ajout, {"R2", "R5", "R7"})
        self.assertEqual(len(ajout), 3)


class TestInventaire(unittest.TestCase):
    """Tests pour les fonctions sur l'inventaire de pièces."""

    def setUp(self):
        """Prépare un stock de pièces de test."""
        self.pieces_stock = {
            "ModeleA": {"moteurs": 10, "capteurs": 25, "roues": 40},
            "ModeleB": {"moteurs": 6, "capteurs": 15, "roues": 24},
        }

    def test_consommer_piece(self):
        """consommation de pièces pour une réparation."""
        stock = copy.deepcopy(self.pieces_stock)
        consommer_piece(stock, "ModeleA", "moteurs", 3)
        self.assertEqual(stock["ModeleA"]["moteurs"], 7)

    def test_total_pieces(self):
        """total des pièces pour un stock non vide."""
        totaux = total_pieces(self.pieces_stock)
        self.assertEqual(totaux, {"moteurs": 16, "capteurs": 40, "roues": 64})

    def test_total_pieces_stock_vide(self):
        """stock ne contenant aucun modèle."""
        totaux = total_pieces({})
        self.assertEqual(totaux, {"moteurs": 0, "capteurs": 0, "roues": 0})


if __name__ == "__main__":
    unittest.main(verbosity=2)
