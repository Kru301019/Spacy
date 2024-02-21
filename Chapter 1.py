# Sure! Here's how you can import the spaCy library in Python:
import spacy

# Load a pre-trained language model (e.g., English)
nlp = spacy.load("en_core_web_sm")

# Now you can use the `nlp` object to process text!
text = "This is an example sentence."
doc = nlp(text)

# Access various linguistic annotations
for token in doc:
    print(f"Token: {token.text}, Lemma: {token.lemma_}, POS: {token.pos_}")

# Remember to install spaCy first using pip:
# pip install spacy
