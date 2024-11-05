import PyPDF2
import os

def split_pdf(pdf_path, output_folder, start_page, end_page):
    # Prüfen, ob das PDF existiert
    if not os.path.exists(pdf_path):
        print(f"Die Datei {pdf_path} existiert nicht.")
        return

    # Ordner erstellen, wenn nicht vorhanden
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # PDF öffnen
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        total_pages = len(reader.pages)

        # Validierung der Seitenzahlen
        if start_page < 1 or end_page > total_pages or start_page > end_page:
            print("Ungültiger Seitenbereich.")
            return

        # Nur den angegebenen Bereich trennen
        for page_num in range(start_page - 1, end_page):
            writer = PyPDF2.PdfWriter()
            writer.add_page(reader.pages[page_num])

            output_path = os.path.join(output_folder, f"page_{page_num + 1}.pdf")
            with open(output_path, 'wb') as output_pdf:
                writer.write(output_pdf)

            print(f"Seite {page_num + 1} wurde als {output_path} gespeichert.")

# Beispielaufruf
pdf_path = 'Bewerbung_Heinrich-Seidel-Straße_Beck.pdf'  # Pfad zur PDF-Datei
output_folder = 'getrennte_seiten'   # Ordner, in dem die Seiten gespeichert werden
start_page = 10  # Startseite angeben
end_page = 10    # Endseite angeben
split_pdf(pdf_path, output_folder, start_page, end_page)
