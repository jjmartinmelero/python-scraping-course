# 🕷️ Python Web Scraping Course

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-1.58-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-4.x-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**A hands-on web scraping journey from basic HTTP requests to browser automation**

📚 Course completed on [midu.dev](https://midu.dev) — _Iniciación al Scraping con Python_

</div>

---

## 🎯 About

This repository contains all the exercises and projects developed during the **"Iniciación al Scraping con Python"** course on the [midu.dev](https://midu.dev) academy platform. The course covers the fundamentals of web scraping using Python, progressing from simple HTTP requests with regex to full browser automation with Playwright.

> **Author:** Juan Jesús Martín Melero

---

## 📂 Project Structure

```
python-scraping-course/
├── 01_basic.py               # Basic scraping with requests & regex
├── 02_beautiful.py           # HTML parsing with BeautifulSoup
├── 03_wiki-scraper.py        # Wikipedia scraper + Open Graph extraction
├── 04_seo_cli.py             # SEO analysis CLI tool
├── 05_playwright.py          # Playwright testing fundamentals
├── 06_playwright_scraping.py # Browser automation scraping
├── LICENSE
└── README.md
```

---

## 📖 Lessons & Exercises

### 1️⃣ Basic Scraping — `01_basic.py`

> Introduction to web scraping using `requests` and **regular expressions**.

- Fetching HTML content from a URL
- Extracting product prices with regex patterns
- Parsing page titles from raw HTML

### 2️⃣ BeautifulSoup — `02_beautiful.py`

> Structured HTML parsing with **BeautifulSoup4**.

- Using custom User-Agent headers
- Finding elements by tag, class, and attributes
- Extracting product names and prices from the Apple Store

### 3️⃣ Wikipedia Scraper — `03_wiki-scraper.py`

> Scraping structured content from Wikipedia + **Open Graph** metadata extraction.

- Extracting all headings and links from a page
- Building absolute URLs with `urljoin`
- Parsing Open Graph `og:image` meta tags

### 4️⃣ SEO CLI Tool — `04_seo_cli.py`

> A command-line **SEO analysis tool** built with `argparse`.

- Accepts any URL as a CLI argument
- Validates title tag length (SEO best practices)
- Checks for proper H1 heading structure

```bash
python 04_seo_cli.py https://example.com
```

### 5️⃣ Playwright Testing — `05_playwright.py`

> Introduction to **Playwright** for browser testing.

- Writing test functions with Playwright's `expect` API
- Verifying page titles and navigation
- Using role-based locators (`get_by_role`)

```bash
pytest 05_playwright.py
```

### 6️⃣ Playwright Scraping — `06_playwright_scraping.py`

> Full **browser automation** for scraping dynamic content.

- Launching a Chromium browser instance
- Navigating and clicking elements with CSS selectors
- Extracting image sources from dynamically loaded pages
- Using **XPath** selectors as an alternative to CSS

---

## 🛠️ Tech Stack

| Technology            | Purpose            |
| --------------------- | ------------------ |
| 🐍 **Python 3.11**    | Core language      |
| 📡 **Requests**       | HTTP requests      |
| 🍜 **BeautifulSoup4** | HTML parsing       |
| 🎭 **Playwright**     | Browser automation |
| 🧪 **pytest**         | Testing framework  |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/jjmartinmelero/python-scraping-course.git
cd python-scraping-course

# Install dependencies
pip install requests beautifulsoup4 playwright pytest-playwright

# Install Playwright browsers
python -m playwright install
```

### Usage

```bash
# Run any exercise
python 01_basic.py
python 02_beautiful.py
python 03_wiki-scraper.py
python 04_seo_cli.py https://midu.dev
python 06_playwright_scraping.py

# Run Playwright tests
pytest 05_playwright.py
```

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with ❤️ by **Juan Jesús Martín Melero**

🎓 Course by [midudev](https://midu.dev)

</div>
