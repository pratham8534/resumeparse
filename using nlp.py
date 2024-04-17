#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from load_spacy_model import nlp
import re

#extracting the metadata name,email,phone,profile_links-LinkedIn etc 
def extract_data(text):
    doc = nlp(text)
    lines = text.split('\n')
    name = lines[0].strip() if lines else None
    email = re.search(r'\b[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}\b', text, flags=re.IGNORECASE)
    phone = re.search(r'\b(?:\d{3}[-.]?)?\d{3}[-.]?\d{4}\b', text)
    profile_links = re.findall(r'(https?://\S+)', text)
    
    return email.group() if email else None, phone.group() if phone else None, profile_links, name

