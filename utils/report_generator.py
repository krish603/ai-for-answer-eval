def assign_marks(similarity_score, key_points_coverage=None):
    """Assign marks out of 10 based on similarity score and key points coverage."""
    # Base score from similarity (0-1 scale to 0-10 scale)
    base_score = similarity_score * 10
    
    # Adjust based on key points coverage if available
    if key_points_coverage is not None:
        # Key points contribute up to 30% of the final score
        key_points_score = key_points_coverage * 3
        final_score = (base_score * 0.7) + key_points_score
    else:
        final_score = base_score
    
    # Round to one decimal place
    return round(min(10, max(0, final_score)), 1)