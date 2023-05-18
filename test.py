import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer

def preprocess_text(text):
    # Tokenize text into sentences
    sentences = sent_tokenize(text)
    
    # Tokenize sentences into words and filter out stopwords
    stop_words = set(stopwords.words('english'))
    word_tokens = [word_tokenize(sentence) for sentence in sentences]
    filtered_words = [
        [word.lower() for word in sentence if word.isalpha() and word.lower() not in stop_words]
        for sentence in word_tokens
    ]
    
    # Lemmatize words
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [
        [lemmatizer.lemmatize(word) for word in sentence]
        for sentence in filtered_words
    ]
    
    # Flatten the list of words into a single list
    flattened_words = [word for sentence in lemmatized_words for word in sentence]
    
    return flattened_words

# Example usage:
document = """
   You should only add tooltips to HTML elements that are traditionally keyboard-focusable and interactive (such as links or form controls). Although arbitrary HTML elements (such as <span>s) can be made focusable by adding the tabindex="0" attribute, this will add potentially annoying and confusing tab stops on non-interactive elements for keyboard users. In addition, most assistive technologies currently do not announce the tooltip in this situation.
    """
preprocessed_words = preprocess_text(document)
print(str(preprocessed_words))

