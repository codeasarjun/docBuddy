# DocBuddy Flask App

## Overview

DocBuddy is a Flask-based web application that allows users to upload PDF files, view their content, summarize the text, suggest keywords, and interact with a dummy Q&A feature. The application provides a user-friendly interface with various tabs to explore different aspects of the uploaded document.

## Features

- **Upload PDF Files**: Upload and process PDF files to extract and display content.
- **View Original Content**: See the raw text extracted from the PDF.
- **Summarize Content**: Get a summarized version of the text.
- **Suggested Keywords**: View keywords suggested from the document's content.
- **Chat**: Interact with a dummy Q&A feature to ask questions related to the document.
- **PDF Viewer**: View the uploaded PDF directly in the browser.

## Project Structure

- `app.py`: The main Flask application script.
- `core/`:
  - `functionality.py`: Contains the core functions for text summarization, keyword suggestion, and dummy Q&A.
- `templates/`:
  - `upload.html`: The file upload form template.
  - `tabs.html`: The main view template with tabs for content display.
- `static/`:
  - `upload.css`: CSS styles for the file upload form.
  - `tabs.css`: CSS styles for the main view template.

## Installation

### Prerequisites

- Python 3.7+
- `pip` (Python package installer)

### Output

<img src='https://github.com/codeasarjun/docBuddy/blob/main/img/home_page.png'>
<img src='https://github.com/codeasarjun/docBuddy/blob/main/img/landing_page.png'>
<img src='https://github.com/codeasarjun/docBuddy/blob/main/img/summary.png'>
<img src='https://github.com/codeasarjun/docBuddy/blob/main/img/keywords.png'>
