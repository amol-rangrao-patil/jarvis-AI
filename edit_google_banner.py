from PIL import Image, ImageDraw, ImageFont
import os

try:
    base_banner_path = r"C:\Users\amole\.gemini\antigravity\brain\763077b7-6bbc-4729-885e-6565c76c7291\jarvis_google_banner_1774536629179.png"
    target_banner_path = r"e:\Readme Correction\jarvis-AI\assets\banner.png"
    logo_path = r"e:\Readme Correction\jarvis-AI\assets\logo.png"

    banner = Image.open(base_banner_path).convert("RGBA")
    width, height = banner.size

    overlay = Image.new('RGBA', banner.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)

    bar_height = int(height * 0.18)
    bar_y0 = height - bar_height

    # Sleek frosted white-ish footer / Google style tab
    d.rectangle([0, bar_y0, width, height], fill=(255, 255, 255, 240))

    # Draw top thin border with Google colors
    w_q = width // 4
    thick = max(4, int(height*0.01))
    d.rectangle([0, bar_y0, w_q, bar_y0+thick], fill=(66, 133, 244, 255)) # Blue
    d.rectangle([w_q, bar_y0, w_q*2, bar_y0+thick], fill=(234, 67, 53, 255)) # Red
    d.rectangle([w_q*2, bar_y0, w_q*3, bar_y0+thick], fill=(251, 188, 5, 255)) # Yellow
    d.rectangle([w_q*3, bar_y0, width, bar_y0+thick], fill=(52, 168, 83, 255)) # Green

    banner = Image.alpha_composite(banner, overlay)
    draw = ImageDraw.Draw(banner)

    try:
        font_author1 = ImageFont.truetype("arialbd.ttf", int(bar_height * 0.22))
        font_author2 = ImageFont.truetype("arialbd.ttf", int(bar_height * 0.45))
        # Keep font size reasonable based on width to avoid touching borders
        font_center = ImageFont.truetype("arialbd.ttf", int(width * 0.08)) 
    except IOError:
        font_author1 = font_author2 = font_center = ImageFont.load_default()

    # == 1. CENTER TEXT "Jarvis AI" ==
    center_text = "Jarvis AI"
    bbox_c = draw.textbbox((0,0), center_text, font=font_center)
    tw_c = bbox_c[2] - bbox_c[0]
    th_c = bbox_c[3] - bbox_c[1]
    
    # Give extremely generous spacing from the border
    if tw_c > width * 0.8:
        font_center = ImageFont.truetype("arialbd.ttf", int(width * 0.08 * (width * 0.8 / tw_c)))
        bbox_c = draw.textbbox((0,0), center_text, font=font_center)
        tw_c = bbox_c[2] - bbox_c[0]
        th_c = bbox_c[3] - bbox_c[1]

    cx = (width - tw_c) // 2
    # Ensure it's visually centered in the top space perfectly
    cy = (bar_y0 - th_c) // 2 - int(height * 0.02)

    # Draw thick shadow/glow effect for "Jarvis AI"
    shadow_offset = max(2, int(height * 0.008))
    draw.text((cx + shadow_offset, cy + shadow_offset), center_text, fill=(0, 0, 0, 180), font=font_center)
    # Draw main text "Jarvis AI" in pure white
    draw.text((cx, cy), center_text, fill=(255, 255, 255, 255), font=font_center)

    # == 2. FOOTER LOGO AND TEXT ==
    text1 = "DEVELOPED BY"
    text2 = "AMOL PATIL"

    logo_size = int(bar_height * 0.70)
    logo_x = int(width * 0.05)
    logo_y = bar_y0 + (bar_height - logo_size) // 2

    if os.path.exists(logo_path):
        logo = Image.open(logo_path).convert("RGBA")
        logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
        mask = Image.new("L", (logo_size, logo_size), 0)
        draw_mask = ImageDraw.Draw(mask)
        draw_mask.ellipse((0, 0, logo_size, logo_size), fill=255)
        logo.putalpha(mask)
        banner.paste(logo, (logo_x, logo_y), logo)
        text_start_x = logo_x + logo_size + int(width * 0.03)
    else:
        text_start_x = logo_x

    draw.text((text_start_x, logo_y + int(logo_size*0.05)), text1, fill=(100, 100, 105, 255), font=font_author1)
    bbox1 = draw.textbbox((0,0), text1, font=font_author1)
    h1 = bbox1[3] - bbox1[1]
    draw.text((text_start_x, logo_y + int(logo_size*0.05) + h1 + 5), text2, fill=(66, 133, 244, 255), font=font_author2)

    banner.convert("RGB").save(target_banner_path)
    print("Banner updated with perfectly spaced centered text successfully!")
except Exception as e:
    print(f"Error: {e}")
