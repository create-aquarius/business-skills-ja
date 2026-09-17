# Two review skills you can try with pasted text

Early release: two independently installable Agent Skills for evidence-based review. English and Japanese inputs are supported by the instructions; respond in the user's language. No API key, script, or package dependency is included. An AI agent is required to interpret the instructions; its usual access requirements and charges still apply.

These are new skills, not established products. The examples below are synthetic and are not evidence of customer adoption, conversion improvements, or OpenAI program acceptance.

## 1. LP Claim Audit

**Catch the difference between what a landing page promises and what your product evidence actually says.**

[Read the skill](../skills/lp-claim-audit/SKILL.md) · [Download ZIP](https://github.com/create-aquarius/business-skills-ja/raw/refs/heads/main/downloads/lp-claim-audit.zip) · [Example input and output](examples/lp-claim-audit.md)

```bash
npx skills add create-aquarius/business-skills-ja --skill lp-claim-audit -a codex
```

On Windows PowerShell use `npx.cmd`. For Claude Code replace `-a codex` with `-a claude-code`. Alternatively copy the `lp-claim-audit` folder into your agent's skills directory. In a chat interface, paste the full SKILL.md followed by the example input; this is a manual trial, not an installation.

Try: `Use lp-claim-audit to compare this landing page with the product brief. Quote evidence and suggest only supported corrections.`

It distinguishes missing support from a proven contradiction, preserves pilot-study limits, and catches billing conditions lost in copy. It does not verify scientific truth, certify legal compliance, predict conversion, test links, or inspect responsive layouts.

## 2. Feedback to Repro

**Turn "it doesn't work" into an issue a maintainer can investigate, without inventing a reproduction.**

[Read the skill](../skills/feedback-to-repro/SKILL.md) · [Download ZIP](https://github.com/create-aquarius/business-skills-ja/raw/refs/heads/main/downloads/feedback-to-repro.zip) · [Example input and output](examples/feedback-to-repro.md)

```bash
npx skills add create-aquarius/business-skills-ja --skill feedback-to-repro -a codex
```

The same Windows, Claude Code, and manual-copy alternatives apply.

Try: `Use feedback-to-repro to turn these support notes into an English issue draft. Keep reported observations separate from anything not yet tested.`

It preserves useful error details while redacting private values, separates potentially different bugs, and asks focused follow-up questions. It does not submit issues or claim to run a reproduction.

## 日本語で試す

**LPの点検**：「この商品資料とLPを照合して、根拠が足りない説明・矛盾・修正案を出して」。商品資料とLP本文を両方貼ってください。資料がない場合は、裏付け未確認として整理します。

**不具合報告の整理**：「このお客様からの不具合報告を、開発者に渡せるIssueの下書きにして」。報告をそのまま貼り、不明な環境や操作を無理に埋める必要はありません。秘密情報は入力前に取り除いてください。

## What is verified

See [evaluation cases and limitations](evals/review-skills.md). Structural checks and documented author walkthroughs are not a multi-model benchmark. Agent output can vary. If a skill makes up a fact or loses a qualifier, report the sanitized input, agent/model, output excerpt, expected behavior, and skill revision in an [issue](https://github.com/create-aquarius/business-skills-ja/issues/new/choose).

## Open-source scope

Maintainers can rebuild the two ZIPs with `python tools/package_review_skills.py` from the repository root, or check their contents without rewriting with `python tools/package_review_skills.py --check`. Each archive contains only its skill folder's SKILL.md and the repository MIT license. No runtime script is installed with a skill.

MIT, like the rest of this repository. Contributions should improve behavior on a concrete case. These skills do not promise eligibility for a grant or any acceptance outcome.
