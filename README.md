# MovaCondo v3.0.0
App:        index.html, planos.html, termos.html, sw.js, manifest.webmanifest, icons/
Servidor:   worker.js + wrangler.jsonc (confere a assinatura no Mercado Pago)
Treinos:    data/g12/ (index.json, catalogo.json, AAAA-MM.json, status.json, fotos/)
Motor:      tools/ (não vai para o site)  ->  python tools/motor.py 12 2026-11 2027-12

Aparelho quebrado: data/g12/status.json -> "manutencao": ["leg_press_h"]
Revisar imagens:   /?revisar=1
Liberar celular de um assinante: Cloudflare > KV > ACESSOS > apagar a chave e:email
