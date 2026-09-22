"""Classe Village : composition et agrégation."""

from tp2.habitant import Adulte, Enfant, Habitant


class Village:
    """Représente un village et la liste de ses habitants."""

    def __init__(self, nom):
        self.__nom = nom
        self.__habitants = []

    def get_nom(self):
        """Retourne le nom du village."""
        return self.__nom

    def get_habitants(self):
        """Retourne la liste des habitants."""
        return list(self.__habitants)

    def ajouter_habitant_composition(self, nom, age, adresse, animaux=None):
        """Crée un habitant et l'ajoute au village (composition)."""
        if age >= 18:
            nouvel_habitant = Adulte(nom, "", age, adresse, animaux)
        else:
            nouvel_habitant = Enfant(nom, "", age, adresse, animaux)
        self.__habitants.append(nouvel_habitant)

    def ajouter_habitant_agregation(self, habitant):
        """Ajoute un habitant existant au village (agrégation)."""
        if not isinstance(habitant, Habitant):
            raise TypeError("L'objet doit etre un Habitant.")
        self.__habitants.append(habitant)

    def afficher_habitants(self):
        """Affiche chaque habitant du village."""
        for habitant in self.__habitants:
            print(habitant)


# Composition : le village crée l'habitant (ajouter_habitant_composition).
# Agrégation : le village ajoute un habitant déjà créé (ajouter_habitant_agregation).
