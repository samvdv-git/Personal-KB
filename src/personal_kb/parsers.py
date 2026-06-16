from personal_kb.models import Note

def parse_note(text: str) -> Note:
    title = text.split("TITLE:")[1].split("SUMMARY:")[0].strip()

    summary = text.split("SUMMARY:")[1].split("CONTENT:")[0].strip()

    content = text.split("CONTENT:")[1].strip()

    return Note(
        title=title,
        summary=summary,
        content=content,
    )
