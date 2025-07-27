import requests
from bs4 import BeautifulSoup
import json
import xml.etree.ElementTree as ET

def scrape_quotes(num_pages=1):
    """
    Scrapes quotes, authors, and tags from quotes.toscrape.com.
    Args:
        num_pages (int): The number of pages to scrape.
    Returns:
        list: A list of dictionaries, where each dictionary represents a quote.
    """
    quotes_data = []
    base_url = "http://quotes.toscrape.com"

    for page_num in range(1, num_pages + 1):
        url = f"{base_url}/page/{page_num}/"
        print(f"Scraping page: {url}") # For progress tracking
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all quote divs
        quote_divs = soup.find_all('div', class_='quote')

        for quote_div in quote_divs:
            text = quote_div.find('span', class_='text').get_text(strip=True)
            author = quote_div.find('small', class_='author').get_text(strip=True)
            tags = [tag.get_text(strip=True) for tag in quote_div.find('div', class_='tags').find_all('a', class_='tag')]

            quotes_data.append({
                'text': text,
                'author': author,
                'tags': tags
            })

        # Check if there's a next page link
        next_button = soup.find('li', class_='next')
        if not next_button:
            print(f"No more pages after page {page_num}.")
            break # Exit loop if no next page

    return quotes_data

def save_to_json(data, filename="quotes.json"):
    """Saves the scraped data to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Data saved to {filename}")

def save_to_xml(data, filename="quotes.xml"):
    """Saves the scraped data to an XML file."""
    root = ET.Element("quotes")
    for quote_item in data:
        quote_elem = ET.SubElement(root, "quote")

        text_elem = ET.SubElement(quote_elem, "text")
        text_elem.text = quote_item['text']

        author_elem = ET.SubElement(quote_elem, "author")
        author_elem.text = quote_item['author']

        tags_elem = ET.SubElement(quote_elem, "tags')
        for tag in quote_item['tags']:
          tag_elem = ET.SubElement(quote_elem, "tags") # Using double quotes for both

            tag_elem.text = tag

    tree = ET.ElementTree(root)
    # Use pretty_print to make the XML human-readable
    ET.indent(tree, space="  ", level=0) # Requires Python 3.9+
    tree.write(filename, encoding='utf-8', xml_declaration=True)
    print(f"Data saved to {filename}")

def save_to_html(data, filename="quotes.html"):
    """Saves the scraped data to an HTML file as a table."""
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scraped Quotes</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { color: #333; }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
            vertical-align: top; /* Ensures text aligns at the top of the cell */
        }
        th {
            background-color: #f2f2f2;
            font-weight: bold;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        .quote-text {
            max-width: 600px; /* Limit width for readability */
            line-height: 1.5;
        }
        .tags-list {
            list-style-type: none;
            padding: 0;
            margin: 0;
        }
        .tags-list li {
            display: inline-block;
            background-color: #e0f2f7;
            border-radius: 4px;
            padding: 3px 8px;
            margin-right: 5px;
            margin-bottom: 5px;
            font-size: 0.85em;
            color: #333;
        }
    </style>
</head>
<body>

    <h1>Scraped Quotes from quotes.toscrape.com</h1>

    <table>
        <thead>
            <tr>
                <th>Quote Text</th>
                <th>Author</th>
                <th>Tags</th>
            </tr>
        </thead>
        <tbody>
    """

    for quote_item in data:
        html_content += "<tr>\n"
        html_content += f'<td class="quote-text">{quote_item["text"]}</td>\n'
        html_content += f'<td>{quote_item["author"]}</td>\n'
        
        # Format tags as an unordered list
        html_content += '<td><ul class="tags-list">\n'
        for tag in quote_item['tags']:
            html_content += f'<li>{tag}</li>\n'
        html_content += '</ul></td>\n'
        
        html_content += "</tr>\n"

    html_content += """
        </tbody>
    </table>

</body>
</html>
    """

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    # Scrape the first 3 pages as an example
    # You can change this number based on how many pages you want to scrape
    print("Starting scraping process...")
    quotes = scrape_quotes(num_pages=3)
    print(f"Scraping complete. Found {len(quotes)} quotes.")

    if quotes:
        print("\nSaving data to different formats:")
        save_to_json(quotes)
        save_to_xml(quotes)
        save_to_html(quotes)
    else:
        print("No quotes scraped. Cannot save to files.")


