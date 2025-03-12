from sentence_transformers import SentenceTransformer, util

def calculate_similarity(text1, text2):
    """Calculate similarity between two texts."""
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Encode texts to get embeddings
    embedding1 = model.encode(text1, convert_to_tensor=True)
    embedding2 = model.encode(text2, convert_to_tensor=True)
    
    # Calculate cosine similarity
    similarity = util.pytorch_cos_sim(embedding1, embedding2).item()
    
    return similarity