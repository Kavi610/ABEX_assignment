#Proofreads & Improves Content
from config import model

def review_content(content):
    """
    Proofreads and improves the content quality using Gemini.
    """
    try:
        prompt = f"Proofread and improve the following blog content for grammar, readability, and coherence:\n{content}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error reviewing content: {e}")
        return content  # Return original content if review fails
