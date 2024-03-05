import re

def transform_content(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    # Matches images with explicit size and optional inline styles
    image_with_size_pattern = re.compile(r'!\[(.*?)\]\((.*?)\s*=\s*(\d+)x\)\s*(\{.*?\})?')
    # Matches images without explicit size but with inline styles
    image_without_size_pattern = re.compile(r'!\[(.*?)\]\((.*?)\)\s*(\{.*?\})?')
    block_quote_warning_pattern = re.compile(r'^>\s*(.*?)\s*\{\.is-warning\}')
    block_quote_success_pattern = re.compile(r'^>\s*(.*?)\s*\{\.is-(success|info)\}')
    inline_style_pattern = re.compile(r'\{\.[-\w\s]+\}')

    for line in lines:
        if image_with_size_pattern.search(line):
            # Use double quotes for the outer string to avoid needing to escape single quotes
            new_line = image_with_size_pattern.sub(r"\n![\1](\2 'size:=\3x')\n", line)
        elif image_without_size_pattern.search(line):
            # Handle images without explicit size or with inline styles, ensure newlines
            new_line = image_without_size_pattern.sub(r'\n![\1](\2)\n', line)
        elif block_quote_warning_pattern.search(line) or block_quote_success_pattern.search(line):
            # Replace block quotes with warning/info format
            new_line = block_quote_warning_pattern.sub(r'> [!WARNING]\n> \1', line)
            new_line = block_quote_success_pattern.sub(r'> [!INFO]\n> \1', new_line)
        else:
            # Remove inline styles
            new_line = inline_style_pattern.sub('', line)
        new_lines.append(new_line)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Example usage
input_md_file = 'input.md'  # Adjust with the path to your input file
output_md_file = 'output.md'  # Adjust with the path to your output file

transform_content(input_md_file, output_md_file)
