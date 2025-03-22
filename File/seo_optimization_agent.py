#Optimizes for SEO
from config import model

def optimize_seo(content):
    """
    Optimizes the blog content for SEO using Gemini.
    """
    try:
        prompt = f"Optimize the following blog content for SEO. Add relevant keywords, meta descriptions, and ensure proper heading tags:\n{content}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error optimizing SEO: {e}")
        return content  # Return original content if optimization fails
