# Summarize Text from YouTube or Websites

This project is a **Streamlit-based AI tool** that extracts and summarizes text from **YouTube videos** and **web pages** using **Groq's LLM (Gemma 2-9B-It model)**. It helps users quickly grasp key insights from long-form content.

## Features

- **Summarization from YouTube**: Extracts transcript and generates a concise summary.
- **Summarization from Web Pages**: Scrapes content from URLs and provides a structured summary.
- **Customizable Summaries**: Generates 300-word summaries based on extracted content.
- **Interactive UI**: Built with Streamlit for a smooth and intuitive user experience.

## Tech Stack

- **Python**
- **Streamlit**
- **LangChain**
- **Groq API (Gemma 2-9B-It model)**
- **Pytube** (for YouTube transcript extraction)
- **Unstructured** (for webpage content extraction)

## Installation

### Prerequisites

- Python 3.8+
- Groq API Key

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/PrinceGupta8/summarizer.git
   cd summarizer
   ```
2. **Create a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate     # On Windows
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application**
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Enter your Groq API Key** in the sidebar input box.
2. **Provide a YouTube video URL or a webpage URL** in the main input box.
3. **Click 'Summarize'** to generate a summary.
4. **Wait for the AI-generated summary** to appear in the output section.

## Example

**Input (YouTube URL):**

```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

**Output (Summary):**

```
The video explains the fundamentals of AI, discussing its applications and impact on various industries...
```

## API Key Setup

- Get your **Groq API Key** from [Groq](https://groq.com/).
- Set the API key as an environment variable or enter it in the Streamlit UI.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.

---

🚀 **Summarize YouTube videos and web pages effortlessly with AI-powered summaries!**

