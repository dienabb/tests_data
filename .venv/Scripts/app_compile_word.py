import streamlit as st
from docx import Document
import os
import tempfile

def merge_docs(doc_files):
    merged_document = Document()

    for index, doc_file in enumerate(doc_files):
        sub_doc = Document(doc_file)
        for element in sub_doc.element.body:
            merged_document.element.body.append(element)

        # Don't add a page break if you've reached the last file.
        if index < len(doc_files)-1:
           merged_document.add_page_break()

    return merged_document

st.title('Fusionneur de Word')

uploaded_files = st.file_uploader("Choisissez des fichiers Word", type=["docx"], accept_multiple_files=True)

# Get the path to the .venv/Temp directory
temp_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'Temp')

# Get the path to the Téléchargements directory
downloads_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'Downloads')

if st.button('Fusionner'):
    if uploaded_files:
        doc_files = []
        for uploaded_file in uploaded_files:
            # Create a temporary file in the specified directory
            temp_fd, temp_path = tempfile.mkstemp(dir=temp_dir)
            with os.fdopen(temp_fd, 'wb') as tmp:
                # Write the content of the uploaded file to the temporary file
                tmp.write(uploaded_file.read())
            doc_files.append(temp_path)

        try:
            merged_document = merge_docs(doc_files)
            # Save the merged document in the Téléchargements directory
            merged_file_path = os.path.join(downloads_dir, 'merged.docx')
            merged_document.save(merged_file_path)
            st.success(f'Fusion réussie. Téléchargez le fichier fusionné <a href="{merged_file_path}" download>ici</a>')
            for doc_file in doc_files:
                os.unlink(doc_file)
        except Exception as e:
            st.error(f"Une erreur s'est produite lors de la fusion des documents : {e}")
    else:
        st.error('Veuillez d\'abord télécharger des fichiers Word.')