from pathlib import Path

from personal_kb.models import Note

VAULT_PATH = Path("vault/Inbox")


def save_note(note: Note) -> Path:
    VAULT_PATH.mkdir(parents=True, exist_ok=True)

    filename = (
        note.title.lower()
        .replace(" ", "_")
        .replace("/", "_")
    )

    filepath = VAULT_PATH / f"{filename}.md"

    markdown = f"""# {note.title}

## Samenvatting

{note.summary}

## Inhoud

{note.content}
"""

    filepath.write_text(markdown, encoding="utf-8")

    return filepath