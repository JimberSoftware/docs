import re

def transform_content(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    # Patterns for images and block quotes
    image_with_size_pattern = re.compile(r'!\[(.*?)\]\((.*?)\s*=\s*(\d+)x\)\s*(\{.*?\})?')
    image_without_size_pattern = re.compile(r'!\[(.*?)\]\((.*?)\)\s*(\{.*?\})?')
    block_quote_info_pattern = re.compile(r'^>\s*(.*?)\s*\{\.is-info\}')
    block_quote_warning_pattern = re.compile(r'^>\s*(.*?)\s*\{\.is-warning\}')
    inline_style_pattern = re.compile(r'\{\.[-\w\s]+\}')

    for line in lines:
        if image_with_size_pattern.search(line):
            new_line = image_with_size_pattern.sub(r"\n![\1](\2 ':size=\3')\n", line)
        elif image_without_size_pattern.search(line):
            new_line = image_without_size_pattern.sub(r'\n![\1](\2)\n', line)
        elif block_quote_info_pattern.search(line):
            # Specific handling for .is-info
            new_line = block_quote_info_pattern.sub(r'> [!INFO]\n> \1', line)
        elif block_quote_warning_pattern.search(line):
            # Specific handling for .is-warning
            new_line = block_quote_warning_pattern.sub(r'> [!WARNING]\n> \1', line)
        else:
            # Remove inline styles and not matched patterns
            new_line = inline_style_pattern.sub('', line)
        new_lines.append(new_line)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Example usage
input_md_file = 'input.md'  # Path to your input markdown file
output_md_file = 'output.md'  # Path to your output markdown file

transform_content(input_md_file, output_md_file)
