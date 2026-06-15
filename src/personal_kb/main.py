from personal_kb.llm import generate


def main():
    response = generate(
        "Leg in maximaal 3 zinnen uit wat RAG is."
    )

    print("\n=== MODEL RESPONSE ===\n")
    print(response)


if __name__ == "__main__":
    main()