"""
crawler.py
Author: Komal Wavhal (20034443)
Description: Mini Search Engine using Web Crawler and Inverted Index

This script starts with a seed URL and crawls up to MAX_PAGES internal links from the website,
saving each as an HTML file in the 'input_pages' folder.

This project implements a simplified version of a search engine, designed to demonstrate fundamental concepts in information retrieval, web crawling, and indexing. The system consists of two main components: a Web Crawler and an Inverted Index-based Search Engine.
The Web Crawler starts from a seed URL and automatically downloads a set number of internal web pages, saving them locally for analysis. The downloaded HTML pages are then processed by the Search Engine, which extracts textual content, removes stopwords, and builds an inverted index — a data structure that maps each word to the files it appears in, along with frequency counts.
The system supports user queries via a command-line interface, ranking and returning relevant documents based on term frequency. A log of all queries and results is saved to an output file. The goal of this project is to simulate the core functionality of real-world search engines like Google, using basic but effective techniques.
This project helps understand the lifecycle of a search engine: from web crawling and indexing to querying and ranking results — all built using Python, BeautifulSoup, and basic text processing methods.

"""

import requests  # To send HTTP requests to web pages
from bs4 import BeautifulSoup  # To parse HTML content
from urllib.parse import urljoin, urlparse  # To handle and resolve URLs
import os  # To handle file system operations

# Configuration
SEED_URL = "https://en.wikipedia.org/wiki/Google"  # Starting point of the crawl
MAX_PAGES = 10  # Maximum number of pages to crawl
SAVE_DIR = "input_pages"  # Directory to store HTML files
visited = set()  # To keep track of visited URLs and avoid duplicates

def is_valid_link(url, base_netloc):
    """
    Checks whether a link is internal (i.e., within the same domain).
    Prevents crawling external websites.
    """
    return urlparse(url).netloc == base_netloc or urlparse(url).netloc == ''

def crawl(url, base_url, count=0):
    """
    Recursively fetches and saves internal web pages starting from a URL.
    Stops after MAX_PAGES have been saved or no new links are found.
    """
    if count >= MAX_PAGES or url in visited:
        return count  # Stop condition

    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch: {url} (status code {response.status_code})")
            return count
        html = response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return count

    visited.add(url)  # Mark this URL as visited

    # Save HTML to local file
    filename = os.path.join(SAVE_DIR, f"page{count+1}.html")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Saved: {url} → {filename}")
    count += 1

    # Parse all links on this page
    soup = BeautifulSoup(html, "html.parser")
    for link in soup.find_all("a", href=True):
        next_url = urljoin(base_url, link['href'])  # Resolve relative URLs
        if next_url not in visited and is_valid_link(next_url, urlparse(base_url).netloc):
            count = crawl(next_url, base_url, count)
            if count >= MAX_PAGES:
                break

    return count

if __name__ == "__main__":
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)  # Create the save directory if it doesn't exist

    print(f"🌐 Starting crawl from: {SEED_URL}")
    print(f"📥 Saving up to {MAX_PAGES} pages in: {SAVE_DIR}")
    crawl(SEED_URL, SEED_URL)
    print("✅ Crawling complete.")