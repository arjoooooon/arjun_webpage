import os
import markdown
from pathlib import Path

# Directory containing Markdown files
BLOGS_DIR = "blogs_md"
OUTPUT_DIR = "blogs"

# Template for the blog post HTML
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Arjun Taneja</title>
    <link rel="icon" type="image/png" href="../favicomatic/favicon-32x32.png"/>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <script src="https://kit.fontawesome.com/b1bec8acd8.js" crossorigin="anonymous"></script>

    <style>
        body {{
            font-family: 'Roboto', sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
            background-color: #f8f9fa;
            color: #333;
        }}

        header {{
            background-color: #007bff;
            color: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1em 2em;
        }}

        header h1 {{
            margin: 0;
            font-size: 1.5em;
        }}
        nav {{
            display: flex;
            gap: 15px;
        }}

        nav a {{
            text-decoration: none;
            color: white;
            font-weight: bold;
        }}

        nav a:hover {{
            text-decoration: underline;
        }}

        main {{
            max-width: 800px;
            margin: auto;
            padding: 20px;
            flex: 1;
        }}
        article {{
            margin-bottom: 20px;
            border-bottom: 1px solid #ddd;
            padding-bottom: 10px;
        }}
        footer {{
            background-color: #007bff;
            color: white;
            text-align: center;
            padding: 1em 0;
            margin-top: auto;
        }}

        footer p {{
            margin: 0;
        }}

        .socials {{
            display: flex;
            justify-content: center;
            gap: 30px;
        }}

        .socials a {{
            color: white;
            text-decoration: none;
            font-size: 1.2em;
        }}
        .socials a:hover {{
            text-decoration: underline;
        }}

        @media (max-width: 768px) {{
            header {{
                flex-direction: column;
                text-align: center;
                padding: 1em;
            }}

            nav {{
                flex-wrap: wrap;
                justify-content: center;
                margin-top: 1em;
                gap: 10px;
            }}

            .awards-projects img {{
                width: 200px;
                height: 200px;
                margin: 0 auto 15px auto;
            }}

            .awards-projects ul li {{
                flex-direction: column;
                align-items: flex-start;
            }}

            .awards-projects div {{
                text-align: center;
            }}

            .awards-projects div p {{
                text-align: left;
            }}
        }}
    </style>
</head>
<body>
    <header>
        <h1>Arjun Taneja</h1>
        <nav>
            <a href="../index.html">Home</a>
            <a href="../blog.html">Blog</a>
        </nav>
    </header>

    <main>
        {content}
    </main>

    <footer>
        <div class="socials">
            <a href="https://github.com/arjoooooon" target="_blank"><i class="fab fa-github"></i></a>
            <a href="https://linkedin.com/in/arjuntaneja" target="_blank"><i class="fab fa-linkedin"></i></a>
            <a href="mailto:arjun.taneja02@gmail.com"><i class="fa-solid fa-envelope"></i></a>
        </div>
    </footer>
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
