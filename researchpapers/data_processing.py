import xml.etree.ElementTree as ET
import pandas as pd
import os
from typing import List, Dict, Optional

def process_author_details(xml_data: str) -> List[Dict[str, str]]:
    """Processes author details from provided XML data, focusing on those with pharma or biotech affiliations.

    Args:
        xml_data (str): XML data containing author and article details.

    Returns:
        List[Dict[str, str]]: List of dictionaries with article details if they have relevant author affiliations.
    """
    root = ET.fromstring(xml_data)
    papers_list = []
    for article in root.findall('./PubmedArticle'):
        pubmed_id = article.find('.//PMID').text
        title = article.find('.//ArticleTitle').text
        pub_date = f"{article.find('.//PubDate/Year').text}-{article.find('.//PubDate/Month').text}"
        
        authors = article.findall('.//Author')
        relevant_authors = []

        for author in authors:
            full_name = f"{author.find('ForeName').text} {author.find('LastName').text}"
            affiliations = author.findall('.//AffiliationInfo/Affiliation')
            for affiliation in affiliations:
                if "pharmaceutical" in affiliation.text.lower() or "biotech" in affiliation.text.lower():
                    relevant_authors.append(full_name)
                    break  # Only need one qualifying affiliation per author

        if relevant_authors:  # Only add papers that have at least one relevant author
            papers_list.append({
                "PubmedID": pubmed_id,
                "Title": title,
                "Publication Date": pub_date,
                "Authors with Pharma/Biotech Affiliations": ", ".join(relevant_authors)
            })

    return papers_list


def save_to_csv(papers, filename):
    """Saves the extracted paper data to a CSV file in the script's directory.

    Args:
        papers (list of dict): A list of dictionaries containing paper information.
        filename (str): The filename for the CSV file.
    """
    # Get the directory of the currently executing script
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Combine the directory path with the filename to create the full path
    full_path = os.path.join(dir_path, filename)

    # Create a DataFrame and save it to CSV
    df = pd.DataFrame(papers)
    df.to_csv(full_path, index=False)
    print(f"Data successfully saved to {full_path}")

