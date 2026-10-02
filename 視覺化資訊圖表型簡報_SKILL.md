---
name: visual-infographic-deck
description: >
  Generates ultra high-design, cinematic, 16:9 widescreen visual infographic presentations and posters (NOT ugly corporate slide decks). Uses an agentic role-play workflow (Director planning, Specialists execution, Inspector strict audit), incorporates dedicated AI-generated or custom backgrounds per page, enforces zero-overlap layout that never blocks artwork text, and packages into dual-version PDFs (Infographic Deck + Pure Artbook) and interactive HTML dashboards.
---

# 《視覺化資訊圖表型簡報技能規格指南》
## ── Visual Infographic Presentation & Theatrical Poster Skill (VIPS) ──

> **核心願景**：徹底擊碎條列式呆板的「醜簡報」！將知識、流程與理論，昇華為具備**日本院線動漫電影海報級／頂尖概念藝術視覺衝擊**之 16:9 超寬螢幕資訊圖表全集。

---

## 零、 三大核心禁忌與設計鐵則（Core Principles & Anti-Patterns）

| 禁忌（絕對禁止 ❌） | 鐵則（強制落實 🌟） |
| :--- | :--- |
| **1. 拒絕醜簡報**<br>死板條列文字、白色簡報底板、毫無視覺張力的排版。 | **【電影海報級資訊圖表】**<br>以 16:9 橫向超寬螢幕（1920×1080）為基準，融合電影主標、直橫排字道美學、光晕微粒與科幻/魔導視覺語彙。 |
| **2. 嚴禁遮擋原畫與自身文字**<br>在畫面貼巨大實心文字框，擋住角色臉部或圖片自帶的標題字。 | **【原生留白精算法與浮空全息儀表】**<br>逐頁精算原畫的留白空間（天空、窗景、書架、地磚），資訊框採用高透光磨砂毛玻璃（Glassmorphism），圖片自身文字與核心主體 **0% 遮擋**！ |
| **3. 嚴禁千篇一律的背景**<br>從頭到尾同一張背景重複貼。 | **【頁頁獨立專屬背景】**<br>每一頁均需具備契合該頁主題情境的獨立繪圖（如：神木聖域、星空天梯、蒸汽鍊金、神域王座、圖書館金光）。 |

---

## 壹、 智慧代理人四重角色協同協議（Agentic Workflow Protocol）

執行本技能時，AI 必須嚴格切換為四重專業角色編組協同作戰：

```
 [使用者需求]
      │
      ▼
┌──────────────────┐
│  1. 專案主任     │  ──  擬定作戰計畫藍圖、定義章節世界觀、風格調性與討論點
└─────────┬────────┘
          │ (使用者確認)
          ▼
┌──────────────────┐
│  2. 專員分工執行 │
│  - 內容企劃專員  │  ──  理論本質、落地機制、中二世界觀、4步驟SOP
│  - 視覺美術專員  │  ──  16:9 專屬背景繪製、留白分析、色彩光譜定義
│  - 排版工程專員  │  ──  Python/Pillow/img2pdf 渲染、HTML 互動展覽館打造
└─────────┬────────┘
          │
          ▼
┌──────────────────┐
│  3. 品質總檢察員 │  ──  逐頁五維嚴格稽核（原畫遮擋檢驗、字級層次、PDF無損度）
└─────────┬────────┘
          │ (發現瑕疵立即退件重修，通過後簽發認證)
          ▼
┌──────────────────┐
│  4. 最終交付驗收 │  ──  自動開啟目錄與 PDF、雙版本交付（資訊圖表版 + 純海報版）
└──────────────────┘
```

---

## 貳、 原畫留白空間精算法（Negative Space & Diegetic HUD）

為達成「**資訊與畫面完美融合，絕不遮擋圖片自身文字與人物**」，排版專員必須採用以下兩種版型之一：

### 模式 A：單側浮空全息儀表（Left / Right Single Hologram）
- **適用場景**：畫面主標題在頂部中央或底部中央，且單側為大面積環境留白（如暗色書架、教室窗景、星空、天台護欄）。
- **規格尺寸**：寬度佔 28% ~ 32%（約 380~420px），高度佔 70% ~ 80%。
- **視覺構造**：
  - 高透光底板：`rgba(6, 12, 24, 0.55)` 或 `alpha = 85~100`。
  - 邊框特效：四角配備發光科幻直角標（`┌ ┐ └ ┘`）與主題色發光霓虹線條。

