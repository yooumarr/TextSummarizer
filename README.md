# TextSummarizer

A simple Flask web app that summarizes text locally using LangChain and Hugging Face Transformers.

##  Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/<yooumarr>/TextSummarizer.git
   cd TextSummarizer
2. **Create and activate Conda environment**
   ```bash
   conda create -n text-sum python=3.10 -y
   conda activate text-sum
3. **Install dependencies**
   ```bash
   conda install --file requirements.txt
4. **Run the Flask app**
   ```bash
   python app.py
5. **Open in browser**
   ```bash
   http://127.0.0.1:5000

## How It Works

Loads a summarization model (facebook/bart-large-cnn) locally using Hugging Face Transformers.

Wraps it inside LangChain’s HuggingFacePipeline.

Flask provides a lightweight UI to input text and display the summary.
