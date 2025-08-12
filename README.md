Week 3 Project: Pretraining Data Pipeline & Voice Agent Development
1. Pretraining Data Collection & Extraction
Goal: Build a mini pipeline for LLM pretraining data, including scraping scientific papers, OCR text extraction from PDFs, and data cleaning/filtering.

Workflow:

Scrape papers from arXiv on a chosen topic (e.g., NLP, AI safety)

Extract text using OCR tools like Tesseract, Surya, or GPT-4o Vision API

Clean and filter data: deduplicate with MinHash, remove PII, non-English, and low-quality text

Produce a clean, diverse, multi-source dataset to simulate real SOTA LLM pretraining pipelines

Technologies: Python (requests, BeautifulSoup, scrapy), OCR (pytesseract, Surya), data cleaning (pandas, regex, langdetect), deduplication (datasketch)

Key takeaway: Data quality and diversity are crucial for model performance — rigorous cleaning and filtering are essential.

2. Voice Agent Development
Goal: Develop a local real-time voice assistant supporting 5-turn multi-round conversations, converting audio input to voice responses.

Core components:

FastAPI server for audio upload and response

Whisper for Automatic Speech Recognition (ASR)

LLaMA 3 for context-aware dialogue generation

CozyVoice for natural Text-to-Speech (TTS) synthesis

Simple conversation state management to maintain dialogue history

Highlights: Modular design, supports async optimization, easy to extend with UI or personalized voices

Run instructions: Use Python environment, run server with uvicorn, test with curl or Postman
