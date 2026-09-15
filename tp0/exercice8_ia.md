# Exercice 8 : Regard critique avec un assistant IA

Assistant utilisé : GitHub Copilot, pour la relecture et les tâches annexes.

---

## 1. Activation de l'assistant IA

GitHub Copilot activé dans l'éditeur pour la relecture, la documentation et les tests.

---

## 2. Relecture de `recalibrer` (sans réécriture)

Fonction relue : `recalibrer` dans `tp0/tuples.py`.

### Remarque pertinente 1
La fonction retourne bien une **nouvelle liste** sans modifier l'originale, ce qui respecte l'immutabilité des tuples. En revanche, il serait utile de **vérifier explicitement dans les tests** que `releves` reste inchangé après l'appel — ce comportement est implicite mais non testé initialement.

### Remarque pertinente 2
Si plusieurs relevés portent le **même nom de capteur**, la fonction met à jour **tous** les tuples correspondants. Ce comportement n'est pas documenté dans la docstring et pourrait surprendre un utilisateur du journal de bord.

### Remarque incorrecte ou hors sujet
GitHub Copilot suggère d'**ajouter une validation stricte du type** avec `isinstance(nouvelle_valeur, float)` et de lever une exception si la valeur est négative. Hors sujet ici : le sujet ne demande aucune validation métier, et les capteurs peuvent légitimement renvoyer des valeurs de types variés (ex. `87.5` pour un gyroscope en degrés).

---

## 3. Test unitaire supplémentaire suggéré par GitHub Copilot

GitHub Copilot propose d'ajouter un test vérifiant que la **liste originale n'est pas modifiée** après recalibrage.

```python
def test_recalibrer_liste_originale_inchangee(self):
    """Cas limite : la liste d'origine ne doit pas être modifiée."""
    releves_copie = list(self.releves)
    recalibrer(self.releves, "laser_avant", 2.40)
    self.assertEqual(self.releves, releves_copie)
```

- **Passe-t-il ?** Oui.
- **Couvre-t-il un cas non prévu ?** Oui. Les tests existants vérifiaient le contenu de la nouvelle liste, mais pas l'immutabilité de la liste passée en argument. Ce test complète la couverture.

---

## 4. README.md : rédaction et corrections

GitHub Copilot a proposé un README initial. Corrections apportées manuellement :

| Proposition GitHub Copilot | Correction |
|----------------|------------|
| Chemin absolu `/home/yuyao/Desktop/tp_9_15` | Remplacé par `<racine-du-projet>` pour la reproductibilité |
| Absence de mention de `verify_tp0.py` | Ajouté : script de vérification des assertions du sujet |
| Pas de section sur l'exercice 8 | Ajout d'une section « Exercice 8 » avec lien vers ce fichier |

---

## 5. Message de commit généré par GitHub Copilot vs message manuel

Commit réel : ajout du test supplémentaire et du rapport exercice 8.

| Source | Message proposé |
|--------|-----------------|
| **GitHub Copilot** | `Update tests and docs` |
| **Message manuel** | `Exercice 8 : relecture IA, test d'immutabilité et rapport` |

Le message de GitHub Copilot est **trop vague** : il ne précise ni la fonction testée (`recalibrer`), ni le type de changement (test d'immutabilité, rapport exercice 8). Le message manuel est plus précis et traçable dans l'historique Git.

---

## 6. Réflexion (2–3 phrases)

L'usage le plus fiable de GitHub Copilot m'a semblé être la **relecture de code** et la **suggestion de cas de test limites** : GitHub Copilot repère rapidement des oublis (comme l'immutabilité de la liste d'entrée) que l'on peut valider soi-même. En revanche, la **génération de messages de commit** et certaines suggestions (validation de types, dataclasses) sont souvent trop génériques ou hors sujet pour un TP ciblé ; il faut systématiquement filtrer et corriger les propositions avant de les accepter.
