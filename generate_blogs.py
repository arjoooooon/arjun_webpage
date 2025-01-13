import os
import markdown
from pathlib import Path

# Directory containing Markdown files
BLOGS_DIR = "blogs"
OUTPUT_DIR = "generated_blogs"

# Template for the blog post HTML
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: auto;
            padding: 20px;
        }}
    </style>
</head>
<body>
    {content}
</body>
</html>
"""

def convert_markdown_to_html(md_path, output_path):
    """Convert a Markdown file to an HTML file."""
    with open(md_path, "r", encoding="utf-8") as md_file:
        md_content = md_file.read()
    
    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content, extensions=["fenced_code", "md_in_html"])
    
    # Extract the title (assuming the first line is the title)
    title = md_content.splitlines()[0].replace("# ", "").strip()
    
    # Create the final HTML content
    html_output = HTML_TEMPLATE.format(title=title, content=html_content)
    
    # Save the HTML file
    with open(output_path, "w", encoding="utf-8") as html_file:
        html_file.write(html_output)

def generate_html_files():
    """Generate HTML files for all Markdown blogs."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for md_file in Path(BLOGS_DIR).glob("*.md"):
        output_file = Path(OUTPUT_DIR) / f"{md_file.stem}.html"
        convert_markdown_to_html(md_file, output_file)
        print(f"Generated: {output_file}")

if __name__ == "__main__":
    generate_html_files()
