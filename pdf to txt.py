#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install PyPDF2


# In[ ]:


import PyPDF2

def extract_text_from_pdf(pdf_file_path):
    text = ""
    try:
        # Open the PDF file in binary mode
        with open(pdf_file_path, 'rb') as pdf_file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            
            # Extract text from each page
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                text += page.extractText()
    except Exception as e:
        print("An error occurred:", e)
    
    return text




# In[ ]:




