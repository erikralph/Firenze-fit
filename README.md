# Firenze Fit v2.4.0

## Estrutura
index.html, sw.js, manifest.webmanifest, icons/, wrangler.jsonc  -> o app
data/g12/  -> treinos do Grupo 12 (index.json, catalogo.json, AAAA-MM.json, status.json, fotos/)
tools/     -> motor que gera os treinos (não vai para o site)

## Rotina
- Atualizar o app: subir só os arquivos alterados (mesmo nome = substitui).
- Aparelho quebrado: editar data/g12/status.json -> "manutencao": ["leg_press_h"]
- Revisar imagens: abrir o app com /?revisar=1
- Fotos da academia: data/g12/fotos/ (capa.jpg, leg_press_h.jpg, peck_deck.jpg...)
