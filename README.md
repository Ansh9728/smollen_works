# FastAPI Text Analysis Application

## Overview
This application provides endpoints for analyzing text using Named Entity Recognition (NER) and Sentiment Analysis.

## Requirements
- Python 3.x
- Flask
- TextBlob
- SpaCy
- Matplotlib
- WordCloud

## Installation
1. Clone the repository.
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
To run the FastAPI application, execute the following command:
```bash
python run.py
```

The application will start on `http://127.0.0.1:5000`.

## Endpoints

### POST /analysis/ner
This endpoint analyzes the provided text for named entities and sentiment.

#### Input Format
You can send the text in two ways:
1. **File Upload**: Send a file containing the text only upload .txt file.
2. **JSON Payload**: Send a JSON object with the following structure:
   ```json
   {
       "text": "Your text goes here."
   }
   ```

#### Example Request (JSON)
```bash
curl -X POST http://127.0.0.1:5000/analysis/ner -H "Content-Type: application/json" -d '{"text": "Your text goes here."}'
```

#### Example Response
```json
{
    "named_entities": {
        "PERSON": ["John Doe"],
        "ORG": ["OpenAI"],
        "GPE": ["San Francisco"]
    },
    "sentiment": "Positive"
}
```

## Cloning the Repository
To clone the repository, use the following command:
```bash
git clone <repository_url>
```
Replace `<repository_url>` with the URL of the repository.

## Running the Main Script
To run the `main.py` file for generating a word cloud and performing other analyses, execute the following command:
```bash
python main.py <path_to_text_file>
```
Replace `<path_to_text_file>` with the path to the text file you want to analyze.

### Example Command
```bash
python main.py test.txt
```

### Input Format
The input file should contain plain text. The script will read the text, perform preprocessing, extract named entities, analyze sentiment, and generate a word cloud.

## Setup Script
To automate the setup process, you can use the `setup.sh` script. Run the following command:
```bash
bash setup.sh
```
This will install the required packages for the project.

