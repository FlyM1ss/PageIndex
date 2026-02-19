"""
Local query tool for PageIndex JSON results.
Extracts summaries from the parsed structure and synthesizes answers via LLM.
Supports both OpenAI and Google Gemini (auto-detected from .env).
"""

import json
import sys
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

gemini_key = os.getenv("GEMINI_API_KEY")
if gemini_key:
    client = OpenAI(api_key=gemini_key, base_url=GEMINI_BASE_URL)
    DEFAULT_MODEL = "gemini-2.0-flash"
else:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    DEFAULT_MODEL = "gpt-4o"

# Sections to skip when building context (saves tokens, reduces noise)
SKIP_SECTIONS = {"Endnotes", "Bibliography", "Acknowledgments"}


def load_structure(json_path: str) -> dict:
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_summaries(nodes: list, depth: int = 0) -> str:
    """Recursively extract summaries from the tree, preserving hierarchy via indentation."""
    lines = []
    for node in nodes:
        title = node.get("title", "Untitled")
        if title in SKIP_SECTIONS:
            continue

        summary = node.get("summary", "")
        pages = f"(pp. {node['start_index']}-{node['end_index']})"
        indent = "  " * depth
        prefix = "#" * (depth + 1)

        lines.append(f"{indent}{prefix} {title} {pages}")
        if summary:
            lines.append(f"{indent}{summary}")
        lines.append("")

        children = node.get("nodes", [])
        if children:
            lines.append(extract_summaries(children, depth + 1))

    return "\n".join(lines)


def should_skip_section(title: str) -> bool:
    """Decide whether a section should be included in the context.

    TODO: Customize this for each use case. For concept summaries,
    you probably want to skip reference material. For citation queries,
    you'd want to include them.
    """
    return title in SKIP_SECTIONS


def query_document(json_path: str, question: str, model: str = DEFAULT_MODEL) -> str:
    """Query a PageIndex JSON structure with a natural language question."""
    doc = load_structure(json_path)
    doc_name = doc.get("doc_name", "Unknown document")
    structure = doc.get("structure", [])

    context = extract_summaries(structure)

    system_prompt = (
        f"You are an expert analyst for the document: '{doc_name}'.\n"
        "Below is the hierarchical summary of every section in the document.\n"
        "Use this to answer the user's question thoroughly and accurately.\n"
        "Reference specific sections/pages when relevant.\n"
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"## Document Structure & Summaries\n\n{context}\n\n---\n\n## Question\n\n{question}"},
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python query_local.py <path_to_json> \"<your question>\"")
        print()
        print("Example:")
        print('  python query_local.py results/DataAndSociety_MediaManipulationAndDisinformationOnline_structure.json \\')
        print('    "Summarize all key concepts introduced in the book and briefly talk about connections between them"')
        sys.exit(1)

    json_path = sys.argv[1]
    question = sys.argv[2]

    if not os.path.exists(json_path):
        print(f"Error: File not found: {json_path}")
        sys.exit(1)

    print(f"Querying: {os.path.basename(json_path)}")
    print(f"Question: {question}")
    print("-" * 60)
    answer = query_document(json_path, question)
    print(answer)
