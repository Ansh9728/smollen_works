"""
    this will analysis The Named entity origanization
    Note:: in that case Spacy Output is better
"""
# uncomment for using the spacy for analysis
import spacy
nlp = spacy.load("en_core_web_sm")

def extract_named_entities(text):
    doc = nlp(text)
    # entities = {"PERSON": [], "ORG": [], "GPE": []}
    entities = {}

    for ent in doc.ents:
        if ent.label_ not in entities:
            entities[ent.label_] = []
            
        entities[ent.label_].append(ent.text)

    return entities


#transformer for entity recognization
# uncomment to use transformer based
# from transformers import pipeline

# def extract_named_entities(text):
#     # Initialize the named entity recognition pipeline
#     ner = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")
    
#     # Get the named entities from the text
#     entities = ner(text)
    
#     # Convert float32 to float to ensure it is JSON serializable
#     for entity in entities:
#         entity['score'] = float(entity['score'])  # Convert np.float32 to float
    
#     print(entities)  # Optional, for debugging
#     return entities