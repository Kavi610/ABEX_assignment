#Generates Blog Content
from config import model

def generate_blog_content(outline):
    """
    Generates the blog content based on the outline using Gemini.
    """
    try:
        prompt = f"Write a detailed, engaging, and professional blog post based on the following outline:\n{outline}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error generating blog content: {e}")
        return "Error: Blog content could not be generated."
