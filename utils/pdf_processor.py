def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    text = ""
    try:
        # Try PyPDF2 first
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        
        # If text is empty or too short, try OCR
        if len(text.strip()) < 100:
            text = extract_text_using_ocr(pdf_path)
    except Exception as e:
        print(f"Error extracting text: {e}")
        text = extract_text_using_ocr(pdf_path)
    
    return clean_text(text) 