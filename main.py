import argparse
from app.services.data_processing import preprocess_text
from app.services.ner_analysis import extract_named_entities
from app.services.sentiment_analysis import analyze_sentiment
from app.services.visualization import generate_wordcloud

def main(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    tokens, cleaned_text = preprocess_text(text)
    named_entities = extract_named_entities(cleaned_text)
    sentiment = analyze_sentiment(cleaned_text)

    print("\nNamed Entities:", named_entities)
    print("\nSentiment Analysis:", sentiment)

    generate_wordcloud(cleaned_text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="Path to the text file")
    args = parser.parse_args()

    main(args.file_path)
