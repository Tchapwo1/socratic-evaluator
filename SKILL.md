---
name: socratic-evaluator
description: Socratic reasoning, philosophical dilemma benchmark, and dialectical essay evaluation skill. Features 85 multi-level philosophical questions across classical notions (Kant, Sartre, Plato, Descartes, Nietzsche, Rousseau, Hannah Arendt) and Hegelian tripartite dialectic outlines (Thèse / Antithèse / Synthèse).
---

# Socratic Reasoning & Philosophical Evaluation Engine

A structured dialectical evaluation skill for AI agents, benchmark testing, and ethical dilemma analysis based on classical French philosophical inquiry.

## Capabilities

1. **Philosophical Benchmark & Dilemma Bank (85 Questions across 10 Levels):**
   - **Level 0 (Repères Conceptuels):** Absolu vs Relatif, En fait vs En droit, En théorie vs En pratique, Idéal vs Réel, Médias vs Fins.
   - **Moral Philosophy:** Kantian deontology vs Aristotelian teleology, Bentham/Mill utilitarianism vs categorical imperatives.
   - **Existentialism & Freedom:** Sartre's bad faith (mauvaise foi), radical freedom, Beauvoir, Camus.
   - **Epistemology & Truth:** Descartes' Cogito, Plato's Allegory of the Cave, Popper's falsifiability.
   - **Political Philosophy:** Hobbes vs Rousseau state of nature, Machiavelli, Arendt on totalitarianism.

2. **Tripartite Dialectical Outlines:**
   - Systematic decomposition of philosophical propositions into:
     - **Thèse (Part I):** Immediate intuitive thesis.
     - **Antithèse (Part II):** Critical refutation and conceptual limits.
     - **Synthèse (Part III):** Transcendental resolution and conceptual re-definition.

---

## Tool Execution

The evaluation script is located at:
`python "D:\Downloads\skills for Smithery.ai\socratic-evaluator\scripts\evaluate.py"`

### 1. Query by Concept or Author
```bash
python "D:\Downloads\skills for Smithery.ai\socratic-evaluator\scripts\evaluate.py" query "Kant" --format text
```

### 2. Generate Dialectical Outline
```bash
python "D:\Downloads\skills for Smithery.ai\socratic-evaluator\scripts\evaluate.py" outline "La liberté consiste-t-elle à faire ce que l'on veut ?"
```

### 3. List Standard Inquiry Prompts
```bash
python "D:\Downloads\skills for Smithery.ai\socratic-evaluator\scripts\evaluate.py" prompts
```
