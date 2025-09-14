# Week 3 Project: Pretraining Data Pipeline & Voice Agent Development

## 🚀 Quick Summary
Built a **two-part project**:  
1. A **pretraining data pipeline** that scrapes scientific papers, extracts text via OCR, and cleans/deduplicates data.  
2. A **real-time voice agent** supporting 5-turn multi-round conversations using ASR (Whisper), LLM (LLaMA 3), and TTS (CozyVoice).  
Deliverables include a **clean dataset** for LLM training and a **local FastAPI server** for interactive voice dialogue.  
Demonstrates skills in **data engineering, NLP preprocessing, multimodal pipelines, and conversational AI development**.  

---

## 📖 Project Description
This project was designed to simulate **real-world AI workflows** in two areas:  

1. **Pretraining Data Pipeline** – Building a scalable, high-quality dataset for LLM pretraining, emphasizing **data quality, deduplication, and multi-source diversity**.  
2. **Voice Agent Development** – Creating a lightweight local voice assistant capable of **real-time dialogue**, integrating speech recognition, language modeling, and speech synthesis.  

The project highlights the importance of **data quality for model performance** and showcases the integration of multiple AI components into a single interactive system.  

---

## 🎯 Objectives

### Pretraining Data Pipeline
- Scrape scientific papers from arXiv on selected topics (e.g., NLP, AI safety).  
- Extract text from PDFs using OCR tools (Tesseract, Surya, GPT-4o Vision API).  
- Clean and filter data:  
  - Deduplicate with MinHash  
  - Remove PII (emails, phone numbers, credit cards)  
  - Filter non-English and low-quality text  
- Produce a **clean, diverse dataset** simulating state-of-the-art LLM training data.  

### Voice Agent Development
- Build a FastAPI server for audio input/output.  
- Use **Whisper** for Automatic Speech Recognition (ASR).  
- Integrate **LLaMA 3** for dialogue generation with conversation state tracking.  
- Synthesize speech with **CozyVoice** for natural TTS output.  
- Support **5-turn multi-round conversations** with history preservation.  

---

## 🛠️ Tech Stack
- **Programming Language**: Python  
- **Web/Data**: requests, BeautifulSoup, scrapy, pandas, regex, langdetect  
- **OCR**: Tesseract, pytesseract, Surya  
- **Deduplication**: datasketch (MinHash)  
- **ASR**: Whisper  
- **Dialogue Generation**: LLaMA 3  
- **TTS**: CozyVoice  
- **Server Framework**: FastAPI, Uvicorn  
- **Testing Tools**: curl, Postman  

---

## 🔥 Architecture / Workflow Diagram 
flowchart LR
  subgraph Data Pipeline
    A[Scrape PDFs] --> B[OCR (Tesseract/Surya)]
    B --> C[Cleaning (langdetect/regex)]
    C --> D[MinHash Dedup]
  end
  subgraph Voice Agent
    E[Audio Upload] --> F[ASR(Whisper)]
    F --> G[LLM(LLaMA-3)+State]
    G --> H[TTS(Co zyVoice)]
  end

---

## 📂 Deliverables
- `clean_dataset/` → pretraining-ready text corpus (deduplicated, PII-free).  
- `scraper/` → arXiv scraping and cleaning scripts.  
- `ocr_pipeline/` → PDF-to-text OCR processing scripts.  
- `voice_agent/` → FastAPI-based real-time voice assistant code.  
- Example outputs:  
  - `stats.md` → dataset statistics (token counts, % removed).  
  - Conversation transcripts (JSON).  

---


## 🔥 How to Run / Quick Start 
# Data pipeline
pip install -r requirements.txt
python build_corpus.py --topic "AI safety" --out dataset/

# Voice agent
uvicorn voice_agent.api:app --reload --port 8001
# Test
curl -X POST -F "file=@sample.wav" http://localhost:8001/talk
---

## 🌟 Highlights
- **End-to-end pretraining pipeline** for scientific text.  
- **Multi-modal integration**: web, PDFs, audio → unified text corpus.  
- **Privacy-aware cleaning** with PII removal and deduplication.  
- **Modular voice agent**: supports async processing, scalable to UI or custom voices.  
- Combines **research-oriented data engineering** with **applied conversational AI**.  

---

## 🚀 Skills Demonstrated
- **Data Engineering & NLP Preprocessing** – scraping, OCR, deduplication, and cleaning.  
- **Pipeline Design** – building modular, end-to-end workflows.  
- **Conversational AI Development** – ASR + LLM + TTS integration in real time.  
- **System Deployment** – FastAPI server design, API testing with curl/Postman.  
- **Research-to-Production Thinking** – simulating SOTA LLM pretraining workflows.  

---

## 🚀 Future Improvements
VAD/endpointing；speaker profiles；RAG grounding for factuality；latency tuning。

---
