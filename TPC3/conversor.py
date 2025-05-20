import re

def conversor(markdown):
    html = ""
    lines = markdown.splitlines()
    in_list = False

    for line in lines:
        line = line.strip()

        # Cabeçalhos
        if line.startswith("### "):
            html += f"<h3>{line[4:].strip()}</h3>\n"
            continue
        elif line.startswith("## "):
            html += f"<h2>{line[3:].strip()}</h2>\n"
            continue
        elif line.startswith("# "):
            html += f"<h1>{line[2:].strip()}</h1>\n"
            continue

        # Lista numerada
        if re.match(r"\d+\.\s", line):
            if not in_list:
                html += "<ol>\n"
                in_list = True
            item = re.sub(r"\d+\.\s", "", line)
            item = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r'<img src="\2" alt="\1"/>', item)
            item = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', item)
            item = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", item)
            item = re.sub(r"\*(.+?)\*", r"<i>\1</i>", item)
            html += f"<li>{item}</li>\n"
        else:
            if in_list:
                html += "</ol>\n"
                in_list = False

            # Imagem
            line = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r'<img src="\2" alt="\1"/>', line)
            # Link
            line = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', line)
            # Negrito
            line = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", line)
            # Itálico
            line = re.sub(r"\*(.+?)\*", r"<i>\1</i>", line)

            html += line + "\n"

    if in_list:
        html += "</ol>\n"

    return html

# Exemplo direto
if __name__ == "__main__":
    texto = """
# Lista de Compras

Estas são as minhas compras para hoje:

1. Pão
2. Leite
3. Ovos

## Notas

Lembrar de comprar **pão** e *leite*.

Site: [site do supermercado](https://supermercado.pt).

Imagem: ![leite](https://supermercado.pt/leite.png)
"""

    print(conversor(texto))