import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def get_all_links(url, visited):
    if url in visited:
        return []
    
    visited.add(url)
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to access {url}. Status code: {response.status_code}")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [urljoin(url, link['href']) for link in soup.find_all('a', href=True)]
    
    return links

def download_pdfs(url, save_dir, visited=set()):
    os.makedirs(save_dir, exist_ok=True)
    
    all_links = get_all_links(url, visited)
    pdf_links = []
    subpage_links = []
    
    for link in all_links:
        if link.endswith('.pdf'):
            pdf_links.append(link)
        elif urlparse(link).netloc == urlparse(url).netloc and link not in visited:
            subpage_links.append(link)
    
    for pdf_url in pdf_links:
        pdf_name = os.path.join(save_dir, os.path.basename(pdf_url))
        
        try:
            pdf_response = requests.get(pdf_url, stream=True)
            if pdf_response.status_code == 200:
                with open(pdf_name, 'wb') as pdf_file:
                    for chunk in pdf_response.iter_content(chunk_size=1024):
                        pdf_file.write(chunk)
                print(f"Downloaded: {pdf_name}")
            else:
                print(f"Failed to download {pdf_url}. Status code: {pdf_response.status_code}")
        except requests.RequestException as e:
            print(f"Error downloading {pdf_url}: {e}")
    
    for subpage in subpage_links:
        download_pdfs(subpage, save_dir, visited)

if __name__ == "__main__":
    target_url = input("Enter the URL of the web page: ")
    target_dir = input("Enter the directory to save PDFs: ")
    download_pdfs(target_url, target_dir)

