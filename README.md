# business-skills-ja

**Agent Skills for Japanese business practitioners — solo founders, freelancers, and small teams.**

A small, deliberately beginner-friendly set of skills for everyday business work,
written in Japanese, for people who are not developers.

Works with Claude Code, Codex, ChatGPT, Claude, and other agents that read the
Agent Skills format.

日本語の説明は [README.ja.md](./README.ja.md) にあります。

## Why this exists

Agent Skills adoption is concentrated among English-speaking developers.

Large community collections now ship hundreds or thousands of skills, which is
excellent for engineers who already know what a skill is. But that scale creates
a different problem for everyone else: a business practitioner opening a
1,000-skill catalogue has no idea which one to install first, and every skill
they find assumes English and a developer's workflow.

In Japan this gap is especially wide. Solo founders, freelancers, and small
agencies are adopting AI tools quickly, but almost nothing exists between
"chat with an assistant" and "install a developer toolchain."

This project is the missing first step: a handful of skills, in Japanese,
covering work that people actually do every day. It is intentionally small and
intentionally basic. The goal is that someone installs one skill, uses it on a
real task within five minutes, and understands what a skill is by having used one.

Maintained by someone who runs this kind of business daily, not as an outside
observer.

## Skills

| Skill | What it does |
|---|---|
| `meeting-notes-to-actions` | Turns meeting notes or transcripts into decisions, action items, and open questions |
| `content-repurposing` | Rewrites a long article into posts for X, Instagram/Facebook, and a newsletter |
| `feedback-organizer` | Sorts survey responses and customer feedback, preserving the wording while redacting sensitive values |
| `inquiry-reply-draft` | Drafts a reply to an inbound enquiry, leaving anything unconfirmed blank |
| `service-description` | Writes product descriptions at three lengths, avoiding regulated advertising claims |
| `competitor-research-notes` | Turns competitor pages into comparable notes, separating fact from inference |
| `weekly-report` | Turns scattered notes into a report with results, setbacks, and next steps |

## Install

macOS / Linux:

```bash
npx skills add create-aquarius/business-skills-ja --skill meeting-notes-to-actions -a claude-code
```

Windows PowerShell:

```powershell
npx.cmd skills add create-aquarius/business-skills-ja --skill meeting-notes-to-actions -a claude-code
```

Replace `-a claude-code` with `-a codex` for Codex.

You can also copy any skill folder from `skills/` into your agent's skills
directory by hand. Every skill is a single `SKILL.md` file with no dependencies,
no build step, and no install script.

## Design principles

These skills are used for real business documents, so they follow a few strict rules:

- **Never invent what is not there.** If a meeting note does not name an owner,
  the output says "未定" (undecided) rather than guessing. Documents that quietly
  fill in plausible details are worse than useless as a record.
- **One task per skill.** No orchestration, no multi-step pipelines, no
  configuration files.
- **Plain language.** No jargon that assumes a software background.
- **Readable in full.** Every skill is short enough to read start to finish
  before using it.

## Roadmap

v0.1 ships the seven skills above. The next version will be driven by what
actually breaks for real users rather than by a feature list, so the priority
is collecting feedback from non-developers using these on real work.

Known areas to improve:

- Wording of the trigger phrases in each `description`, which decides whether a
  skill activates when a user asks in their own words
- Verification against Codex in addition to Claude Code

## Contributing

Issues and pull requests are welcome, in Japanese or English.

If you are a business practitioner rather than a developer and something did not
work, that is the most useful bug report this project can receive. Please open an
issue describing what you tried and what you expected — you do not need to know
how to write a skill.

## License

MIT — see [LICENSE](./LICENSE).
