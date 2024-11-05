import PyPDF2
import os

def merge_pdfs(pdf_list, output_path):
    # Ein PdfWriter Objekt erstellen, das die PDFs zusammenfügt
    pdf_writer = PyPDF2.PdfWriter()

    # Jede PDF in der Liste öffnen und Seiten hinzufügen
    for pdf_path in pdf_list:
        if not os.path.exists(pdf_path):
            print(f"Die Datei {pdf_path} existiert nicht.")
            continue

        with open(pdf_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)

            # Alle Seiten der aktuellen PDF hinzufügen
            for page_num in range(len(reader.pages)):
                pdf_writer.add_page(reader.pages[page_num])

            print(f"Datei {pdf_path} wurde hinzugefügt.")

    # Zusammengeführte Datei speichern
    with open(output_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

    print(f"Zusammengeführtes PDF wurde als {output_path} gespeichert.")

# Beispielaufruf
pdf_list = [
    './getrennte_seiten/1.pdf',
    './getrennte_seiten/2.pdf',
]  # Liste der PDFs, die zusammengeführt werden sollen

output_path = 'Beck_Victoria.pdf'  # Name der Ausgabedatei
merge_pdfs(pdf_list, output_path)
