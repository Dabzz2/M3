#GROUP ASSIGNMENT 3, PORTFOLIO EXERCISE 3: GPT MODELS


This project showcases the application of modern AI techniques, particularly GPT-based models and AI agents, to analyze and solve economic problems. The primary objective is to utilize FlowiseAI to build an automated workflow that processes and extracts insights from academic materials, specifically in economics. Additionally, an interactive Streamlit app is created to provide an accessible interface for querying and exploring the results.

The workflow begins with a File Loader component in FlowiseAI, which imports an academic text, such as David Romer's Advanced Macroeconomics, into the pipeline. To manage the complexity of the text, a Recursive Character Text Splitter divides it into manageable chunks of 1000 characters, with a 200-character overlap to maintain context. These text chunks are then processed using OpenAI Embeddings, which convert them into vector representations using the text-embedding-ada-002 model.

Once vectorized, the data is stored in an In-Memory Vector Store, which ensures efficient retrieval of relevant text based on user queries. For language processing and query handling, the ChatOpenAI component leverages the GPT-3.5-turbo model to generate insightful responses. The VectorDB QA Chain links the vector store with the language model, enabling the system to answer user questions accurately by retrieving and synthesizing information from the embedded text.



For example, users can ask the following question in the application: "What is the Solow model?"

The system will respond:
"The Solow model, also known as the Solow-Swan model, is an economic model that focuses on the long-term growth of an economy. It looks at the relationships between capital accumulation, population growth, and technological progress in determining an economy's output over time. The model simplifies the economy by focusing on key variables like output, capital, labor, and technological progress to understand how an economy grows and develops."

This response is generated by processing the uploaded material, such as David Romer - Advanced Macroeconomics. The system uses OpenAI Embeddings to vectorize the text and stores the processed data in a vector-based database. When a user submits a query, the VectorDB QA Chain retrieves the most relevant chunks of information from the document, and the GPT model refines and synthesizes this information to provide a clear and accurate answer.

The purpose of this workflow is to make complex economic concepts accessible and understandable to users, leveraging modern AI technology to extract and explain insights from academic resources effectively.