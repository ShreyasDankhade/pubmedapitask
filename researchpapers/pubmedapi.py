import requests
from typing import List, Optional
from xml.etree import ElementTree as ET
from requests import Session

# Initialize a Session
session = Session()

def fetch_pubmed_ids(api_key: str, query: str) -> Optional[List[str]]:
    """Fetches PubMed IDs based on a given search query via the PubMed API.
    
    Args:
        api_key (str): The API key for accessing PubMed.
        query (str): The search query string.

    Returns:
        Optional[List[str]]: A list of PubMed IDs or None if an error occurs.
    """
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "api_key": api_key,
        "retmax": "20"
    }
    try:
        response = session.get(base_url, params=params)
        response.raise_for_status()
        root = ET.fromstring(response.text)
        ids = [id_elem.text for id_elem in root.findall('./IdList/Id')]
        return ids
    except requests.HTTPError as e:
        print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
        return None
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None
    except ET.ParseError as e:
        print(f"XML parsing error: {e}")
        return None

def fetch_summary_details(api_key: str, ids: List[str]) -> Optional[str]:
    """Fetches detailed article summaries based on PubMed IDs.
    
    Args:
        api_key (str): The API key for accessing PubMed.
        ids (List[str]): List of PubMed IDs.

    Returns:
        Optional[str]: Raw XML data of summaries or None if an error occurs.
    """
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "api_key": api_key,
        "id": ",".join(ids),
        "retmode": "xml"
    }
    try:
        response = session.get(base_url, params=params)
        response.raise_for_status()
        return response.text
    except requests.HTTPError as e:
        print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
        return None
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None
