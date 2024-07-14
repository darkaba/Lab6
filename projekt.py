import argparse

def parsuj():
    parser = argparse.ArgumentParser(description='Konwerter Danych')
    parser.add_argument('plik_wejsciowy', type=str, help='Ścieżka do pliku wejściowego')
    parser.add_argument('plik_wyjsciowy', type=str, help='Ścieżka do pliku wyjściowego')
    return parser.parse_args()

if __name__ == "__main__":
    argumenty = parsuj()
    print(f"Plik wejściowy: {argumenty.plik_wejsciowy}")
    print(f"Plik wyjściowy: {argumenty.plik_wyjsciowy}")
