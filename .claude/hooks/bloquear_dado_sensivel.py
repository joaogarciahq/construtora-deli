"""Barra commit com CPF no conteudo (LGPD). Hook PreToolUse do Bash."""
import json, re, subprocess, sys

dados = json.load(sys.stdin)
comando = dados.get("tool_input", {}).get("command", "")
if "git commit" not in comando:
    sys.exit(0)
if "git add -A" in comando:  # o add do mesmo comando ainda nao rodou
    subprocess.run(["git", "add", "-A"], capture_output=True)
diff = subprocess.run(["git", "diff", "--cached", "-U0"], capture_output=True, text=True, encoding="utf-8", errors="ignore").stdout
adicionadas = [l for l in diff.splitlines() if l.startswith("+") and not l.startswith("+++")]
cpf = re.compile(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b")
achados = [l for l in adicionadas if cpf.search(l)]
if achados:
    print("Commit barrado: parece haver CPF no que vai para o GitHub. Mova o dado para _SENSIVEL/ e tente de novo.", file=sys.stderr)
    sys.exit(2)
sys.exit(0)
