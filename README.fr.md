# Projet de Chiffrement César en Python

[FR](README.fr.md) | [EN](README.md)

## Description

Ce projet est un script en Python qui implémente le chiffrement de César. Il peut être exécuté en ligne de commande pour chiffrer ou déchiffrer des textes.
Le script travaille uniquement sur les lettres de l'alphabet (après conversion en minuscules) et ignore tous les autres caractères (espaces, chiffres, ponctuations, etc.).

---

### Table des matières

- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Fonctionnement](#fonctionnement)
- [Suggestions d'améliorations](#suggestions-daméliorations)
- [Licence](#licence)
- [Auteur](#auteur)

---

## Fonctionnalités

**Chiffrement/Déchiffrement**

- Permet de chiffrer ou déchiffrer du texte en appliquant un décalage défini sur chaque lettre de l'alphabet.
- Les lettres sont converties en minuscules et seules les lettres de A à Z sont traitées.

**Modes de traitement**

- Mode texte : Le texte à traiter est passé en argument dans la ligne de commande.
- Mode fichier : Le script peut lire le texte dans un fichier, le traiter et réécrire le résultat dans le même fichier ou dans un fichier de sortie spécifié.

**Options en ligne de commande**

- Le script utilise le module argparse pour offrir une aide détaillée et vérifier la validité des arguments transmis.

## Prérequis

Python 3.x doit être installé sur votre machine.

## Installation

Cloner le dépôt (ou télécharger le script) :

```bash
git clone https://github.com/votre-utilisateur/nom-du-repository.git
cd nom-du-repository
```

Rendre le script exécutable (optionnel) :

```bash
chmod +x main.py
```

Lancez le script depuis la ligne de commande avec la syntaxe suivante :

```bash
python main.py [-c SHIFT | -d SHIFT] [-f FICHIER] [-o FICHIER_SORTIE] [TEXTE]
```

**Chiffrement d'un texte passé en argument**

Pour chiffrer le texte "abc" avec un décalage de 2 :

```bash
python main.py -c 2 "abc"
```

Sortie attendue :

```nginx
cde
```

**Déchiffrement d'un texte passé en argument**

Pour déchiffrer le texte "cde" avec un décalage de 2 :

```bash
python main.py -d 2 "cde"
```

Sortie attendue :

```nginx
abc
```

**Chiffrement d'un fichier**

Si le fichier fichier.txt contient par exemple "Abc, XYZ! 123", le script traitera seulement les lettres (après conversion en minuscules) et ignorera les caractères non alphabétiques :

```bash
python main.py -c 27 -f fichier.txt
```

Le résultat sera écrit dans le même fichier (sauf si l'option -o est utilisée). Par exemple, pour un décalage de 27, on pourrait obtenir :

Résultat affiché :

```nginx
abcya
```

**Spécifier un fichier de sortie**

Pour écrire le résultat dans un autre fichier et ne pas écraser l'original :

```bash
python main.py -c 27 -f fichier.txt -o resultat.txt
```

Le résultat sera écrit dans resultat.txt et sera également affiché dans la console.

## Fonctionnement

Le chiffrement de César réalisé par ce script fonctionne de la manière suivante :

### Conversion en minuscules :

Toutes les lettres sont transformées en minuscules.

### Traitement des lettres uniquement :

Seules les lettres de l'alphabet (A à Z) sont chiffrées/déchiffrées. Les autres caractères ne sont pas pris en compte dans le résultat final.

### Décalage cyclique :

L'opération de décalage est réalisée modulo 26, ce qui permet d'utiliser des clés supérieures à 26.

**Options disponibles**

- -c SHIFT : Chiffrer le texte avec le décalage spécifié.

- -d SHIFT : Déchiffrer le texte avec le décalage spécifié.

- -f, --file FICHIER : Spécifie le fichier à traiter.

- -o, --output FICHIER_SORTIE : (Optionnel) Spécifie le fichier de sortie. Par défaut, le fichier d'entrée est écrasé.

- -h, --help : Affiche l'aide d'utilisation du script.

## Suggestions d'améliorations

- [ ] Mode interactif : Ajouter une interface en ligne de commande qui guide l'utilisateur étape par étape.

- [ ] Traitement de plusieurs fichiers : Permettre le chiffrement/déchiffrement par lot.

- [ ] Ajout d'autres algorithmes : Intégrer d'autres systèmes de chiffrement (ex : chiffre de Vigenère).

- [ ] Tests unitaires : Mettre en place une suite de tests pour garantir la robustesse du code.

- [ ] Interface graphique : Développer une interface utilisateur avec Tkinter ou une autre bibliothèque.

## Licence

Sous Licence MIT. Vous êtes libre d'utiliser, de modifier et de distribuer ce code, tant que vous conservez la mention de l'auteur et la licence.

## Auteur

[@Foufou-exe](https://github.com/Foufou-exe)
