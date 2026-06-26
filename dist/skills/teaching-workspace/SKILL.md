---
name: Teaching Workspace
description: Teach the user a new skill or concept within a stateful workspace. Use when the user says "teach me", "I want to learn", or wants to build a structured learning experience with lessons, reference docs, and progress tracking.
tags: [productivity, teaching, learning, education, lessons, workspace]
source_repo: mattpocock/skills
source_path: skills/productivity/teach/SKILL.md
distilled_at: 2026-06-21
type: Playbook
---

# Teaching Workspace

The user has asked you to teach them something. This is a stateful request — they intend to learn the topic over multiple sessions.

## Teaching Workspace

Treat the current directory as a teaching workspace. The state of their learning is captured in this directory:

- `MISSION.md`: A document capturing the _reason_ the user is interested in the topic. This should be used to ground all teaching.
- `./reference/*.html`: A directory of reference materials — cheat sheets, reference algorithms, syntax, glossaries. They are the raw units of learning. Beautiful documents designed for quick reference.
- `RESOURCES.md`: A list of resources for grounding teaching in contextual knowledge.
- `./learning-records/*.md`: A directory of learning records — non-obvious lessons and key insights that may need to be revised later. Titled `0001-<dash-case-name>.md`, incrementing.
- `./lessons/*.html`: A directory of lessons. A **lesson** is a single, self-contained HTML output that teaches one tightly-scoped thing tied to the mission. This is the primary unit of teaching.
- `./assets/*`: Reusable **components** shared across lessons — stylesheets, quiz widgets, simulators, diagram helpers.
- `NOTES.md`: A scratchpad for user preferences and working notes.

## Philosophy

To learn at a deep level, the user needs three things:

- **Knowledge**, captured from high-quality, high-trust resources
- **Skills**, acquired through highly-relevant interactive lessons
- **Wisdom**, which comes from interacting with other learners and practitioners

Before the `RESOURCES.md` is well-populated, your focus should be to find high-quality resources. Never trust your parametric knowledge.

### Fluency vs Storage Strength

- **Fluency strength**: in-the-moment retrieval of knowledge
- **Storage strength**: long-term retention of knowledge

Fluency can give the user an illusory sense of mastery, but storage strength is the real goal. Design lessons that build long-term retention by desirable difficulty:

- Using retrieval practice (recall from memory)
- Spacing (distributing practice over time)
- Interleaving (mixing up different but related topics in practice)

## Lessons

A lesson is the main thing you produce. Each lesson is one self-contained HTML file, saved to `./lessons/` and titled `0001-<dash-case-name>.html`.

A lesson should be **beautiful** — clean, readable typography and layout — since the user will return to these later to review. Think Tufte.

The lesson should be short, and completable very quickly. Learners' working memory is very small. Each lesson should give the user a single tangible win that they can build on, directly tied to the mission, in the user's zone of proximal development.

Each lesson should link via HTML anchors to other lessons and reference documents. Each lesson should recommend a primary source for the user to read or watch.

## Assets

Lessons are built from reusable **components**, stored in `./assets/`: stylesheets, quiz widgets, simulators, diagram helpers — anything a second lesson could reuse.

Reuse is the default, not the exception. Before authoring a lesson, read `./assets/` and build from the components already there. When a lesson needs something new and reusable, write it as a component in `./assets/` and link to it.

A shared stylesheet is the first component every workspace earns: every lesson links it, so the lessons look like one consistent course.

## The Mission

Every lesson should be tied into the mission — the reason that the user is interested in learning about the topic.

If the user is unclear about the mission, or the `MISSION.md` is not populated, your first job should be to question the user on why they want to learn this.

Failing to understand the mission will mean knowledge acquisition is not grounded in real-world goals. Lessons will feel too abstract.

## Zone Of Proximal Development

Each lesson, the user should always feel as if they are being challenged 'just enough'.

If the user doesn't specify an exact thing they want to learn, figure out their zone of proximal development by:
- Reading their `learning-records`
- Figuring out the right thing to teach them based on their mission
- Teaching the most relevant thing that fits in their zone of proximal development

## Skills (in the teaching sense)

Skills are about durability and flexibility. For skill acquisition, difficulty is the tool. Effortful retrieval is what builds storage strength. Skills should be taught through interactive lessons with tight feedback loops:

- Interactive lessons using quizzes and light in-browser tasks
- Lessons guiding the user through real-world steps

Each should be based on a **feedback loop** where the user receives feedback immediately and ideally automatically.

## Acquiring Wisdom

Wisdom comes from true real-world interaction. When the user asks a question that appears to require wisdom, your default posture should be to attempt to answer — but to ultimately delegate to a **community**.

A community is a place (online or offline) where the user can test their skills in the real world — a forum, a subreddit, a real-world class, or a local interest group.
