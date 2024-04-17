#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import csv
from extract_text_from_pdf import extract_text
from text_summarize import summarize_text
from extract_data import extract_data



def resumes(folder_path, candidates_data):
    with open(candidates_data, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['File Name', 'Name', 'Email', 'Phone', 'Profile Links', 'Summary']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for filename in os.listdir(folder_path):
            if filename.endswith('.pdf'):
                file_path = os.path.join(folder_path, filename)
                text = extract_text(file_path)
                email, phone, profile_links, name = extract_data(text)
                summary = summarize_text(text)

                writer.writerow({
                    'File Name': filename,
                    'Name': name if name else 'Name not found',
                    'Email': email if email else 'E-mail not found',
                    'Phone': phone if phone else 'Phone number not mentioned ',
                    'Profile Links': ', '.join(profile_links) if profile_links else 'Profile not found',
                    'Summary': summary
                })

folder_path = r'C:\Users\Pratham Pathak\Desktop\Candidate Shortlisting System\allpdf'
candidates_data = 'output.csv'
resumes(folder_path, candidates_data)
print("The data is extracted succesfully in the candidates_data.csv file")

 

