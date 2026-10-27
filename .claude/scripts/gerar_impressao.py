"""Gera HTML A4 de impressao a partir de um Markdown simples.
Uso: python3 gerar_impressao.py ENTRADA.md SAIDA.html [--sem-linhas]"""
import re,html,sys
LINHAS='--sem-linhas' not in sys.argv
src=open(sys.argv[1],encoding='utf-8').read()
def inl(t):
    t=html.escape(t)
    t=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',t); t=re.sub(r'\*(.+?)\*',r'<i>\1</i>',t)
    return re.sub(r'`(.+?)`',r'<code>\1</code>',t)
out=[];inlist=False
for l in src.splitlines():
    if l.startswith('- ') and not re.match(r'^\d',l):
        if not inlist: out.append('<ul>');inlist=True
        out.append(f'<li>{inl(l[2:])}</li>');continue
    if inlist: out.append('</ul>');inlist=False
    if l.startswith('# '): out.append(f'<h1>{inl(l[2:])}</h1>')
    elif l.startswith('## '):
        cls=' class="nb"' if l.startswith('## Bloco') or l.startswith('## Fechamento') else ''
        out.append(f'<h2{cls}>{inl(l[3:])}</h2>')
    elif l.startswith('> '): out.append(f'<p class="meta">{inl(l[2:])}</p>')
    elif m:=re.match(r'^(\d+)\. (.*)',l):
        big=False
        out.append(f'<div class="q"><p><span class="n">{m[1]}</span>{inl(m[2])}</p>'+('<div class="ln"></div>'*(5 if big else 3) if LINHAS else '')+'</div>')
    elif l.strip(): out.append(f'<p>{inl(l)}</p>')
if inlist: out.append('</ul>')
css="""@page{size:A4;margin:16mm 16mm 18mm}body{font-family:'DejaVu Sans',Arial,sans-serif;font-size:10.5pt;color:#1a1a1a;line-height:1.4}
h1{font-size:17pt;margin:0 0 4px;border-bottom:2px solid #1a1a1a;padding-bottom:6px}h2{font-size:12pt;margin:16px 0 6px;background:#eee;padding:4px 8px;break-after:avoid}
.meta{color:#555;font-size:9.5pt;margin:2px 0}.q{break-inside:avoid;margin:8px 0 10px}.q p{margin:0 0 2px;display:flex}.n{flex:0 0 28px;font-weight:bold}
.ln{border-bottom:1px solid #bbb;height:20px;margin-left:28px}ul{margin:4px 0;padding-left:20px}li{margin:3px 0}code{font-size:9.5pt}"""
open(sys.argv[2],'w',encoding='utf-8').write(f'<!doctype html><html lang="pt-BR"><meta charset="utf-8"><title>Construtora DELI</title><style>{css}</style><body>{"".join(out)}</body></html>')
