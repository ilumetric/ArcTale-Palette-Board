"""Собирает llms-full.txt — все правила сайта одним файлом для нейросетей.

Запускать после каждой правки .md-страниц:  python tools/build_llms.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = 'https://ilumetric.github.io/ArcTale-Palette-Board/'

# Порядок как в меню сайта: (id страницы, заголовок, файл).
PAGES = [
    ('directories', 'Directories', 'directories.md'),
    ('naming', 'Naming Convention', 'naming-convention.md'),
    ('cpd', 'Custom Primitive Data', 'custom-primitive-data.md'),
    ('nanite', 'Nanite', 'nanite.md'),
]

HEADER = f"""# ArcTale: правила арт-контента (полная версия)

> Все правила с {SITE} одним файлом: структура папок, именование ассетов, индексы Custom Primitive Data, что делаем на Nanite. Проект на Unreal Engine.

Файл собран из исходных Markdown-страниц сайта, не редактируйте его вручную. Краткий индекс — {SITE}llms.txt.

Формат: `{{#id}}` после заголовка — якорь, на сайте это `{SITE}#<страница>/<id>`; ссылки вида `#naming/pve-exception` ведут туда же. `::: card` / `::: half` / `::: third` … `:::` — карточка с правилом; `::: step` — карточки цепочкой, связаны линией; `::: yes` / `::: maybe` / `::: no` — вердикт: всегда Nanite / возможно / точно нет; `| Метка` после заголовка — бейдж. В блоке ```tree вложенность задаётся отступом, `— текст` — пояснение, `?` — папка ещё не создана. `- (-) …` — запрещённый вариант.
"""


def main():
    parts = [HEADER]
    for page, title, file in PAGES:
        # Разделы страниц начинаются с ##, поэтому ложатся прямо под # заголовок страницы.
        body = (ROOT / file).read_text(encoding='utf-8').strip()
        parts.append(f'\n---\n\n# {title}\n\nСтраница: {SITE}#{page} · исходник: {SITE}{file}\n\n{body}\n')
    (ROOT / 'llms-full.txt').write_text(''.join(parts), encoding='utf-8', newline='\n')


if __name__ == '__main__':
    main()