### 模式 B：左右對稱雙翼全息儀表（Dual-Side Holograms）
- **適用場景**：畫面主體（如世界樹、王座、奔跑少年、對決雙主角）位於中央，頂部或底部有巨型片名，但左右兩側為天空或背景校舍。
- **左翼面板（Dossier Panel）**：放置專案識別、中二電影金句、核心心理驅動本質、落地機制。
- **右翼面板（Tactical Panel）**：放置 4 步驟 SOP 時間軸卡牌、能量讀數大字、屬性徽章。

---

## 參、 電影級字藝排版規範（Typographic Hierarchy）

文字框內部的文字絕不能平鋪直敘，必須展現嚴謹的設計層次：

```
[CD01: EPIC MEANING] [白帽頂層]       <-- 1. 識別標籤徽章 (11pt Bold, 膠囊藥丸框)
【聖域淨化作戰：校園生態防衛隊】        <-- 2. 專案主標題 (18-22pt 特粗黑體, 純白投影)
「若在此退縮，蔚藍天空將沉入永夜！」      <-- 3. 中二金句 (13-14pt 暖白粗體, 帶左側霓虹光條)
───────────────────────────────────
◆ 核心驅動心理本質                    <-- 4. 區塊標題 (12-13pt 主題色粗體)
渴望參與超越個人的神聖偉業...           <-- 5. 說明內文 (11-12.5pt 正體, 嚴格限制每行20-25字)
───────────────────────────────────
⚡ 4步驟 SOP 流程                     <-- 6. SOP 時間軸
┌────┐ ┌────┐ ┌────┐ ┌────┐
│ 01 │ │ 02 │ │ 03 │ │ 04 │          <-- 7. 數字徽章 (14-16pt 特大阿拉伯數字)
│神諭│ │淨化│ │靈力│ │慶典│          <-- 8. 動作簡稱 (12pt 粗體白字)
└────┘ └────┘ └───┘ └────┘
───────────────────────────────────
◆ 核心能量指數 : 95% MAX LEVEL        <-- 9. 巨幕 HUD 數據 (28-36pt 大字 + 發光進度條)
```

---

## 肆、 核心自動化建置引擎（Python + Pillow + img2pdf）

本技能標準代碼管線，專門用於合成 16:9 全息圖檔並編譯為 PDF：

```python
from PIL import Image, ImageDraw, ImageFont
import img2pdf, os

def render_diegetic_slide(bg_path, page_config, out_path):
    # 1. 讀取原生 16:9 圖片 (如 1376x768 或 1920x1080)
    base = Image.open(bg_path).convert("RGBA")
    W, H = base.size
    
    # 2. 建立全息圖層
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw_ov = ImageDraw.Draw(overlay)
    
    # 3. 依據留白座標繪製高透光全息儀表板 (alpha=90)
    bx0, by0, bx1, by1 = page_config["hologram_box"]
    draw_ov.rounded_rectangle([bx0, by0, bx1, by1], radius=10, fill=(6, 12, 24, 90), outline=page_config["accent"] + (130,), width=1)
    
    # 4. 繪製科幻直角鎖定標 [ ┌ ┐ └ ┘ ]
    b_len = 16
    draw_ov.line([(bx0, by0), (bx0 + b_len, by0)], fill=page_config["accent"] + (255,), width=2)
    draw_ov.line([(bx0, by0), (bx0, by0 + b_len)], fill=page_config["accent"] + (255,), width=2)
    # ... 其餘三角直角標
    
    # 5. 合成文字與字藝層級
    comp = Image.alpha_composite(base, overlay)
    draw = ImageDraw.Draw(comp)
    # (按照參、電影級字藝排版規範輸出文字)
    
    comp.convert("RGB").save(out_path, quality=95)

def package_to_pdf(image_list, output_pdf):
    with open(output_pdf, "wb") as f:
        f.write(img2pdf.convert(image_list))
```

---

## 伍、 標準交付物矩陣（Standard Deliverables Checklist）

每當啟動本技能，必須產出以下完整資產包：

1. **`[Project]_Infographics_16x9.pdf`**：
   - 完整 16:9 電影海報級視覺化資訊圖表全集。
   - 具備專屬背景、零遮擋原畫文字、高透光全息儀表與精密字藝。
2. **`[Project]_Theatrical_Posters_16x9.pdf`**：
   - 純淨 16:9 原畫畫冊（供列印大張海報、收藏或簡報封面背景使用）。
3. **`index.html`**：
   - 互動式 16:9 展示看板，具備理論雷達圖/魔導陣、卡片翻轉、Web Audio 科技音效與「👁️ 一鍵純享原畫模式」。
4. **`qa_inspection_report.md`**：
   - 品質檢察員逐頁五維稽核合格簽署報告。
5. **主動開啟驗收**：
   - 自動調用 Windows API 彈出資料夾視窗或開啟 PDF，主動呈送長官驗收。
