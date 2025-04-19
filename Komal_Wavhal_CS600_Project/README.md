# SearchEngine
Komal Shahadeo Wavhal (20034443)
CS600: Advanced Algorithm Design & Implementation
Final Project  
# 🔍 Simple Python Search Engine

This is a simple search engine project built using Python. 
It parses a collection of HTML web pages, builds an **inverted index**, and allows users to search for keywords using a **command-line interface**. 
The project is inspired by Section 23.6 of our textbook and is designed for educational purposes.

---

## 📂 Project Structure

This project implements a simplified search engine using Python. It parses local HTML files, builds an inverted index, and allows users to search for keywords. Search results are ranked based on word frequency and relevance.

Key components include:
Inverted Index: Maps each word to a list of pages containing it.
Occurrence Dictionary: Tracks how often each word appears in each document.
Ranking Algorithm: Results are ranked by total keyword occurrences, with higher weights for words in titles.
Algorithms: Modified merge for intersecting result lists and quicksort for ranking.
The engine returns relevant HTML pages in descending order of relevance, mimicking the behavior of a basic web search engine.

---

## 📦 Dependencies

Make sure you have Python 3 installed. The project uses the following Python package:

- **BeautifulSoup4** – for parsing HTML content
 
### 1. Install depedencies via pip:
(requires python 3)  
    1. pip install nltk  
    2. pip install beautifulsoup4  
    3. pip install requests

## ▶️ How to Run 

1. Place your `.html` files inside the `webpages/` folder.
2. Make sure `stopwords.txt` is in the same directory.
3. Run the engine:

### 2. Run project
In project directory (../Komal_Wavhal_CS600_Project):

komal_wavhal_cs600_project/
├── crawler.py              # Crawls pages from a seed URL and saves them as HTML
├── invertedindex.py        # Builds an inverted index from the crawled pages
├── search_engine.py        # Provides a CLI to search and rank results
├── stopwords.txt           # List of common stopwords to exclude from index
├── output.txt              # Auto-generated file logging search queries/results
├── input_pages/            # Folder where HTML files are saved from the crawler
│   ├── page1.html
│   ├── page2.html
│   ├── ... up to page10.html
└── README.md               # (Optional) Instructions for setup and usage


~~~
pip install -r requirements.txt

python main.py
~~~

### 📤 Output
~~~
The results of each search query are saved in a file named output.txt.

This file contains:

The search terms entered.

The ranked list of matching webpage URLs.

The number of times each search term appeared on each page.

This ensures search history and results can be reviewed or analyzed later.
~~~

Wait for data to load. Begin entering search terms when this appears:

~~~
(myenv) ~/..../Komal_Wavhal_CS600_Project
python crawler.py
🌐 Starting crawl from: https://en.wikipedia.org/wiki/Google
📥 Saving up to 10 pages in: input_pages
✅ Saved: https://en.wikipedia.org/wiki/Google → input_pages/page1.html
✅ Saved: https://en.wikipedia.org/wiki/Google#bodyContent → input_pages/page2.html
✅ Saved: https://en.wikipedia.org/wiki/Main_Page → input_pages/page3.html
✅ Saved: https://en.wikipedia.org/wiki/Wikipedia:Contents → input_pages/page4.html
✅ Saved: https://en.wikipedia.org/wiki/Portal:Current_events → input_pages/page5.html
✅ Saved: https://en.wikipedia.org/wiki/Special:Random → input_pages/page6.html
✅ Saved: https://en.wikipedia.org/wiki/Wikipedia:About → input_pages/page7.html
✅ Saved: https://en.wikipedia.org/wiki/Wikipedia:Contact_us → input_pages/page8.html
✅ Saved: https://en.wikipedia.org/wiki/Help:Contents → input_pages/page9.html
✅ Saved: https://en.wikipedia.org/wiki/Help:Introduction → input_pages/page10.html
✅ Crawling complete.

(myenv) ~/..../Komal_Wavhal_CS600_Project
python invertedindex.py  

(myenv) ~/..../Komal_Wavhal_CS600_Project
python search_engine.py  
🔎 Type your search query (or 'exit' to quit):

Query: google
📄 Results:
  page1.html (score: 784)
  page2.html (score: 784)

Query: machine learning
📄 Results:
  page1.html (score: 12)
  page2.html (score: 12)
  page3.html (score: 3)
  page7.html (score: 1)
  page9.html (score: 1)

Query: artificial intelligence
📄 Results:
  page1.html (score: 33)
  page2.html (score: 33)

Query: data
📄 Results:
  page1.html (score: 50)
  page2.html (score: 50)
  page7.html (score: 1)
  page5.html (score: 1)

Query: python
❌ No results found.

Query: sql
❌ No results found.

Query: file
📄 Results:
  page1.html (score: 1)
  page10.html (score: 1)
  page5.html (score: 1)
  page2.html (score: 1)

Query: technology
📄 Results:
  page1.html (score: 24)
  page2.html (score: 24)
  page4.html (score: 9)
  page5.html (score: 6)

Query: deep learning
📄 Results:
  page1.html (score: 5)
  page2.html (score: 5)
  page4.html (score: 1)
  page7.html (score: 1)
  page9.html (score: 1)
  page3.html (score: 1)

Query: java
❌ No results found.

Query: exit
✅ Search complete. Results saved to output.txt.


### 📄 Example `output.txt`
 === Search Engine Query Log ===

Query: google
  page1.html (score: 784)
  page2.html (score: 784)

Query: machine learning
  page1.html (score: 12)
  page2.html (score: 12)
  page3.html (score: 3)
  page7.html (score: 1)
  page9.html (score: 1)

Query: artificial intelligence
  page1.html (score: 33)
  page2.html (score: 33)

Query: data
  page1.html (score: 50)
  page2.html (score: 50)
  page7.html (score: 1)
  page5.html (score: 1)

Query: python
  No results found.

Query: sql
  No results found.

Query: file
  page1.html (score: 1)
  page10.html (score: 1)
  page5.html (score: 1)
  page2.html (score: 1)

Query: technology
  page1.html (score: 24)
  page2.html (score: 24)
  page4.html (score: 9)
  page5.html (score: 6)

Query: deep learning
  page1.html (score: 5)
  page2.html (score: 5)
  page4.html (score: 1)
  page7.html (score: 1)
  page9.html (score: 1)
  page3.html (score: 1)

Query: java
  No results found.

