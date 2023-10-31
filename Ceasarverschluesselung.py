def caesar_verschluesselung(text, k):
    """
    Verschlüsselt den gegebenen Text mit der Caesar-Verschlüsselung.

    Args:
    - text (str): Der zu verschlüsselnde Text.
    - k (int): Der Verschiebungsfaktor.

    Returns:
    - str: Der verschlüsselte Text.
    """
    verschluesselter_text = ""

    for char in text:
        # Für Großbuchstaben
        if 'A' <= char <= 'Z':
            verschluesselter_text += chr((ord(char) - ord('A') + k) % 26 + ord('A'))
        # Für Kleinbuchstaben
        elif 'a' <= char <= 'z':
            verschluesselter_text += chr((ord(char) - ord('a') + k) % 26 + ord('a'))
        # Für alle anderen Zeichen (z.B. Zahlen, Satzzeichen) den Charakter unverändert hinzufügen
        else:
            verschluesselter_text += char

    return verschluesselter_text

# Test
text = "Hallo Welt!"
k = 3
print(caesar_verschluesselung(text, k))  # Ausgabe: "Kdoor Zhow!"
