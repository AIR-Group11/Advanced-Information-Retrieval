# Semantic Song Retrieval System: A Transformer-Based Approach

## Abstract

This project presents a semantic song retrieval system that leverages transformer-based models to analyze song lyrics and retrieve songs based on lyrical semantics. By integrating pre-trained transformer models, the system bridges the gap between natural language user queries and computational understanding of song lyrics. It evaluates performance and highlights potential improvements for future development.

---

## Motivation

Finding songs based on lyrics can be challenging, especially when users only recall small fragments or describe them vaguely. Traditional keyword-based search methods often fail to capture the meaning behind the lyrics or handle incomplete queries. This inspired the creation of a semantic song retrieval system that focuses on understanding the meaning of lyrics and user input through advanced transformer-based models.

## What It Does

The system enables users to search for songs based on the semantic meaning of their lyrics. Users can provide natural language queries, ranging from specific lyric fragments to vague or descriptive terms. The system processes the input, retrieves semantically relevant lyrics, and returns a list of matching songs, including metadata such as title and artist.

### Key Features:

1. **Natural Language Query Support:** Handles vague, descriptive, or incorrect user queries.
2. **Transformer Models for Embeddings:** Utilizes fine-tuned transformer models to analyze and compare lyrical semantics.
3. **Vector Search Integration:** Leverages Pinecone for efficient storage and retrieval of high-dimensional embeddings.
4. **Re-ranking Mechanism:** Employs a cross-encoder model to refine search results for better accuracy.

---

## Dataset

The project uses the **50 Years of Pop Music Lyrics** dataset, sourced from [Walker's GitHub repository](https://github.com/walkerkq/musiclyrics/tree/master). This dataset contains:

- **5100 items** with key features like song title, artist name, and full lyrics.
- Lyrics from Billboard Year-End Hot 100 songs spanning 1965-2015.
- Preprocessed to ensure completeness and standardization, with missing values removed and short lyrics excluded.

---

## How It Works

1. **Data Preparation:**

   - Lyrics are split into chunks using the RecursiveCharacterTextSplitter from the LangChain library, ensuring contextual integrity with overlapping segments.

2. **Embedding Generation:**

   - Song lyrics chunks are converted into 768-dimensional embedding vectors using the `all-MiniLM-L6-v2` model from the `sentence-transformers` library.
   - The embeddings are stored in Pinecone, a vector database, along with metadata.

3. **Query Processing:**

   - User queries are refined using a GPT-based model to enhance clarity and alignment with stored embeddings.
   - The refined query is encoded into a vector using the same transformer model.

4. **Search and Matching:**
   - Pinecone performs a cosine similarity search to identify semantically closest matches.
   - Results are further re-ranked using a cross-encoder model (`cross-encoder/ms-marco-MiniLM-L-6-v2`) for enhanced relevance.

---

## Setup Instructions

### Prerequisites

- Python 3.8+
- Access to GPT API and Pinecone API (users need their own keys).

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AIR-Group11/Advanced-Information-Retrieval.git
   cd Advanced-Information-Retrieval
   ```
2. Open main.ipynb in a Jupyter Notebook environment.

   - Follow the steps outlined in the notebook to set up the environment and execute the project.

3. Add your API keys:
   - GPT API Key: Provide your key in the configuration file or environment variable.
   - Pinecone API Key: Set up and provide your Pinecone API credentials.

### Contributors

**_Naida Nožić_**: Dataset processing, embedding vectors, Pinecone integration, re-ranking, and related tasks.
**_Petra Buršić_**: Dataset processing, embedding vectors, Pinecone integration, re-ranking, and related tasks.
**_Faruk Šahat_**: Evaluation and results.
**_Maksim Madžar_**: GPT integration for user query refinement and fine-tuning.

### Future work

- Expand the dataset to include more diverse genres and languages.
- Integrate a user interface for easier access and usability.
- Try additional fine-tuning approaches to improve retrieval results.
