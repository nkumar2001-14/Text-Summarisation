Text Summarization:
--------------------

Text summarization is the process of generating a concise summary of a document or a set of documents. The goal is to extract the most important information from the source while maintaining the actual meaning.

Process Steps:
--------------

1.Text Cleaning:
Remove stopwords (e.g., "the," "at," "on") and punctuation symbols.

2.Sentence Tokenization:
Split the text into sentences.

3.Word Tokenization:
Split sentences into words.
Calculate the word frequency of each sentence, considering normalized values.

4.Generate Summary:
Provide the summary based on the highest word frequency.

5.Using Libraries:
Use nltk (Natural Language Toolkit) or other libraries for text processing.
Import the required libraries to implement text summarization.
