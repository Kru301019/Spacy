# Sure! Here's how you can import the spaCy library in Python:
import spacy

# Load a pre-trained language model (e.g., English)
nlp = spacy.load("en_core_web_sm")

# Now you can use the `nlp` object to process text!


def testSpacy():
    
    doc = nlp('hello world today i am starting nlp')
    # Access various linguistic annotations
    for token in doc:
        print(token)

    # Remember to install spaCy first using pip:
    # pip install spacy
testSpacy()    

def lexiOne():
    # Process the text
    doc = nlp(
        "In 1990, more than 60% of people in East Asia were in extreme poverty. "
        "Now less than 4% are."
    )

    # Iterate over the tokens in the doc
    for token in doc:
        # Check if the token resembles a number
        if token.like_num:
            # Get the next token in the document
            print(token.i + 1)
            next_token = doc[token.i + 1]
            # Check if the next token's text equals "%"
            if next_token.text == "%":
                print("Percentage found:", token.text)


#lexiOne()
