from backend.models.document import Document


def search_documents(
    query: str,
    documents: list[Document]
) -> list[Document]:
    results: list[Document] = []

    for document in documents:
        if query.lower() in document.content.lower():
            results.append(document)

    return results