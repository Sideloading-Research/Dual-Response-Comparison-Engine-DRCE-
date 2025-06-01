# parse_markdown.py

def parse_markdown_answers(file_path):
    """Parse Q&A pairs from markdown file with format:
    # Question
    Answer
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    qa_pairs = {}
    current_question = None
    buffer = []

    for line in lines:
        line = line.strip()
        if line.startswith("# "):
            if current_question:
                qa_pairs[current_question] = "\n".join(buffer).strip()
            current_question = line[2:].strip()
            buffer = []
        elif current_question:
            buffer.append(line)

    if current_question:
        qa_pairs[current_question] = "\n".join(buffer).strip()

    return qa_pairs
