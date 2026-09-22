"""Classes Habitant, Adulte et Enfant."""

from abc import ABC, abstractmethod

from multipledispatch import dispatch

AGE_RETRAITE = 62


class Habitant(ABC):
    """Classe abstraite représentant un habitant du village."""

    def __init__(self, nom, age, adresse, animaux=None, prenom=""):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age
        self.__adresse = adresse
        self.__animaux = dict(animaux) if animaux is not None else {}

    @property
    def nom(self):
        """Nom de famille (ou nom unique si pas de prénom)."""
        return self.__nom

    @property
    def age(self):
        """Âge de l'habitant."""
        return self.__age

    @age.setter
    def age(self, valeur):
        if valeur < 0 or valeur > 130:
            raise ValueError("L'age doit etre compris entre 0 et 130.")
        self.__age = valeur

    def get_nom(self):
        """Retourne le nom de famille."""
        return self.__nom

    def get_prenom(self):
        """Retourne le prénom."""
        return self.__prenom

    def get_age(self):
        """Retourne l'âge."""
        return self.__age

    def get_adresse(self):
        """Retourne l'adresse."""
        return self.__adresse

    def get_animaux(self):
        """Retourne le dictionnaire des animaux."""
        return self.__animaux

    def set_nom(self, nom):
        """Modifie le nom de famille."""
        self.__nom = nom

    def set_age(self, age):
        """Modifie l'âge avec validation."""
        self.age = age

    def set_adresse(self, adresse):
        """Modifie l'adresse."""
        self.__adresse = adresse

    def set_animaux(self, animaux):
        """Remplace le dictionnaire des animaux."""
        self.__animaux = dict(animaux)

    def _nom_affichage(self):
        """Construit le nom complet pour l'affichage."""
        if self.__prenom and self.__nom:
            return f"{self.__prenom} {self.__nom}"
        if self.__prenom:
            return self.__prenom
        return self.__nom

    def affichage_adresse(self):
        """Affiche une phrase indiquant où habite l'habitant."""
        print(f"{self._nom_affichage()} habite a {self.__adresse}")

    def compte_animal(self, animal):
        """Retourne le nombre d'animaux possédés pour un type donné."""
        return self.__animaux.get(animal, 0)

    def __str__(self):
        """Représentation textuelle de l'habitant."""
        return (
            f"{self._nom_affichage()}, {self.__age} ans, "
            f"habite a {self.__adresse}"
        )

    @abstractmethod
    def calcul_nombre_annee_avant_retraite(self):
        """Calcule le nombre d'années restantes avant la retraite."""


class Adulte(Habitant):
    """Habitant adulte (18 ans ou plus)."""

    def __init__(self, nom, prenom, age, adresse, animaux=None):
        if age < 18:
            raise ValueError("Un adulte doit avoir au moins 18 ans.")
        super().__init__(nom, age, adresse, animaux, prenom=prenom)

    def calcul_nombre_annee_avant_retraite(self):
        """Retourne les années avant la retraite ou un message adapté."""
        if self.age >= AGE_RETRAITE:
            return "Deja a la retraite"
        return AGE_RETRAITE - self.age


class Enfant(Habitant):
    """Habitant enfant (moins de 18 ans)."""

    def __init__(self, nom, prenom, age, adresse, animaux=None):
        if age >= 18:
            raise ValueError("Un enfant doit avoir moins de 18 ans.")
        super().__init__(nom, age, adresse, animaux, prenom=prenom)

    def calcul_nombre_annee_avant_retraite(self):
        """Un enfant ne peut pas calculer sa retraite."""
        return "Erreur: un enfant ne peut pas calculer sa retraite"


# pylint: disable=function-redefined
@dispatch(Habitant, str)
def set_info(habitant_obj, nom):
    """Met à jour uniquement le nom de l'habitant."""
    habitant_obj.set_nom(nom)


@dispatch(Habitant, str, int)
def set_info(habitant_obj, nom, age):
    """Met à jour le nom et l'âge de l'habitant."""
    habitant_obj.set_nom(nom)
    habitant_obj.age = age
# pylint: enable=function-redefined
