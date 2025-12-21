from prompts.base import PromptHandler

class PromptGeneration(PromptHandler):
    def process(self, context):
        spec = context["spec"]

        context["final_prompt"] = f"""
You are writing a reimagined version of the Mahabharata,
set in a future world governed by intelligent systems.

The story should reflect the idea of Dharma (right action and responsibility)
in a world where decisions are made by AI-driven systems.

Write the story in three Acts:
- ACT I: Setup -The rise of order and hope
- ACT II: Confrontation -Power without restraint
- ACT III: Resolution- Consequences without clear victory

Each Act should contain 2 to 3 short scenes.
Each scene should be 2 to 3 short paragraphs.

Use simple words, clear sentences, and ideas that even a child can understand.
Do not use mythological language and phrases. Keep it realistic.

---

ACT: {spec['act']}
WORLD:
{spec['world_description']}

GOVERNANCE SYSTEMS:
{', '.join(spec['governance'])}

CORE CONFLICTS:
{', '.join(spec['core_conflicts'])}

FACTIONS (inspired by Mahabharata roles):
{', '.join(spec['factions'])}

ADVISOR FIGURE (like Krishna, but non-controlling):
{spec['advisor']} – {spec['advisor_role']}

KEY THEMES (Dharma-focused):
{', '.join(spec['themes'])}

CONSTRAINTS:
{chr(10).join(f"- {c}" for c in spec['constraints'])}

---

Story Guidance:
- Show how power grows through technology.
- Show how good intentions slowly weaken.
- Show how ethical voices are ignored or removed.
- The advisor should guide through questions, not commands.
- There should be **no perfect ending**.
- End with reflection, not victory.

Tone:
Calm, thoughtful, reflective, and serious.
"""
        return context
