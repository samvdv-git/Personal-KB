from personal_kb.llm import generate, create_note
from personal_kb.parsers import parse_note
from personal_kb.notes import save_note


def main():
    question = input("Vraag: ")

    note_text = create_note(question)

    note = parse_note(note_text)

    path = save_note(note)

    print(f"\nNote opgeslagen in: {path}")


if __name__ == "__main__":
    main()
