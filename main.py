#!/usr/bin/env python3
import argparse

def caesar_cipher(text, shift, decrypt=False):
    """
    Applique le chiffrement ou déchiffrement de César uniquement sur les lettres alphabétiques.
    Les lettres sont d'abord converties en minuscules, et les caractères non-alphabétiques
    sont ignorés.
    
    :param text: Texte à traiter.
    :param shift: Décalage numérique pour le chiffrement.
    :param decrypt: Si True, déchiffre (inverse le décalage), sinon chiffre.
    :return: Texte traité sans caractères spéciaux.
    """
    if decrypt:
        shift = -shift
    result = ""
    for char in text:
        if char.isalpha():
            lower_char = char.lower()
            shifted = (ord(lower_char) - ord('a') + shift) % 26 + ord('a')
            result += chr(shifted)
        # Les caractères non-alphabétiques sont ignorés (non ajoutés au résultat)
    return result

def main():
    parser = argparse.ArgumentParser(
        description="Script de chiffrement/déchiffrement de César en ne prenant en compte que l'alphabet.",
        usage='%(prog)s [-c shift | -d shift] [-f FICHIER] [-o FICHIER_SORTIE] [TEXTE]'
    )

    # Groupe d'options mutuellement exclusives pour le chiffrement ou déchiffrement
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-c', type=int, help="Chiffrer avec la clé donnée.")
    group.add_argument('-d', type=int, help="Déchiffrer avec la clé donnée.")

    # Option pour spécifier un fichier d'entrée
    parser.add_argument('-f', '--file', type=str,
                        help="Nom du fichier à traiter (mode fichier).")
    # Option facultative pour spécifier un fichier de sortie
    parser.add_argument('-o', '--output', type=str,
                        help="Nom du fichier de sortie (optionnel). Si non spécifié, le fichier d'entrée sera écrasé.")
    # Argument positionnel pour le mode texte
    parser.add_argument('text', nargs='?', type=str,
                        help="Texte à traiter (mode texte).")

    args = parser.parse_args()

    # Détermination de l'opération (chiffrement ou déchiffrement)
    if args.c is not None:
        shift = args.c
        decrypt = False
    else:
        shift = args.d
        decrypt = True

    # Traitement en mode fichier
    if args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                content = f.read()
        except IOError as e:
            print("Erreur lors de la lecture du fichier :", e)
            exit(1)

        result = caesar_cipher(content, shift, decrypt)

        # Détermination du fichier de sortie (écrase le fichier d'origine par défaut)
        output_file = args.output or args.file

        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(result)
        except IOError as e:
            print("Erreur lors de l'écriture dans le fichier :", e)
            exit(1)

        # Affichage du résultat dans la console
        print(f"Résultat obtenu dans le fichier '{output_file}':")
    else:
        if args.text is None:
            print("Erreur : Vous devez fournir un texte ou utiliser l'option -f pour un fichier.")
            exit(1)
        result = caesar_cipher(args.text, shift, decrypt)
        print("Résultat:")

    print(result)

if __name__ == '__main__':
    main()
