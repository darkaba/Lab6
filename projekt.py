import argparse
import json
import xmltodict
import yaml

def parsuj():
    parser = argparse.ArgumentParser(description='Konwerter Danych')
    parser.add_argument('plik_wejsciowy', type=str, help='Ścieżka do pliku wejściowego')
    parser.add_argument('plik_wyjsciowy', type=str, help='Ścieżka do pliku wyjściowego')
    return parser.parse_args()

def taskjson(sciezka_pliku):
    with open(sciezka_pliku, 'r') jako plik:
        try:
            dane = json.load(plik)
            return dane
        except json.JSONDecodeError as e:
            print(f"Błąd odczytu pliku JSON: {e}")
            return None

def zapisz_json(sciezka, dane):
    with open(sciezka, 'w') jako plik:
        json.dump(dane, plik, indent=4)

def taskxml(sciezka):
    with open(sciezka, 'r') jako plik:
        try:
            dane = xmltodict.parse(plik.read())
            return dane
        except Exception as e:
            print(f"Błąd odczytu pliku XML: {e}")
            return None

def zapisz_xml(sciezka, dane):
    with open(sciezka, 'w') jako plik:
        xml_str = xmltodict.unparse(dane, pretty=True)
        plik.write(xml_str)

def taskyaml(sciezka):
    with open(sciezka, 'r') jako plik:
        try:
            dane = yaml.safe_load(plik)
            return dane
        except yaml.YAMLError as e:
            print(f"Błąd odczytu pliku YAML: {e}")
            return None

def zapisz_yaml(sciezka, dane):
    with open(sciezka, 'w') jako plik:
        yaml.dump(dane, plik, indent=4)

def konwertowanie(plik_wejsciowy, plik_wyjsciowy):
    rozszerzenie_wejsciowe = plik_wejsciowy.split('.')[-1].lower()
    rozszerzenie_wyjsciowe = plik_wyjsciowy.split('.')[-1].lower()

    if rozszerzenie_wejsciowe == 'json':
        dane = taskjson(plik_wejsciowy)
    elif rozszerzenie_wejsciowe == 'xml':
        dane = taskxml(plik_wejsciowy)
    elif rozszerzenie_wejsciowe in ['yaml', 'yml']:
        dane = taskyaml(plik_wejsciowy)
    else:
        print(f"Nieobsługiwany format pliku wejściowego: {rozszerzenie_wejsciowe}")
        return

    if not dane:
        print("Brak danych do konwersji")
        return

    if rozszerzenie_wyjsciowe == 'json':
        zapisz_json(plik_wyjsciowy, dane)
    elif rozszerzenie_wyjsciowe == 'xml':
        zapisz_xml(plik_wyjsciowy, dane)
    elif
