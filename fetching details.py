#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import spacy

def extract_details(text):
    # Load the English language model
    nlp = spacy.load("en_core_web_sm")
    
    # Process the text with spaCy
    doc = nlp(text)

    # Initialize variables to store details
    name = ""
    phone = ""
    address = ""
    linkedin = ""

    # Extract details using named entity recognition
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name = ent.text
        elif ent.label_ == "PHONE":
            phone = ent.text
        elif ent.label_ == "ADDRESS":
            address = ent.text
        elif ent.label_ == "LINK":
            linkedin = ent.text

    # Return the extracted details
    return name, phone, address, linkedin

# Example text containing the details
text = """
Name: pratham pathak
Phone: 123-456-7890
Address: 123 Main St, City, State, Zip
LinkedIn: https://www.linkedin.com/in/pratham
"""

# Extract details from the text
name, phone, address, linkedin = extract_details(text)

# Print the extracted details
print("Name:", name)
print("Phone:", phone)
print("Address:", address)
print("LinkedI



