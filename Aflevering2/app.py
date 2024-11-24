import os
from sentence_transformers import SentenceTransformer, util
from datasets import load_dataset
from datasets import load_dataset
from transformers import pipeline
import streamlit as st



dataset_id = "sentence-transformers/natural-questions"
dataset_file = load_dataset(dataset_id, split="train")

# Use the allenai-specter model with SentenceTransformers
model = SentenceTransformer('allenai-specter')

# Prepare paper texts by combining query and answer fields
paper_texts = [
    record['query'] + '[SEP]' + record['answer'] for record in dataset_file.select(range(32))
]

# Compute embeddings for all paper texts
corpus_embeddings = model.encode(paper_texts, convert_to_tensor=True, show_progress_bar=True)

# Function to search for answers given a query
def search_papers(query):
    # Encode the query
    query_embedding = model.encode(query, convert_to_tensor=True)

    # Perform semantic search
    search_hits = util.semantic_search(query_embedding, corpus_embeddings)
    search_hits = search_hits[0]  # Get the hits for the first query

    print("\n\nQuery:", query)
    print("Most similar answers:")
    for hit in search_hits[:5]:  # Limit to top 5 results for clarity
        related_text = dataset_file[int(hit['corpus_id'])]  # Access related record
        print("{:.2f}\tAnswer: {}".format(
            hit['score'], related_text['answer']
        ))


# Summarization pipeline
summarizer = pipeline("summarization")

# Collect the relevant answers from the search function
def search_papers_and_summarize(query, max_summary_length=45):
    # Encode the query
    query_embedding = model.encode(query, convert_to_tensor=True)

    # Perform semantic search
    search_hits = util.semantic_search(query_embedding, corpus_embeddings)
    search_hits = search_hits[0]  # Get the hits for the first query

    # Collect answers from top hits
    answers = []
    for hit in search_hits[:5]:  # Limit to top 5 results
        related_text = dataset_file[int(hit['corpus_id'])]
        answers.append(related_text['answer'])

    # Combine answers into a single text for summarization
    combined_text = " ".join(answers)

    # Summarize the combined text
    summary = summarizer(combined_text, max_length=max_summary_length, clean_up_tokenization_spaces=True)
    print("Summary:")
    print(summary[0]['summary_text'])


title = st.text_input("Ask a question", "What is Wimpy Kid")
new_preds = search_papers_and_summarize(title)
st.write("The Answer is", new_preds)

