# """
#     this  is responsible for working with data processing
# """
# import os
# import spacy
# from spacy.lang.en.stop_words import STOP_WORDS
# import string


# class TextProcessing:
    
#     def __init__(self):
#         self.text_data = ""
#         self.tokens = []
    
    
#     def read_text_file(self, file_path: str):
#         """
#             this function is responsible to reading the text file
#         """        
#         if os.path.exists(file_path):
#             with open(file_path, 'r') as f:
#                 self.text_data = f.read()
                
#             print("File Read Successfully")
            
#             return self.text_data
            
#         else:
#             print("File Not Found")
#         return None
    
    
#     def tokenization(self, text: str):
        
#         """
#             this will tokenize and lemmetize the text properly
#         """
        
#         try:
#             nlp = spacy.load("en_core_web_sm")
#             lemmatizer = nlp.get_pipe("lemmatizer")
#             doc = nlp(text)
#             for token in doc:
#                 self.tokens.append(token.lemma_)
#             return self.tokens
            
#         except Exception as e:
#             print(f"Error Occured: {e}")
#             return self.tokens
            
#     def remove_stopwords_punctuation(self, tokens: list):
#         tokens = [word for word in tokens if word not in STOP_WORDS and word not in string.punctuation]
#         return tokens
    
    
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')

def preprocess_text(text):
    tokens = word_tokenize(text.lower())  # Tokenization & lowercase
    stop_words = set(stopwords.words("english"))
    lemmatizer = WordNetLemmatizer()

    cleaned_tokens = [lemmatizer.lemmatize(word) for word in tokens if word.isalnum() and word not in stop_words]
    cleaned_text = " ".join(cleaned_tokens)
    
    return cleaned_tokens, cleaned_text
