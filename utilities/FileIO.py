def save_text(filepath: str, text: str):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

def load_text(filepath: str) -> str:
    with open(filepath, encoding='utf-8') as f:
        text = f.read()
        return text