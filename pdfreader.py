from pdfminer.high_level import extract_pages
from pdfminer.layout import (LTTextContainer, LTTextBox, LTChar, LTAnno, LTImage, 
                             LTFigure, LTCurve, LTRect, LTLine)
import xml.etree.ElementTree as ET

def pdf_to_xml(pdf_path):
    root = ET.Element("pdf_document")
    
    for page_layout in extract_pages(pdf_path):
        page_elem = ET.SubElement(root, "page")
        
        for element in page_layout:
            if isinstance(element, LTTextBox):
                box_elem = ET.SubElement(page_elem, "textbox", bbox=str(element.bbox))
                for text_line in element:
                    line_elem = ET.SubElement(box_elem, "textline")
                    for char_obj in text_line:
                        if isinstance(char_obj, LTChar):
                            char_elem = ET.SubElement(line_elem, "char", bbox=str(char_obj.bbox))
                            char_elem.text = char_obj.get_text()
                        elif isinstance(char_obj, LTAnno):
                            char_elem = ET.SubElement(line_elem, "anno")
                            char_elem.text = char_obj.get_text()
            elif isinstance(element, LTImage):
                ET.SubElement(page_elem, "image", bbox=str(element.bbox))
            elif isinstance(element, LTFigure):
                ET.SubElement(page_elem, "figure", bbox=str(element.bbox))
            elif isinstance(element, LTCurve):
                ET.SubElement(page_elem, "curve", bbox=str(element.bbox))
            elif isinstance(element, LTRect):
                ET.SubElement(page_elem, "rectangle", bbox=str(element.bbox))
            elif isinstance(element, LTLine):
                ET.SubElement(page_elem, "line", bbox=str(element.bbox))
    
    tree = ET.ElementTree(root)
    return tree

pdf_path = 'PLAN B Dachaufsicht.pdf'
xml_output_path = 'output.xml'

tree = pdf_to_xml(pdf_path)
tree.write(xml_output_path, encoding="utf-8", xml_declaration=True)
