# Firenze Fit v2.1

## Pastas
index.html, sw.js, manifest.webmanifest, icons/   -> o app
data/g12/index.json      meses publicados do grupo (o app escolhe o mês sozinho)
data/g12/AAAA-MM.json    programa de cada mês (nov/2026 a dez/2027 já gerados)
data/g12/catalogo.json   exercícios e aparelhos que EXISTEM no Grupo 12
data/g12/status.json     aparelho em manutenção + aviso (você edita pelo GitHub)
data/g12/fotos/          fotos reais da academia (capa.jpg + um arquivo por aparelho)
tools/                   motor que gera os meses (não é usado pelo app)

## Regras automáticas
- Dia 1º: o app abre o arquivo do mês. Se o mês não existir, usa o último publicado.
- Aparelho quebrado: em status.json, "manutencao": ["leg_press_h"] -> o app troca pelo alternativo.
- Foto: se data/g12/fotos/leg_press_h.jpg existir, aparece em "Na sua academia". Se não existir, o app simplesmente não mostra.

## Gerar meses (quem gera é o Copilot; registro técnico)
python tools/motor.py 12 2028-01 2028-12
