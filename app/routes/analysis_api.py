from flask import Flask, request, jsonify, Blueprint, make_response
from app.services.data_processing import preprocess_text
from app.services.ner_analysis import extract_named_entities
from app.services.sentiment_analysis import analyze_sentiment

analysis_bp = Blueprint('analysis', __name__, url_prefix='/analysis')

@analysis_bp.route('/ner', methods=['POST'])
def analyze_text():
    
    if 'file' in request.files:
        file = request.files['file']
        text = file.read().decode('utf-8')
    else:
        data = request.get_json()
        text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    _, cleaned_text = preprocess_text(text)
    entities = extract_named_entities(cleaned_text)
    sentiment = analyze_sentiment(cleaned_text)

    return jsonify({"named_entities": entities, "sentiment": sentiment})


@analysis_bp.route('/test')
def test():
    return make_response("successy establishest", 200)