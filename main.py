import os
import sys

# The joke is a one-liner about AI coding agents.
# It must be exactly the same on every run.
JOKE = "My agent claimed it fixed the bug, then spent an hour documenting the file it just deleted."

def main():
    # Resolve output directory
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    file_path = os.path.join(output_dir, "entry.txt")
    
    # Ensure directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Write the joke
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(JOKE)
    except Exception as e:
        print(f"Error writing to {file_path}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
