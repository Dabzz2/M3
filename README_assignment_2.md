Link to streamlit: https://huggingface.co/spaces/Chri12345/Best_Guess


# SBERT and Semantic Search Assignment

This project demonstrates the use of **SBERT (Sentence-BERT)** for implementing a semantic search system combined with text summarization. The objective is to explore innovative applications of SBERT for retrieving and processing contextually relevant information while providing concise and user-friendly outputs.

The dataset used for this project is the **"Natural Questions"** dataset from Hugging Face, which contains question-answer pairs that are ideal for training and evaluating semantic search systems. The semantic search is powered by the **`allenai-specter`** SBERT model, which encodes queries and text into dense embeddings to calculate semantic similarity. For summarization, the **`sshleifer/distilbart-cnn-12-6`** model is used to condense multiple retrieved answers into a single concise response.

The implementation integrates semantic search and summarization into a seamless pipeline. First, the system retrieves the top 5 most relevant results from the corpus based on semantic similarity using cosine similarity. These results are then combined into a single text, which is processed by the summarization pipeline to generate a brief and coherent summary tailored to the query.

For example, when querying *"Who made the song my achy breaky heart?"*, the system provides a detailed semantic search retrieval followed by a summary about Billy Ray Cyrus's song "Achy Breaky Heart." Similarly, the query *"Who is wimpy kid?"* results in a summary mentioning a television show, though with some mismatch in relevance. These examples highlight the system's potential as well as areas for refinement.

The key features of this project include its innovative combination of semantic search and summarization, the use of state-of-the-art pretrained models from Hugging Face, and its ability to handle diverse queries dynamically. While the current implementation demonstrates strong capabilities, there is room for improvement. Enhancements could include better filtering or re-ranking of semantic search results, tuning summarization parameters like `max_length` for more complete outputs, and incorporating additional datasets or models to broaden the application's scope.
