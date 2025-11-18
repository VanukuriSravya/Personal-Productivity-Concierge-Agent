# Personal-Productivity-Concierge-Agent
An AI concierge agent that understands natural language to automatically manage tasks, reminders, and events, improving daily productivity
# Concierge Agent — Personal Productivity (Demo)

This repository contains a minimal demo of a Concierge Agent: an NLP-driven assistant for personal productivity.
The demo includes a simple rule-based NLP parser, workflow handlers, and JSON-backed storage. A lightweight Flask
app (app.py) provides REST endpoints and a tiny HTML UI (templates/index.html).

## Files
- app.py: Flask app (demo; run locally)
- nlp_parser.py: rule-based intent parser
- workflow.py: intent handlers and simple scheduling logic
- models.py: JSON-backed storage functions
- templates/index.html: minimal UI
- sample_data.json: storage file
- demo_notebook.ipynb: Colab-compatible notebook that demonstrates core functionality without running Flask.

## Quick start (local)
1. Create virtualenv and activate it.
2. pip install flask
3. python app.py
4. Open http://127.0.0.1:5000/ in your browser.

## Notes for Kaggle / Colab
- Kaggle and Colab notebooks can run the demo_notebook.ipynb to showcase parsing + workflow capabilities.
- For a live demo (Flask), deploy to a machine or use ngrok to expose the local server.
