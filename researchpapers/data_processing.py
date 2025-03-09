import xml.etree.ElementTree as ET
import pandas as pd
import os
from typing import List, Dict, Optional

def process_author_details(xml_data: str) -> List[Dict[str, str]]:
    """Processes author details from provided XML data, focusing on those with pharma or biotech affiliations."""
    root = ET.fromstring(xml_data)
    papers_list = []

    for article in root.findall('./PubmedArticle'):
        pubmed_id = article.find('.//PMID').text
        title = article.find('.//ArticleTitle').text

        # Handle missing Year and Month in PubDate
        pub_date_element = article.find('.//PubDate/Year')
        pub_month_element = article.find('.//PubDate/Month')

        pub_date = (
            f"{pub_date_element.text}-{pub_month_element.text}"
            if pub_date_element is not None and pub_month_element is not None
            else "Unknown"
        )

        authors = article.findall('.//Author')
        relevant_authors = []

        for author in authors:
            first_name = author.find('ForeName')
            last_name = author.find('LastName')
            full_name = (
                f"{first_name.text} {last_name.text}"
                if first_name is not None and last_name is not None
                else "Unknown"
            )

            affiliations = author.findall('.//AffiliationInfo/Affiliation')
            for affiliation in affiliations:
                if affiliation is not None and (
                    "pharmaceutical" in affiliation.text.lower() or "biotech" in affiliation.text.lower()
                ):
                    relevant_authors.append(full_name)
                    break  # Stop once we find one valid affiliation

        if relevant_authors:  # Only add papers that have at least one relevant author
            papers_list.append({
                "PubmedID": pubmed_id,
                "Title": title,
                "Publication Date": pub_date,
                "Authors with Pharma/Biotech Affiliations": ", ".join(relevant_authors),
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

