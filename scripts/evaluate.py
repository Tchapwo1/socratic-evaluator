"""
Socratic Reasoning & Philosophical Evaluation Engine
Autonomous Agentic Skill for Dialectical Analysis & Moral Dilemmas
"""

import os
import sys
import json
import argparse
from typing import List, Dict, Any, Optional

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
QUESTIONS_FILE = os.path.join(DATA_DIR, "questions.json")
PROMPTS_FILE = os.path.join(DATA_DIR, "prompts.json")

def load_questions() -> List[Dict[str, Any]]:
    if not os.path.exists(QUESTIONS_FILE):
        return []
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def load_prompts() -> List[Dict[str, Any]]:
    if not os.path.exists(PROMPTS_FILE):
        return []
    with open(PROMPTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def search_questions(query: str, questions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    q_lower = query.lower().strip()
    matches = []
    for item in questions:
        text_corpus = (
            item.get("q", "") + " " +
            item.get("tip", "") + " " +
            " ".join(opt.get("text", "") for opt in item.get("options", []))
        ).lower()
        if q_lower in text_corpus:
            matches.append(item)
    return matches

def get_dialectical_structure(subject: str) -> Dict[str, Any]:
    """Generates standard Hegelian/Socratic tripartite dissertation outline"""
    return {
        "subject": subject,
        "methodology": "Dissertation Dialectique (Thèse / Antithèse / Synthèse)",
        "paradox_identification": "Identifier le point de tension : pourquoi le sens commun répond oui, alors qu'une analyse rigoureuse impose le doute.",
        "steps": [
            {
                "part": "Partie I : Thèse Immédiate",
                "goal": "Défendre la réponse intuitive ou empirique avec arguments rationnels et exemples.",
            },
            {
                "part": "Partie II : Réfutation / Antithèse Critique",
                "goal": "Montrer les apories, contradictions ou limites conceptuelles de la thèse initiale.",
            },
            {
                "part": "Partie III : Dépassement / Synthèse Conceptuelle",
                "goal": "Redéfinir les termes pour résoudre le paradoxe à un niveau supérieur sans compromis mou.",
            }
        ]
    }

def format_question_card(item: Dict[str, Any]) -> str:
    lines = []
    lines.append(f"### [Niveau {item.get('level', 0)}] {item['q']}")
    if item.get("difficulty"):
        lines.append(f"**Difficulté:** {item['difficulty']}")
    lines.append("")
    lines.append("**Options:**")
    for opt in item.get("options", []):
        marker = "✅ [CORRECT]" if opt.get("correct") else "❌"
        lines.append(f"  {marker} {opt['text']}")
    if item.get("tip"):
        lines.append(f"\n💡 **Repère conceptuel:** {item['tip']}")
    lines.append("")
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Socratic Philosophy & Reasoning Engine")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Search questions
    search_parser = subparsers.add_parser("query", help="Search philosophical dilemma test bank")
    search_parser.add_argument("term", type=str, help="Search term (e.g. 'Kant', 'Liberté', 'Sartre', 'Vérité')")
    search_parser.add_argument("--format", choices=["json", "text"], default="json")

    # List dissertation prompts
    prompt_parser = subparsers.add_parser("prompts", help="List classical dissertation inquiry prompts")

    # Generate dialectic outline
    outline_parser = subparsers.add_parser("outline", help="Generate dialectical analysis outline for a philosophical prompt")
    outline_parser.add_argument("subject", type=str, help="The philosophical subject to outline")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    questions = load_questions()

    if args.command == "query":
        results = search_questions(args.term, questions)
        if args.format == "text":
            if not results:
                print(f"Aucune question trouvée pour '{args.term}'.")
            else:
                for r in results:
                    print(format_question_card(r))
                    print("-" * 50)
        else:
            print(json.dumps({"count": len(results), "term": args.term, "results": results}, indent=2, ensure_ascii=False))

    elif args.command == "prompts":
        prompts = load_prompts()
        print(json.dumps({"count": len(prompts), "prompts": prompts}, indent=2, ensure_ascii=False))

    elif args.command == "outline":
        res = get_dialectical_structure(args.subject)
        print(json.dumps(res, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
