import argparse
from pubmedapi import fetch_pubmed_ids, fetch_summary_details
from data_processing import process_author_details, save_to_csv

def main():
    # Hardcoded API key
    api_key = "a18f7dedd7964ee4933402ee8052c3e19008"

    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed API.")
    parser.add_argument('query', type=str, help="Search query for fetching papers.")
    parser.add_argument('-f', '--file', type=str, help="Filename to save the results as CSV. If not provided, prints to console.")
    parser.add_argument('-d', '--debug', action='store_true', help="Enable debug outputs.")

    args = parser.parse_args()

    if args.debug:
        print("Debug mode enabled.")
        print(f"Query: {args.query}")
        print(f"API Key: {api_key}")

    pubmed_ids = fetch_pubmed_ids(api_key, args.query)
    if not pubmed_ids:
        print("No IDs found for the query.")
        return

    xml_response = fetch_summary_details(api_key, pubmed_ids)
    if xml_response:
        papers = process_author_details(xml_response)
        if args.file:
            save_to_csv(papers, args.file)
            print(f"Data saved to {args.file}")
        else:
            for paper in papers:
                print(paper)
    else:
        print("Failed to fetch or process data.")

if __name__ == "__main__":
    main()
