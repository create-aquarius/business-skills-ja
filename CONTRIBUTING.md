# Contributing

日本語は下にあります。

## English

Issues and pull requests are welcome.

The most valuable contribution to this project is a report from someone who is
**not** a developer. If a skill did not do what you expected, please open an
issue describing what you tried and what you expected. You do not need to know
how skills work, and you do not need to propose a fix.

### If you want to edit a skill

Every skill is a single `SKILL.md` file under `skills/`, with no dependencies
and no build step. Edit the Markdown and open a pull request.

Please keep these constraints:

- **One task per skill.** No orchestration or multi-step pipelines.
- **Keep the strict rule.** Each skill has one rule preventing the agent from
  inventing content (owners, figures, prices, claims). Do not weaken it.
- **Plain language.** Assume the reader has no software background.
- **Keep it short enough to read in full** before using it.

### Adding a new skill

Please open an issue first describing the task it covers. Skills are added
based on what users actually ask for, not to grow the catalogue.

---

## 日本語

Issue も Pull Request も歓迎します。

このプロジェクトにとっていちばんありがたいのは、
**エンジニアでない方からの「うまく動かなかった」というご報告**です。

「何を貼って、どうなってほしくて、実際はどうなったか」を書いていただければ十分です。
スキルの仕組みを知っている必要はありませんし、
直し方を提案していただく必要もありません。

### スキルを直したい場合

各スキルは `skills/` の下にある `SKILL.md` というファイル1枚だけです。
特別な準備は要りません。書き換えて Pull Request を送ってください。

次の点だけ守っていただけると助かります。

- **1スキル＝1つの仕事**にする（複数の処理を1つにまとめない）
- **「補わないルール」を弱めない** — 各スキルには、AIが担当者・数字・価格・
  効果などを勝手に埋めないためのルールが1つ入っています。ここは外さないでください
- **専門用語を使わない**（読む人はエンジニアではありません）
- **使う前に全部読める長さ**に収める

### 新しいスキルを追加したい場合

先に Issue を立てて、どんな仕事のためのものかを書いてください。
このプロジェクトは数を増やすことを目的にしていないため、
実際に要望のあったものだけを追加しています。
