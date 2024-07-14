import argparse
import json

def parsuj():
    parser = argparse.ArgumentParser(description='Konwerter Danych')
    parser.add_argument('plik_wejsciowy', type=str, help='Ścieżka do pliku wejściowego')
    parser.add_argument('plik_wyjsciowy', type=str, help='Ścieżka do pliku wyjściowego')
    return parser.parse_args()

def wczytaj_json(sciezka_pliku):
    with open(sciezka_pliku, 'r') jako plik:
        try:
            dane = json.load(plik)
            return dane
        except json.JSONDecodeError as e:
            print(f"Błąd odczytu pliku JSON: {e}")
            return None

if __name__ == "__main__":
    argumenty = parsuj()
    print(f"Plik wejściowy: {argumenty.plik_wejsciowy}")
    print(f"Plik
