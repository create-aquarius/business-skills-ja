# business-skills-ja

**個人起業家・フリーランス・小さなチームのための、AIエージェント用スキル集です。**

エンジニアでない方が、日々の業務でそのまま使えるものだけを集めました。
専門知識は必要ありません。

Claude Code、Codex、ChatGPT、Claude など、
Agent Skills 形式に対応したツールで動きます。

## そもそもスキルとは

AIに「この仕事はこうやって進めてね」と手順を覚えさせておく仕組みです。

一度入れておけば、毎回長い指示を書かなくても、
「このメモ整理して」と言うだけで、決められた形で仕上げてくれるようになります。

プロンプトを毎回書き直す必要がなくなる、と考えていただければ十分です。

## 収録スキル

| スキル | できること |
|---|---|
| `meeting-notes-to-actions` | 打ち合わせメモ・議事録・文字起こしを、決定事項・やること・保留・要確認に整理する |
| `content-repurposing` | 長い記事を、X・Instagram/Facebook・メルマガ向けに書き分ける |
| `feedback-organizer` | アンケートやお客様の声を、機密情報を伏せて原文のまま分類する |
| `inquiry-reply-draft` | 問い合わせへの返信を下書きする。未確定のことは空欄で残す |
| `service-description` | 商品・サービスの説明文を3つの長さで作る。誇大な表現を避ける |
| `competitor-research-notes` | 競合ページを比較できるメモにする。事実と推測を分ける |
| `weekly-report` | バラバラのメモから、結果と次の一手が入った日報・週報を作る |

## 入れかた

Mac・Linuxのターミナルでは、次のコマンドを実行します。

```bash
npx skills add create-aquarius/business-skills-ja --skill meeting-notes-to-actions -a claude-code
```

Windows PowerShellでは、`npx`ではなく`npx.cmd`を使います。

```powershell
npx.cmd skills add create-aquarius/business-skills-ja --skill meeting-notes-to-actions -a claude-code
```

Codex をお使いの場合は、末尾を `-a codex` に変えてください。

ターミナルを使わない場合は、`skills/` の中のフォルダを、
お使いのツールのスキル置き場に手でコピーするだけでも動きます。

インストーラーも初期設定も不要です。中身は `SKILL.md` というテキストファイル1枚だけです。

## 使ってみる

打ち合わせのメモを貼り付けて、こう言うだけです。

```
このメモを整理して
```

走り書きでも、録音の文字起こしでも、そのまま渡して大丈夫です。
整えてから渡す必要はありません。

## このスキル集の方針

実際の業務書類に使うものなので、次のルールを守って作っています。

- **書かれていないことを補わない** — メモに担当者が書かれていなければ「未定」と出します。それらしく埋めてしまうと、議事録として使えなくなるためです
- **1スキル＝1つの仕事** — 複雑な組み合わせや設定ファイルはありません
- **専門用語を使わない** — エンジニア向けの前提知識は不要です
- **全部読める短さ** — 使う前に中身を最後まで読める分量に収めています

## 全部まとめて入れる

1つずつではなく、7本まとめて入れることもできます。

Mac・Linux：

```bash
npx skills add create-aquarius/business-skills-ja -a claude-code
```

Windows PowerShell：

```powershell
npx.cmd skills add create-aquarius/business-skills-ja -a claude-code
```

## 今後について

次にどれを直すか・足すかは、**実際に使った方の声で決めます**。

思いつきで機能を増やすより、
「ここが分かりにくかった」「こう言ったら動かなかった」という報告のほうが、
はるかに役に立ちます。

## うまくいかないときは

**エンジニアでない方からの「動かなかった」という報告が、一番ありがたいです。**

スキルの書き方を知っている必要はありません。
何を試して、何を期待していたかを書いて、Issue を立てていただければ十分です。

## ライセンス

MIT ライセンスです。
