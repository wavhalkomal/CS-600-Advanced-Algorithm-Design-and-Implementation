"""
search_engine.py
Author: Komal Wavhal (20034443)
Description: Mini Search Engine using Web Crawler and Inverted Index

This script builds an inverted index from a folder of HTML pages, accepts user queries, and displays ranked results based on term frequency.

This project implements a simplified version of a search engine, designed to demonstrate fundamental concepts in information retrieval, web crawling, and indexing. The system consists of two main components: a Web Crawler and an Inverted Index-based Search Engine.
The Web Crawler starts from a seed URL and automatically downloads a set number of internal web pages, saving them locally for analysis. The downloaded HTML pages are then processed by the Search Engine, which extracts textual content, removes stopwords, and builds an inverted index — a data structure that maps each word to the files it appears in, along with frequency counts.
The system supports user queries via a command-line interface, ranking and returning relevant documents based on term frequency. A log of all queries and results is saved to an output file. The goal of this project is to simulate the core functionality of real-world search engines like Google, using basic but effective techniques.
This project helps understand the lifecycle of a search engine: from web crawling and indexing to querying and ranking results — all built using Python, BeautifulSoup, and basic text processing methods.

"""

import os
import re
from bs4 import BeautifulSoup
from invertedindex import build_index, load_stopwords


def search(index, query, stopwords):
    """
    Processes user query and ranks pages based on total term frequencies.
    """
    from invertedindex import tokenize
    terms = tokenize(query, stopwords)
    results = {}

    for term in terms:
        if term in index:
            for file, count in index[term].items():
                if file not in results:
                    results[file] = 0
                results[file] += count

    return sorted(results.items(), key=lambda x: x[1], reverse=True)

def main():
    stopwords = load_stopwords()
    index = build_index("input_pages", stopwords)

    print("🔎 Type your search query (or 'exit' to quit):")
    logs = []

    while True:
        query = input("\nQuery: ").strip()
        if query.lower() == 'exit':
            break

        matches = search(index, query, stopwords)
        log_entry = f"Query: {query}\n"

        if matches:
            print("📄 Results:")
            for file, score in matches:
                print(f"  {file} (score: {score})")
                log_entry += f"  {file} (score: {score})\n"
        else:
            print("❌ No results found.")
            log_entry += "  No results found.\n"

        logs.append(log_entry)

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("=== Search Engine Query Log ===\n\n")
        f.write("\n".join(logs))

    print("✅ Search complete. Results saved to output.txt.")

if __name__ == "__main__":
    main()