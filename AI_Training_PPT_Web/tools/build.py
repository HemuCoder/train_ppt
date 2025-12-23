import os

def build():
    base_dir = os.getcwd()
    src_dir = os.path.join(base_dir, 'src')
    dist_dir = os.path.join(base_dir, 'dist')
    chapters_dir = os.path.join(src_dir, 'chapters')
    
    # Read layout
    with open(os.path.join(src_dir, 'layout.html'), 'r', encoding='utf-8') as f:
        layout = f.read()
    
    # Read chapters
    slides_content = ""
    chapter_files = sorted(os.listdir(chapters_dir))
    
    for filename in chapter_files:
        if filename.endswith('.html'):
            filepath = os.path.join(chapters_dir, filename)
            print(f"Merging {filename}...")
            with open(filepath, 'r', encoding='utf-8') as f:
                slides_content += f.read() + "\n"
    
    # Inject content
    final_html = layout.replace('<!-- SLIDES_CONTENT -->', slides_content)
    
    # Write to dist
    with open(os.path.join(dist_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    # Copy static assets (simple read/write to avoid depending on shutil if possible, but shutil is fine)
    # Merge CSS
    print("Merging CSS...")
    styles_content = ""
    # 1. Base CSS
    with open(os.path.join(src_dir, 'styles', 'base.css'), 'r', encoding='utf-8') as f:
        styles_content += f.read() + "\n"
    
    # 2. Chapter CSS (if any)
    styles_chapters_dir = os.path.join(src_dir, 'styles', 'chapters')
    if os.path.exists(styles_chapters_dir):
        css_files = sorted(os.listdir(styles_chapters_dir))
        for filename in css_files:
            if filename.endswith('.css'):
                print(f"Merging CSS: {filename}...")
                with open(os.path.join(styles_chapters_dir, filename), 'r', encoding='utf-8') as f:
                    styles_content += f.read() + "\n"

    with open(os.path.join(dist_dir, 'style.css'), 'w', encoding='utf-8') as f:
        f.write(styles_content)

    # Copy script
    import shutil
    shutil.copy(os.path.join(src_dir, 'script.js'), os.path.join(dist_dir, 'script.js'))
    
    # Copy image directory
    image_src = os.path.join(base_dir, 'image')
    image_dist = os.path.join(dist_dir, 'image')
    if os.path.exists(image_dist):
        shutil.rmtree(image_dist)
    if os.path.exists(image_src):
        print("Copying image directory...")
        shutil.copytree(image_src, image_dist)
    
    print("Build complete. Output in dist/")

if __name__ == "__main__":
    build()
