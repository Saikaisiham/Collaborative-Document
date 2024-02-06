# from docx import Document

# def convert_to_html(docx_path):
#     doc = Document(docx_path)
#     html_content = []
#     for paragraph in doc.paragraphs:
#         html_content.append('<p>' + paragraph.text + '</p>')
#     return '\n'.join(html_content)


from odf.opendocument import load

def convert_odt_to_html(odt_path):
    doc = load(odt_path)
    html_content = []
    for element in doc.getElementsByType('text:p'):
        html_content.append('<p>' + element.firstChild.data + '</p>')
    return '\n'.join(html_content)