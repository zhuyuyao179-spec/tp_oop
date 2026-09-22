"""Tests unitaires pour le TP2."""

import unittest
from unittest import mock

from tp2.habitant import Adulte, Enfant, Habitant, set_info
from tp2.personnes import affichage
from tp2.village import Village


class TestHabitant(unittest.TestCase):
    """Tests pour la classe Habitant et l'encapsulation."""

    def setUp(self):
        self.habitant = Adulte("Aldric", "", 25, "Rue A", {"vaches": 3})

    def test_attributs_constructeur(self):
        """Cas usuel : création avec animaux."""
        self.assertEqual(self.habitant.nom, "Aldric")
        self.assertEqual(self.habitant.compte_animal("vaches"), 3)

    def test_compte_animal_absent(self):
        """Cas limite : animal non possédé."""
        self.assertEqual(self.habitant.compte_animal("moutons"), 0)

    def test_age_setter_valide(self):
        """Cas usuel : modification d'âge valide."""
        self.habitant.age = 26
        self.assertEqual(self.habitant.age, 26)

    def test_age_setter_invalide(self):
        """Cas limite : âge négatif."""
        with self.assertRaises(ValueError):
            self.habitant.age = -5

    def test_set_info_nom_seul(self):
        """Surcharge set_info avec un seul argument."""
        h2 = Adulte("Bob", "", 40, "Rue C")
        set_info(h2, "Robert")
        self.assertEqual(h2.get_nom(), "Robert")

    def test_set_info_nom_et_age(self):
        """Surcharge set_info avec nom et âge."""
        h2 = Adulte("Bob", "", 40, "Rue C")
        set_info(h2, "Robert", 41)
        self.assertEqual(h2.get_nom(), "Robert")
        self.assertEqual(h2.age, 41)


class TestVillage(unittest.TestCase):
    """Tests pour la classe Village."""

    def test_composition(self):
        """Ajout par composition."""
        pytown = Village("PyTown")
        pytown.ajouter_habitant_composition("Aldric", 25, "Rue A", {"vaches": 3})
        self.assertEqual(len(pytown.get_habitants()), 1)

    def test_agregation_deux_villages(self):
        """Cas limite : même habitant agrégé dans deux villages."""
        pytown = Village("PyTown")
        voisin = Village("VillageVoisin")
        elise = Adulte("Elise", "", 28, "Rue B", {"poules": 10})
        pytown.ajouter_habitant_agregation(elise)
        voisin.ajouter_habitant_agregation(elise)
        self.assertIn(elise, pytown.get_habitants())
        self.assertIn(elise, voisin.get_habitants())


class TestHeritage(unittest.TestCase):
    """Tests pour Adulte, Enfant et la retraite."""

    def setUp(self):
        self.adulte = Adulte("Dupont", "Marie", 35, "Rue A")
        self.enfant = Enfant("Martin", "Lucas", 12, "Rue B")

    def test_adulte_retraite(self):
        """Cas usuel : adulte en activité."""
        self.assertEqual(self.adulte.calcul_nombre_annee_avant_retraite(), 27)

    def test_enfant_retraite(self):
        """Cas usuel : message d'erreur pour un enfant."""
        message = self.enfant.calcul_nombre_annee_avant_retraite()
        self.assertIn("enfant", message)

    def test_enfant_age_invalide(self):
        """Cas limite : enfant de 20 ans."""
        with self.assertRaises(ValueError):
            Enfant("Test", "Oups", 20, "Rue C")

    def test_habitant_abstrait(self):
        """Impossible d'instancier Habitant directement."""
        with self.assertRaises(TypeError):
            Habitant(  # pylint: disable=abstract-class-instantiated
                "Seul", 30, "Rue Z"
            )

    def test_polymorphisme_affichage(self):
        """affichage() fonctionne pour Adulte et Enfant sans isinstance."""
        with mock.patch("builtins.print") as mock_print:
            affichage(self.adulte)
            affichage(self.enfant)
        self.assertEqual(mock_print.call_count, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
