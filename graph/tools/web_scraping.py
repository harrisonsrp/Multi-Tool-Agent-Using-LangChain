from Agents.ReflexionAgent.graph.tools.tavily import url_search
import requests
from bs4 import BeautifulSoup
import json
def web_scraping(urls):
    print("===== Starting Web Scraping =====")
    results = []
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')

            # Create a dictionary to store scraped data
            scraped_data = {}

            # Extract all headings (h1, h2) and store them in the dictionary
            headings = soup.find_all(['h1', 'h2'])
            scraped_data['headings'] = [heading.text.strip() for heading in headings]

            # Extract all paragraph texts and store them in the dictionary
            paragraphs = soup.find_all('p')
            scraped_data['paragraphs'] = [p.text.strip() for p in paragraphs]


            # Append the new scraped data to the list of all data
            results.append(scraped_data)

    # After scraping all URLs, save the combined data back to the JSON file
    with open("tools_results/scraped_data.json", "w") as json_file:
        json.dump(results, json_file, indent=4)
        print(scraped_data)
    print("==== Web Scraping Finished =====")

