from PIL import Image, ImageDraw, ImageFont
import os

try:
    target_banner_path = r"e:\Readme Correction\jarvis-AI\assets\banner.png"
    logo_path = r"e:\Readme Correction\jarvis-AI\assets\logo.png"

    # 1. Create a perfectly proportioned wide banner (1200x400) -> Removes "extra space"
    width, height = 1200, 400
    
    # True black background as requested ("black colour image")
    banner = Image.new('RGBA', (width, height), (10, 10, 14, 255)) 
    d = ImageDraw.Draw(banner)

    # Footer parameters
    bar_height = int(height * 0.22)
    bar_y0 = height - bar_height

    # Sleek frosted white-ish footer / Google style tab
    d.rectangle([0, bar_y0, width, height], fill=(255, 255, 255, 255))

    # Draw top thin border with Google colors
    w_q = width // 4
    thick = max(4, int(height*0.015))
    d.rectangle([0, bar_y0, w_q, bar_y0+thick], fill=(66, 133, 244, 255)) # Blue
    d.rectangle([w_q, bar_y0, w_q*2, bar_y0+thick], fill=(234, 67, 53, 255)) # Red
    d.rectangle([w_q*2, bar_y0, w_q*3, bar_y0+thick], fill=(251, 188, 5, 255)) # Yellow
    d.rectangle([w_q*3, bar_y0, width, bar_y0+thick], fill=(52, 168, 83, 255)) # Green

    draw = ImageDraw.Draw(banner)

    # Fonts
    try:
        font_author1 = ImageFont.truetype("arialbd.ttf", int(bar_height * 0.25))
        font_author2 = ImageFont.truetype("arialbd.ttf", int(bar_height * 0.50))
        # Larger font for Jarvis AI
        font_center = ImageFont.truetype("arialbd.ttf", int(height * 0.38)) 
    except IOError:
        font_author1 = font_author2 = font_center = ImageFont.load_default()

    # == CENTER TEXT "Jarvis AI" ==
    center_text = "Jarvis AI"
    bbox_c = draw.textbbox((0,0), center_text, font=font_center)
    tw_c = bbox_c[2] - bbox_c[0]
    th_c = bbox_c[3] - bbox_c[1]

    cx = (width - tw_c) // 2
    # Vertically center exactly within the black area above the footer
    cy = (bar_y0 - th_c) // 2 - int(height * 0.05)

    glow_offset = 3
    draw.text((cx + glow_offset, cy + glow_offset), center_text, fill=(0, 0, 0, 200), font=font_center)
    draw.text((cx, cy), center_text, fill=(255, 255, 255, 255), font=font_center)

    # == FOOTER LOGO AND TEXT ==
    text1 = "DEVELOPED BY"
    text2 = "AMOL PATIL"

    logo_size = int(bar_height * 0.80)
    logo_x = int(width * 0.03)
    logo_y = bar_y0 + (bar_height - logo_size) // 2

    if os.path.exists(logo_path):
        logo = Image.open(logo_path).convert("RGBA")
        logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
        mask = Image.new("L", (logo_size, logo_size), 0)
        draw_mask = ImageDraw.Draw(mask)
        draw_mask.ellipse((0, 0, logo_size, logo_size), fill=255)
        logo.putalpha(mask)
        banner.paste(logo, (logo_x, logo_y), logo)
        text_start_x = logo_x + logo_size + int(width * 0.02)
    else:
        text_start_x = logo_x

    draw.text((text_start_x, logo_y + int(logo_size*0.05)), text1, fill=(100, 100, 105, 255), font=font_author1)
    bbox1 = draw.textbbox((0,0), text1, font=font_author1)
    h1 = bbox1[3] - bbox1[1]
    draw.text((text_start_x, logo_y + int(logo_size*0.05) + h1 + 5), text2, fill=(66, 133, 244, 255), font=font_author2)

    banner.convert("RGB").save(target_banner_path)
    print("Sleek black banner with centered Jarvis AI text updated successfully!")
except Exception as e:
    print(f"Error: {e}")
