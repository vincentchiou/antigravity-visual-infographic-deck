import os
import sys
from PIL import Image, ImageDraw, ImageFont
import img2pdf

BASE_DIR = r"H:\我的雲端硬碟\Agent\project\測試資訊圖表2"
FONT_BOLD = r"C:\Windows\Fonts\msjhbd.ttc"
FONT_REG = r"C:\Windows\Fonts\msjh.ttc"

# Accurate layout configs tailored to each image's native empty spaces
# Ensuring ZERO overlap with the image's own titles and characters!
PAGES_CONFIG = [
    {
        "id": "cover",
        "bg": "poster_16_9_main.jpg",
        "theme": "#38bdf8",
        "accent": (56, 189, 248),
        # Layout mode: 'left_single' (x: 40 to 450, y: 90 to 680)
        "mode": "left_single",
        "tag": "🎬 劇場版企劃",
        "badge": "16:9 CINEMA VISUAL",
        "project": "【八角行為設計學：國中小遊戲化藍圖】",
        "quote": "「以周昱凱八角奧義為名，徹底解放校園沉睡的無限潛能！」",
        "essence_title": "動機光影黃金配比",
        "essence": "融合白帽賦能與黑帽緊迫驅動，建構 70% 長期熱情 ＋ 30% 突破拖延之黃金教育生態。",
        "mechanism_title": "八大領域全境解鎖",
        "mechanism": "涵蓋世界樹淨化、九階能力天梯、禁忌鍊金創客、使魔領地契約、雙人連攜與不滅聖火！",
        "sop": [
            ("01", "覺醒啟動", "開學導入魔導陣"),
            ("02", "雙向平衡", "兼顧白帽與黑帽"),
            ("03", "全員賦能", "低門檻人人有責"),
            ("04", "典範深化", "回歸自主學習樂趣")
        ],
        "energy_label": "全域魔力指數",
        "energy_val": "100%",
        "energy_sub": "MAX LEVEL",
        "energy_pct": 1.0,
        "hat": "奧義統合 ｜ 全維度覺醒"
    },
    {
        "id": "cd1",
        "bg": "poster_cd1.jpg",
        "theme": "#10b981",
        "accent": (16, 185, 129),
        # Layout mode: 'dual_side' (Left: 40~420, y: 90~650; Right: 950~1330, y: 90~650)
        "mode": "dual_side",
        "tag": "CD1 : EPIC MEANING",
        "badge": "白帽頂層 ｜ 內在動機",
        "project": "【聖域淨化作戰：生態防衛隊】",
        "quote": "「若在此退縮，學園天空將沉入永夜！」",
        "essence_title": "核心驅動心理本質",
        "essence": "渴望參與超越個人的神聖偉業；深信自己是被命運選中的守護使者。",
        "mechanism_title": "國中小學落地機制",
        "mechanism": "校門口設立「全校結界靈力計」，堆肥每達標推進進度條享慶典。",
        "sop": [
            ("01", "神諭受命", "宣布世界樹受蝕危機"),
            ("02", "淨化分隊", "外掃區整編巡防哨所"),
            ("03", "靈力注滿", "堆肥推進世界進度條"),
            ("04", "聖域慶典", "解鎖全校自選音樂餐")
        ],
        "energy_label": "使命召喚力",
        "energy_val": "95%",
        "energy_sub": "ULTRA HIGH",
        "energy_pct": 0.95,
        "hat": "白帽頂層 ｜ 光之陣營"
    },
    {
        "id": "cd2",
        "bg": "poster_cd2.jpg",
        "theme": "#38bdf8",
        "accent": (56, 189, 248),
        # Layout mode: 'left_single' (x: 40 to 480, y: 170 to 680) - blends into skill tree!
        "mode": "left_single",
        "tag": "CD2 : ACCOMPLISHMENT",
        "badge": "白帽左側 ｜ 外在進階",
        "project": "【百鍊封神錄：九階天梯榜】",
        "quote": "「真正的強者，踏著自己的足跡封神！」",
        "essence_title": "核心驅動心理本質",
        "essence": "渴望克服挑戰、看見自我技能突破並解鎖里程碑印記之成就心流。",
        "mechanism_title": "國中小學落地機制",
        "mechanism": "九階印記制度（黑鐵→秘銀→覺醒）；作業訂正與小考皆可蓋火漆章挑戰魔王題。",
        "sop": [
            ("01", "授予卷軸", "發放學科修煉地圖"),
            ("02", "破關印記", "過關點星印不限重測"),
            ("03", "挑戰魔王", "選填魔王題解鎖徽章"),
            ("04", "階位登頂", "全員晉升秘銀共享榮耀")
        ],
        "energy_label": "成就達成感",
        "energy_val": "92%",
        "energy_sub": "HIGH MASTERY",
        "energy_pct": 0.92,
        "hat": "白帽左側 ｜ 階位晉升"
    },
    {
        "id": "cd3",
        "bg": "poster_cd3.jpg",
        "theme": "#f97316",
        "accent": (249, 115, 22),
        # Layout mode: 'dual_side' (Left: 40~400, y: 200~680; Right: 970~1330, y: 200~680)
        "mode": "dual_side",
        "tag": "CD3 : CREATIVITY",
        "badge": "白帽右側 ｜ 內在創造",
        "project": "【禁忌工坊：機關自力發明週】",
        "quote": "「這裡沒有標準答案！由你改寫真理！」",
        "essence_title": "核心驅動心理本質",
        "essence": "賦予無限組合畫布，在自由嘗試、即時物理反饋中獲得創造的純粹欣喜與掌控感。",
        "mechanism_title": "國中小學落地機制",
        "mechanism": "模組零件盲選＋前方試跑台；失敗獲解析數據，隨時返座改裝升級。",
        "sop": [
            ("01", "禁忌配方", "多元零件不設標準解"),
            ("02", "狂想組裝", "激盪打造動能機關"),
            ("03", "擂台試射", "即刻測試物理反饋"),
            ("04", "迭代優化", "無限重試進化傳奇")
        ],
        "energy_label": "創意賦能力",
        "energy_val": "98%",
        "energy_sub": "PEAK CREATIVE",
        "energy_pct": 0.98,
        "hat": "白帽右側 ｜ 創世靈光"
    },
    {
        "id": "cd4",
        "bg": "poster_cd4.jpg",
        "theme": "#a855f7",
        "accent": (168, 85, 247),
        # Layout mode: 'dual_side' (Left: 40~420, y: 170~680; Right: 950~1330, y: 170~680)
        "mode": "dual_side",
        "tag": "CD4 : OWNERSHIP",
        "badge": "偏左腦 ｜ 價值累積",
        "project": "【靈魂使魔殿堂：守護獸魔導書】",
        "quote": "「刻上真名之刻，此地即為神聖領域！」",
        "essence_title": "核心驅動心理本質",
        "essence": "當人們客製並完全擁有某物，便會自然產生強烈的守護與自我增值慾望。",
        "mechanism_title": "國中小學落地機制",
        "mechanism": "開學領養使魔蛋；札記獲以太晶石，換領地銘牌、配飾與班級獸進化。",
        "sop": [
            ("01", "靈魂契約", "繪製使魔賦予真名"),
            ("02", "領地開闢", "劃定個人置物櫃神域"),
            ("03", "晶石餵養", "整潔作業累積點數"),
            ("04", "守護覺醒", "班級使魔最終姿態")
        ],
        "energy_label": "領地支配力",
        "energy_val": "88%",
        "energy_sub": "SOVEREIGN",
        "energy_pct": 0.88,
        "hat": "左腦邏輯 ｜ 領地構築"
    },
    {
        "id": "cd5",
        "bg": "poster_cd5.jpg",
        "theme": "#06b6d4",
        "accent": (6, 182, 212),
        # Layout mode: 'dual_side' (Left: 40~420, y: 80~580; Right: 950~1330, y: 80~580)
        "mode": "dual_side",
        "tag": "CD5 : SOCIAL INFLUENCE",
        "badge": "偏右腦 ｜ 社交羈絆",
        "project": "【公會共鬥討伐戰：雙人連攜結界】",
        "quote": "「後背交給我！全隊齒輪由我轉動！」",
        "essence_title": "核心驅動心理本質",
        "essence": "渴望同儕接納、情感連結與團隊認同；師徒傳承帶來深刻利他愉悅感。",
        "mechanism_title": "國中小學落地機制",
        "mechanism": "互補組隊共鬥，弱項同學進步觸發隊伍暴擊加分；學長姐任引路賢者指導。",
        "sop": [
            ("01", "公會結盟", "依專長互補配對組隊"),
            ("02", "誓言立約", "簽署協議不棄隊友"),
            ("03", "連攜暴擊", "同伴突破全員加成"),
            ("04", "賢者殿堂", "輔導學伴名列英靈碑")
        ],
        "energy_label": "同盟共鳴力",
        "energy_val": "94%",
        "energy_sub": "STRONG BOND",
        "energy_pct": 0.94,
        "hat": "右腦內在 ｜ 靈魂連攜"
    },
    {
        "id": "cd6",
        "bg": "poster_cd6.jpg",
        "theme": "#f59e0b",
        "accent": (245, 158, 11),
        # Layout mode: 'left_single' (x: 40 to 450, y: 190 to 720) - dark library bookshelves!
        "mode": "left_single",
        "tag": "CD6 : SCARCITY",
        "badge": "黑帽底層 ｜ 稀缺渴望",
        "project": "【深淵禁書區：午休『皇家御座』】",
        "quote": "「唯在月食之瞬，真理之門方敞開裂隙！」",
        "essence_title": "核心驅動心理本質",
        "essence": "得不到的永遠最珍貴；越是限量、越需付出等待，價值感越被成倍放大。",
        "mechanism_title": "國中小學落地機制",
        "mechanism": "全勤閱讀心得者方可抽金色通行證；門口設立神秘倒數沙漏維持期待感。",
        "sop": [
            ("01", "結界封印", "劃定特別閱覽特區"),
            ("02", "鑄造金券", "每週限量十張印信"),
            ("03", "試煉爭奪", "借閱心得達標抽籤"),
            ("04", "尊榮入閣", "週三午休專屬御座")
        ],
        "energy_label": "飢餓渴求度",
        "energy_val": "86%",
        "energy_sub": "SCARCE TIER",
        "energy_pct": 0.86,
        "hat": "黑帽左側 ｜ 稀缺之門"
    },
    {
        "id": "cd7",
        "bg": "poster_cd7.jpg",
        "theme": "#ec4899",
        "accent": (236, 72, 153),
        # Layout mode: 'dual_side' (Left: 40~400, y: 180~680; Right: 960~1330, y: 180~680)
        "mode": "dual_side",
        "tag": "CD7 : UNPREDICTABILITY",
        "badge": "黑帽底層 ｜ 未知好奇",
        "project": "【校園異聞錄：每週盲盒任務】",
        "quote": "「走廊下個轉角，是恩賜還是試煉！」",
        "essence_title": "核心驅動心理本質",
        "essence": "對未知的強烈好奇、開盲盒的腎上腺素飆升；隨機獎勵機制的強效牽引。",
        "mechanism_title": "國中小學落地機制",
        "mechanism": "角落神秘信封或QR碼，觸發向師長問答或尋找彩蛋，隨機掉落神秘道具卡。",
        "sop": [
            ("01", "隨機布陣", "晨會投放次元代碼"),
            ("02", "觸發奇遇", "探索解開盲盒謎題"),
            ("03", "轉動輪盤", "回報抽取命運刮卡"),
            ("04", "驚喜掉落", "獲免排隊餐券稱號")
        ],
        "energy_label": "驚喜心跳度",
        "energy_val": "90%",
        "energy_sub": "RNG FACTOR",
        "energy_pct": 0.90,
        "hat": "黑帽右側 ｜ 混沌輪盤"
    },
    {
        "id": "cd8",
        "bg": "poster_cd8.jpg",
        "theme": "#ef4444",
        "accent": (239, 68, 68),
        # Layout mode: 'left_single' (x: 40 to 450, y: 110 to 590) - open classroom window area!
        "mode": "left_single",
        "tag": "CD8 : LOSS & AVOIDANCE",
        "badge": "黑帽底層 ｜ 虧損避免",
        "project": "【不滅聖火：全班連勝防禦陣線】",
        "quote": "「魔力核心即將冷卻！阻斷虛無深淵！」",
        "essence_title": "核心驅動心理本質",
        "essence": "痛恨既得成果付之一炬（損失厭惡）；群體責任感化為強大自律動能。",
        "mechanism_title": "國中小學落地機制",
        "mechanism": "連續不缺交天數階梯；內建每週「鳳凰替身符」防範一人失誤被同儕霸凌。",
        "sop": [
            ("01", "點燃聖火", "黑板每日記錄連勝"),
            ("02", "備妥替身", "打掃優良兌換救贖符"),
            ("03", "階梯解鎖", "連勝七天解鎖音樂"),
            ("04", "狂歡慶祝", "滿廿一天辦同樂會")
        ],
        "energy_label": "防禦危機感",
        "energy_val": "89%",
        "energy_sub": "CRITICAL SHIELD",
        "energy_pct": 0.89,
        "hat": "黑帽底層 ｜ 緊急結界"
    }
]

