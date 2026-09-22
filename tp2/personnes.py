"""Affichage polymorphe des habitants."""

from tp2.habitant import Habitant


def affichage(h: Habitant):
    """Affiche un habitant via son interface commune (polymorphisme)."""
    print(str(h))


# Habitant est abstrait : Adulte et Enfant redéfinissent calcul_nombre_annee_avant_retraite.
