import xml.etree.ElementTree as ET
import time
import json

def xml_to_json(root):
    """
    Wandelt ein XML-Element in ein JSON-ähnliches Python-Objekt (in diesem Fall ein Dictionary) um.
    """
    data = {}
    
    # Überprüfe, ob das Root-Element 'VehicleInfoPrinter' ist
    if root.tag == 'VehicleInfoPrinter':
        for elem in root:
            # Wenn es ein 'controlledVehicle'-Element gibt
            if elem.tag == 'controlledVehicle':
                data['controlledVehicle'] = {child.tag: child.text for child in elem}
                
            # Wenn es ein 'playerPosition'-Element gibt
            elif elem.tag == 'playerPosition':
                data['playerPosition'] = {k: v for k, v in elem.attrib.items()}
    
    return data

def read_and_parse_xml(file_path):
    """
    Liest die XML-Datei, parst sie und gibt die Werte in der Konsole aus.
    """
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Konvertiere XML zu JSON
        json_data = json.dumps(xml_to_json(root), indent=4)
        print(json_data)

    except ET.ParseError:
        print("Fehler beim Parsen der XML-Datei. Überprüfe das Format der Datei.")

def main():
    xml_path = "C:/Users/User/Documents/My Games/FarmingSimulator2022/mods/FS22_karl/VehicleInfoPrinter.xml"  # Ersetze durch den Pfad zu deiner XML-Datei

    while True:
        read_and_parse_xml(xml_path)
        time.sleep(2)  # Warte 2 Sekunden vor dem nächsten Durchlauf

if __name__ == "__main__":
    main()