def wrap_text(text, max_chars=20):
    lines = []
    for i in range(0, len(text), max_chars):
        lines.append(text[i:i+max_chars])
    return lines

def render_diegetic_integrated_slides():
    print("Executing DIEGETIC INTEGRATION: Zero overlap with artwork text, floating sci-fi hologram widgets...")

    # Load high-precision fonts
    font_h2 = ImageFont.truetype(FONT_BOLD, 17)
    font_quote = ImageFont.truetype(FONT_BOLD, 12.5)
    font_label = ImageFont.truetype(FONT_BOLD, 12)
    font_body = ImageFont.truetype(FONT_REG, 11)
    
    font_sop_num = ImageFont.truetype(FONT_BOLD, 14)
    font_sop_title = ImageFont.truetype(FONT_BOLD, 12)
    font_sop_sub = ImageFont.truetype(FONT_REG, 10.5)

    font_badge = ImageFont.truetype(FONT_BOLD, 11)
    font_credit = ImageFont.truetype(FONT_REG, 9.5)
    
    font_gauge_val = ImageFont.truetype(FONT_BOLD, 28)
    font_gauge_sub = ImageFont.truetype(FONT_BOLD, 9.5)

    generated_slide_paths = []

    for idx, page in enumerate(PAGES_CONFIG):
        bg_path = os.path.join(BASE_DIR, page["bg"])
        if not os.path.exists(bg_path):
            continue

        # Target resolution: 1376 x 768 native
        base_img = Image.open(bg_path).convert("RGBA")
        W, H = base_img.size

        overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        draw_ov = ImageDraw.Draw(overlay)

        # Helper to draw a sci-fi hologram panel with glowing corner brackets
        def draw_hologram_panel(bx0, by0, bx1, by1):
            # Extremely transparent glass fill (alpha=85)
            draw_ov.rounded_rectangle([bx0, by0, bx1, by1], radius=10, fill=(6, 12, 24, 90), outline=page["accent"] + (130,), width=1)
            # Top glowing accent line
            draw_ov.rounded_rectangle([bx0, by0, bx1, by0 + 3], radius=1, fill=page["accent"] + (220,))
            # Glowing sci-fi corner brackets
            bracket_len = 16
            draw_ov.line([(bx0, by0), (bx0 + bracket_len, by0)], fill=page["accent"] + (255,), width=2)
            draw_ov.line([(bx0, by0), (bx0, by0 + bracket_len)], fill=page["accent"] + (255,), width=2)
            draw_ov.line([(bx1, by0), (bx1 - bracket_len, by0)], fill=page["accent"] + (255,), width=2)
            draw_ov.line([(bx1, by0), (bx1, by0 + bracket_len)], fill=page["accent"] + (255,), width=2)
            draw_ov.line([(bx0, by1), (bx0 + bracket_len, by1)], fill=page["accent"] + (255,), width=2)
            draw_ov.line([(bx0, by1), (bx0, by1 - bracket_len)], fill=page["accent"] + (255,), width=2)
            draw_ov.line([(bx1, by1), (bx1 - bracket_len, by1)], fill=page["accent"] + (255,), width=2)
            draw_ov.line([(bx1, by1), (bx1, by1 - bracket_len)], fill=page["accent"] + (255,), width=2)

        mode = page["mode"]

        if mode == "dual_side":
            # DUAL-SIDE HOLOGRAPHIC PANELS (Left + Right)
            # Leaving entire center, top title, and bottom title completely 100% UNTOUCHED!
            left_w = 370
            right_w = 360
            top_y = 110 if page["id"] == "cd5" else 170
            box_h = 490

            # Draw Left Panel
            lx0, ly0, lx1, ly1 = 40, top_y, 40 + left_w, top_y + box_h
            draw_hologram_panel(lx0, ly0, lx1, ly1)

            # Draw Right Panel
            rx0, ry0, rx1, ry1 = W - 40 - right_w, top_y, W - 40, top_y + box_h
            draw_hologram_panel(rx0, ry0, rx1, ry1)

            comp = Image.alpha_composite(base_img, overlay)
            draw = ImageDraw.Draw(comp)

            # --- POPULATE LEFT PANEL (Mission, Quote, Essence, Mechanism) ---
            px = lx0 + 18
            py = ly0 + 16

            # Badges
            draw.rounded_rectangle([px, py, px + 175, py + 22], radius=4, fill=(15, 23, 42, 220), outline=page["accent"], width=1)
            draw.text((px + 6, py + 3), page["tag"], font=font_badge, fill=page["accent"])
            
            draw.rounded_rectangle([px + 185, py, lx1 - 18, py + 22], radius=4, fill=page["accent"])
            draw.text((px + 192, py + 3), page["badge"], font=font_badge, fill=(10, 15, 29))

            py += 32
            # Project Title
            draw.text((px, py), page["project"], font=font_h2, fill=(255, 255, 255))
            
            py += 28
            # Chunibyo Quote
            quote_h = 42
            draw.rounded_rectangle([px, py, lx1 - 18, py + quote_h], radius=4, fill=(0, 0, 0, 130), outline=(page["accent"][0], page["accent"][1], page["accent"][2], 120), width=1)
            draw.rectangle([px, py, px + 3, py + quote_h], fill=page["accent"])
            draw.text((px + 8, py + 12), page["quote"], font=font_quote, fill=(248, 250, 252))

            py += quote_h + 16
            # Essence Box
            draw.rounded_rectangle([px, py, lx1 - 18, py + 105], radius=6, fill=(15, 23, 42, 160), outline=(255, 255, 255, 25), width=1)
            draw.text((px + 10, py + 8), f"◆ {page['essence_title']}", font=font_label, fill=page["accent"])
            for li, line in enumerate(wrap_text(page["essence"], max_chars=18)[:4]):
                draw.text((px + 10, py + 30 + li * 17), line, font=font_body, fill=(226, 232, 240))

            py += 115
            # Mechanism Box
            draw.rounded_rectangle([px, py, lx1 - 18, py + 115], radius=6, fill=(15, 23, 42, 160), outline=(255, 255, 255, 25), width=1)
            draw.text((px + 10, py + 8), f"◆ {page['mechanism_title']}", font=font_label, fill=(245, 158, 11))
            for li, line in enumerate(wrap_text(page["mechanism"], max_chars=18)[:4]):
                draw.text((px + 10, py + 30 + li * 17), line, font=font_body, fill=(226, 232, 240))

            # --- POPULATE RIGHT PANEL (SOP 4-Steps, Energy Gauge, Credit) ---
            qx = rx0 + 18
            qy = ry0 + 16

            draw.text((qx, qy), "⚡ 落地執行 SOP 四步驟", font=font_label, fill=(251, 191, 36))
            qy += 26

            # 4 SOP steps vertically stacked
            sop_h = 58
            for s_idx, (num_str, step_name, sub_1) in enumerate(page["sop"]):
                sy = qy + s_idx * (sop_h + 8)
                draw.rounded_rectangle([qx, sy, rx1 - 18, sy + sop_h], radius=6, fill=(15, 23, 42, 170), outline=(255, 255, 255, 30), width=1)
                draw.rectangle([qx, sy, qx + 3, sy + sop_h], fill=page["accent"])
                
                # Step Numeral + Title
                draw.text((qx + 10, sy + 10), f"[{num_str}] {step_name}", font=font_sop_title, fill=(255, 255, 255))
                draw.text((qx + 10, sy + 32), sub_1, font=font_sop_sub, fill=(203, 213, 225))

            qy += 4 * (sop_h + 8) + 10

            # Energy gauge
            draw.text((qx, qy), f"◆ {page['energy_label']}", font=font_label, fill=(148, 163, 184))
            qy += 20
            draw.text((qx, qy), page["energy_val"], font=font_gauge_val, fill=page["accent"])
            draw.text((qx + 85, qy + 8), page["energy_sub"], font=font_gauge_sub, fill=page["accent"])

            qy += 36
            # Progress bar
            bar_w = (rx1 - 18 - qx)
            draw.rounded_rectangle([qx, qy, qx + bar_w, qy + 6], radius=3, fill=(30, 41, 59, 240))
            fill_w = int(bar_w * page["energy_pct"])
            draw.rounded_rectangle([qx, qy, qx + fill_w, qy + 6], radius=3, fill=page["accent"])

            qy += 18
            draw.text((qx, qy), page["hat"], font=font_credit, fill=page["accent"])

        else:
            # LEFT-SINGLE HOLOGRAPHIC PANEL (x: 40 to 450, y: 100 to 710)
            # Perfect for Cover, CD2 (blends with skill tree), CD6 (dark bookshelves), CD8 (left classroom)
            box_w = 410
            top_y = 75 if page["id"] == "cover" else 135
            box_h = 560

            lx0, ly0, lx1, ly1 = 40, top_y, 40 + box_w, top_y + box_h
            draw_hologram_panel(lx0, ly0, lx1, ly1)

            comp = Image.alpha_composite(base_img, overlay)
            draw = ImageDraw.Draw(comp)

            px = lx0 + 18
            py = ly0 + 14

            # Badges
            draw.rounded_rectangle([px, py, px + 175, py + 22], radius=4, fill=(15, 23, 42, 220), outline=page["accent"], width=1)
            draw.text((px + 6, py + 3), page["tag"], font=font_badge, fill=page["accent"])
            
            draw.rounded_rectangle([px + 185, py, lx1 - 18, py + 22], radius=4, fill=page["accent"])
            draw.text((px + 192, py + 3), page["badge"], font=font_badge, fill=(10, 15, 29))

            py += 30
            # Project Title
            draw.text((px, py), page["project"], font=font_h2, fill=(255, 255, 255))
            
            py += 26
            # Chunibyo Quote
            quote_h = 40
            draw.rounded_rectangle([px, py, lx1 - 18, py + quote_h], radius=4, fill=(0, 0, 0, 130), outline=(page["accent"][0], page["accent"][1], page["accent"][2], 120), width=1)
            draw.rectangle([px, py, px + 3, py + quote_h], fill=page["accent"])
            draw.text((px + 8, py + 11), page["quote"], font=font_quote, fill=(248, 250, 252))

            py += quote_h + 12
            # Essence & Mechanism in 1 compact chip
            draw.rounded_rectangle([px, py, lx1 - 18, py + 125], radius=6, fill=(15, 23, 42, 160), outline=(255, 255, 255, 25), width=1)
            draw.text((px + 10, py + 6), f"◆ {page['essence_title']}", font=font_label, fill=page["accent"])
            for li, line in enumerate(wrap_text(page["essence"], max_chars=20)[:2]):
                draw.text((px + 10, py + 26 + li * 16), line, font=font_body, fill=(226, 232, 240))

            draw.text((px + 10, py + 64), f"◆ {page['mechanism_title']}", font=font_label, fill=(245, 158, 11))
            for li, line in enumerate(wrap_text(page["mechanism"], max_chars=20)[:3]):
                draw.text((px + 10, py + 84 + li * 16), line, font=font_body, fill=(226, 232, 240))

            py += 135
            # SOP 4-Steps (horizontal 2x2 grid or compact vertical)
            draw.text((px, py), "⚡ 4步驟 SOP 流程", font=font_label, fill=(251, 191, 36))
            py += 22

            sop_w = (lx1 - 18 - px - 8) // 2
            sop_h = 46
            for s_idx, (num_str, step_name, sub_1) in enumerate(page["sop"]):
                col_i = s_idx % 2
                row_i = s_idx // 2
                sx = px + col_i * (sop_w + 8)
                sy = py + row_i * (sop_h + 6)
                
                draw.rounded_rectangle([sx, sy, sx + sop_w, sy + sop_h], radius=4, fill=(15, 23, 42, 180), outline=(255, 255, 255, 30), width=1)
                draw.rectangle([sx, sy, sx + 3, sy + sop_h], fill=page["accent"])
                draw.text((sx + 6, sy + 6), f"[{num_str}] {step_name}", font=font_sop_title, fill=(255, 255, 255))
                draw.text((sx + 6, sy + 25), sub_1, font=font_sop_sub, fill=(203, 213, 225))

            py += 2 * (sop_h + 6) + 12

            # Energy Gauge row
            draw.text((px, py), f"◆ {page['energy_label']} : {page['energy_val']}", font=font_label, fill=page["accent"])
            py += 18
            bar_w = (lx1 - 18 - px)
            draw.rounded_rectangle([px, py, px + bar_w, py + 6], radius=3, fill=(30, 41, 59, 240))
            fill_w = int(bar_w * page["energy_pct"])
            draw.rounded_rectangle([px, py, px + fill_w, py + 6], radius=3, fill=page["accent"])

            py += 16
            draw.text((px, py), f"{page['hat']} ｜ 16:9 DIEGETIC SPEC", font=font_credit, fill=(100, 116, 139))


        # Save Slide
        out_slide_name = f"slide_{idx:02d}_{page['id']}.jpg"
        out_slide_path = os.path.join(BASE_DIR, out_slide_name)
        comp.convert("RGB").save(out_slide_path, quality=95)
        print(f"Diegetic slide generated: {out_slide_name}")
        generated_slide_paths.append(out_slide_path)

    # Re-compile PDFs
    print("\nRe-compiling 16:9 PDFs with zero artwork text overlap...")
    pdf_deck_path = os.path.join(BASE_DIR, "八角神域_校園遊戲化_16x9電影海報資訊圖表全集.pdf")
    with open(pdf_deck_path, "wb") as f:
        f.write(img2pdf.convert(generated_slide_paths))
    print(f"Updated Deck PDF: {pdf_deck_path} ({os.path.getsize(pdf_deck_path)} bytes)")

    return generated_slide_paths

if __name__ == "__main__":
    render_diegetic_integrated_slides()
