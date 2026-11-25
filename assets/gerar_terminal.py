"""Gera assets/terminal.svg: um terminal que digita comandos em loop (CSS animado, sem JS).

Uso: python3 assets/gerar_terminal.py assets/terminal.svg  — edite a lista SESSAO para mudar o texto."""
import sys
from xml.sax.saxutils import escape

SAIDA = sys.argv[1]

CICLO = 14.0          # segundos por loop
TECLA = 0.075         # segundos por caractere digitado
PAUSA_SAIDA = 0.35    # entre terminar o comando e mostrar a saída
PAUSA_PROXIMO = 0.9   # entre a saída e o próximo comando
FIM = 0.965           # fração do ciclo em que tudo some para recomeçar

FONTE = 15
CW = 9.0              # largura de cada caractere (forçada com textLength)
LINHA = 24
X0, Y0 = 24, 64       # primeira linha de texto
LARGURA = 640

# (comando, saída, classe da saída)
SESSAO = [
    ("whoami", "lucas · desenvolvedor backend", "out"),
    ("cat stack.txt", "java  spring-boot  postgresql  docker", "out"),
    ("./mvnw verify", "[INFO] BUILD SUCCESS", "ok"),
    ("echo $STATUS", "em busca de estágio ou vaga júnior", "status"),
]
PROMPT = "❯ "

linhas_total = len(SESSAO) * 2 + 1
ALTURA = Y0 + (linhas_total - 1) * LINHA + 30


def pct(t):
    return f"{t / CICLO * 100:.3f}%"


css, corpo = [], []
t = 0.8
y = Y0
for i, (cmd, saida, classe) in enumerate(SESSAO):
    inicio, dur = t, len(cmd) * TECLA
    fim_digitacao = inicio + dur
    largura_cmd = len(cmd) * CW
    x_cmd = X0 + len(PROMPT) * CW

    # Comando: um retângulo de recorte cresce um caractere por vez.
    css.append(
        f"@keyframes c{i}{{0%,{pct(inicio)}{{width:0;animation-timing-function:steps({len(cmd)},end)}}"
        f"{pct(fim_digitacao)},{FIM * 100:.3f}%{{width:{largura_cmd:.1f}px}}100%{{width:0}}}}"
        f"#r{i}{{animation:c{i} {CICLO}s infinite}}"
    )
    corpo.append(f'<clipPath id="k{i}"><rect id="r{i}" x="{x_cmd}" y="{y - FONTE}" width="{largura_cmd:.1f}" height="{LINHA}"/></clipPath>')
    corpo.append(f'<g class="lin" id="p{i}"><text x="{X0}" y="{y}" class="prompt">{escape(PROMPT.strip())}</text>')
    corpo.append(
        f'<text x="{x_cmd}" y="{y}" class="cmd" clip-path="url(#k{i})" textLength="{largura_cmd:.1f}" '
        f'lengthAdjust="spacing">{escape(cmd)}</text></g>'
    )
    # O prompt aparece um instante antes de começar a digitar.
    css.append(
        f"@keyframes q{i}{{0%,{pct(max(inicio - 0.25, 0))}{{opacity:0}}{pct(max(inicio - 0.249, 0.001))},{FIM * 100:.3f}%{{opacity:1}}100%{{opacity:0}}}}"
        f"#p{i}{{animation:q{i} {CICLO}s infinite}}"
    )

    # Saída: aparece de uma vez, como num terminal de verdade.
    y += LINHA
    aparece = fim_digitacao + PAUSA_SAIDA
    css.append(
        f"@keyframes o{i}{{0%,{pct(aparece)}{{opacity:0}}{pct(aparece + 0.001)},{FIM * 100:.3f}%{{opacity:1}}100%{{opacity:0}}}}"
        f"#s{i}{{animation:o{i} {CICLO}s infinite}}"
    )
    corpo.append(
        f'<text id="s{i}" x="{X0 + len(PROMPT) * CW}" y="{y}" class="{classe}" '
        f'textLength="{len(saida) * CW:.1f}" lengthAdjust="spacing">{escape(saida)}</text>'
    )
    y += LINHA
    t = aparece + PAUSA_PROXIMO

# Último prompt com cursor piscando.
css.append(
    f"@keyframes qf{{0%,{pct(t)}{{opacity:0}}{pct(t + 0.001)},{FIM * 100:.3f}%{{opacity:1}}100%{{opacity:0}}}}"
    f"#pf{{animation:qf {CICLO}s infinite}}"
    "@keyframes pisca{0%,49%{opacity:1}50%,100%{opacity:0}}#cursor{animation:pisca 1s steps(1) infinite}"
)
corpo.append(
    f'<g id="pf"><text x="{X0}" y="{y}" class="prompt">{escape(PROMPT.strip())}</text>'
    f'<rect id="cursor" x="{X0 + len(PROMPT) * CW}" y="{y - FONTE + 2}" width="{CW}" height="{FONTE + 3}" fill="#e6edf3"/></g>'
)

assert t < CICLO * FIM - 1.5, f"sessão longa demais para o ciclo ({t:.1f}s)"

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{LARGURA}" height="{ALTURA}" viewBox="0 0 {LARGURA} {ALTURA}" role="img" aria-labelledby="titulo">
<title id="titulo">Terminal: whoami → lucas, desenvolvedor backend; stack java, spring boot, postgresql e docker; build com sucesso; em busca de estágio ou vaga júnior</title>
<style>
text{{font-family:ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace;font-size:{FONTE}px;white-space:pre}}
.prompt{{fill:#3fb950;font-weight:700}}.cmd{{fill:#e6edf3}}.out{{fill:#8b949e}}.ok{{fill:#3fb950;font-weight:700}}.status{{fill:#d29922}}
.barra{{fill:#8b949e;font-size:12px}}
{''.join(css)}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
</style>
<rect x="0.5" y="0.5" width="{LARGURA - 1}" height="{ALTURA - 1}" rx="10" fill="#0d1117" stroke="#30363d"/>
<path d="M0.5 10.5a10 10 0 0 1 10-10h{LARGURA - 21}a10 10 0 0 1 10 10v22h-{LARGURA - 1}z" fill="#161b22"/>
<line x1="0.5" y1="32.5" x2="{LARGURA - 0.5}" y2="32.5" stroke="#30363d"/>
<circle cx="20" cy="17" r="6" fill="#ff5f57"/><circle cx="40" cy="17" r="6" fill="#febc2e"/><circle cx="60" cy="17" r="6" fill="#28c840"/>
<text x="{LARGURA / 2}" y="21" text-anchor="middle" class="barra">lucas@dev: ~</text>
{chr(10).join(corpo)}
</svg>
"""
with open(SAIDA, "w", encoding="utf-8") as f:
    f.write(svg)
print(f"{SAIDA}: {LARGURA}x{ALTURA}, ciclo {CICLO}s, sessão termina em {t:.1f}s")
