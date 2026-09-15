# tp_oop

TP Programmation Orientée Objet

## Contenu de tp0

| Fichier | Description |
|---------|-------------|
| `tuples.py` | Journal de bord du robot |
| `ensembles.py` | Coordination d'une flotte de robots |
| `dictionnaires.py` | Inventaire de pièces détachées |
| `qualite.py` | Calcul du coût énergétique (version refactorisée) |
| `tests.py` | Tests unitaires |
| `exercice8_ia.md` | Rapport de l'exercice 8 |

## Environnement

### Avec Conda

```bash
conda create -n tp_oop python=3.11
conda activate tp_oop
conda install conda-forge::pylint
```

## Lancer les tests

```bash
python -m unittest tp0.tests -v
```

## Vérifier les assertions du sujet

```bash
python verify_tp0.py
```

## Vérifier la qualité du code

```bash
pylint tp0/*.py
```

## Exercice 8

Le rapport de relecture IA, le test supplémentaire suggéré et la réflexion sont dans `tp0/exercice8_ia.md`.
