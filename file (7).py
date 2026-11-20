import os
import json
from PIL import Image

def slice_and_export_icons(sheet_path, manifest_path, output_dir="NEON_STAGE_ASSETS/Icons"):
    """
    Разрезает sprite sheet на отдельные PNG с альфа-каналом (прозрачностью)
    на основе ASSET_MANIFEST.json.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest = json.load(f)
    
    icons_meta = manifest["components"]["icons"]
    grid = icons_meta["grid"]
    cols, rows = grid["cols"], grid["rows"]
    
    sheet = Image.open(sheet_path).convert("RGBA")
    w, h = sheet.size
    cell_w = w / cols
    cell_h = h / rows
    
    # Конвертация черного фона в прозрачность
    datas = sheet.getdata()
    new_data = []
    for item in datas:
        # Пиксели фона (близкие к чисто черному) делаем прозрачными
        brightness = (item[0] + item[1] + item[2]) / 3
        if brightness < 15:
            new_data.append((0, 0, 0, 0))
        else:
            # Сохраняем цвет и альфа-канал в зависимости от яркости свечения
            alpha = min(255, int(brightness * 2.2))
            new_data.append((item[0], item[1], item[2], alpha))
    sheet.putdata(new_data)
    
    # Нарезка по элементам манифеста
    for name, pos in icons_meta["items"].items():
        c, r = pos["col"], pos["row"]
        x1 = int(c * cell_w)
        y1 = int(r * cell_h)
        x2 = int((c + 1) * cell_w)
        y2 = int((r + 1) * cell_h)
        
        icon_crop = sheet.crop((x1, y1, x2, y2))
        
        # Обрезка пустых краев (autocrop)
        bbox = icon_crop.getbbox()
        if bbox:
            icon_crop = icon_crop.crop(bbox)
        
        target_path = os.path.join(output_dir, f"icon_{name}.png")
        icon_crop.save(target_path, "PNG")
        print(f"Экспортирован ассет: {target_path}")

if __name__ == "__main__":
    slice_and_export_icons("neon_stage_icons_sheet.png", "ASSET_MANIFEST.json")
