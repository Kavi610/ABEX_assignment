#Orchestrates the Entire Process
from research_agent import fetch_trending_topics
from content_planning_agent import generate_outline
from content_generation_agent import generate_blog_content
from seo_optimization_agent import optimize_seo
from review_agent import review_content

def main():
    # Step 1: Research Agent
    print("Fetching trending HR topics...")
    topics = fetch_trending_topics()
    print(f"Trending Topics: {topics}")

    # Ensure topics list is not empty
    if not topics:
        print("No topics found. Exiting program.")
        return

    # Select the first topic
    topic = topics[0]
    print(f"Selected Topic: {topic}")

    # Step 2: Content Planning Agent
    print("Generating blog outline...")
    outline = generate_outline(topic)
    print(f"Outline:\n{outline}")

    # Step 3: Content Generation Agent
    print("Generating blog content...")
    blog_content = generate_blog_content(outline)
    print(f"Blog Content:\n{blog_content}")

    # Step 4: SEO Optimization Agent
    print("Optimizing for SEO...")
    optimized_content = optimize_seo(blog_content)
    print(f"Optimized Content:\n{optimized_content}")

    # Step 5: Review Agent
    print("Reviewing and finalizing content...")
    final_content = review_content(optimized_content)
    print(f"Final Content:\n{final_content}")

    # Save the final blog post
    with open("blog_post.md", "w") as file:
        file.write(final_content)
    print("Blog post saved as 'blog_post.md'.")

if __name__ == "__main__":
    main()
