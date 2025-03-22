#Generates Blog Outline
from config import model

def generate_outline(topic):
    """
    Generates a structured outline for the blog post using Gemini.
    """
    try:
        prompt = f"Create a detailed blog outline for the topic: '{topic}'. Include an introduction, main sections, and a conclusion."
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error generating outline: {e}")
        return f"""
# {topic}

## Introduction
## Main Sections
### 1. Section 1
### 2. Section 2
### 3. Section 3
## Conclusion
"""
