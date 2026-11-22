// MovaCondo – serviço de acesso. Confere a assinatura no Mercado Pago e limita celulares por plano.
// Variáveis (Cloudflare > Worker > Settings > Variables and Secrets):
//   MP_TOKEN   (Secret) = Access Token de PRODUÇÃO do Mercado Pago
//   CORTESIA   (Text)   = e-mails liberados sem pagar, separados por vírgula. Ex.: erik@x.com,esposa@y.com
// Opcional: KV "ACESSOS" (limite de celulares). Sem ele o acesso funciona, só não limita aparelhos.
const DUO_MIN = 24;              // assinatura mensal a partir de R$ 24 = plano Duo
const CORTESIA_CELULARES = 3;    // cortesia pode usar até 3 celulares
const json = (o, s = 200) => new Response(JSON.stringify(o), { status: s, headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store' } });

async function assinatura(email, token) {
  const u = `https://api.mercadopago.com/preapproval/search?payer_email=${encodeURIComponent(email)}&status=authorized&limit=10`;
  const r = await fetch(u, { headers: { Authorization: `Bearer ${token}` } });
  if (!r.ok) throw new Error('mp ' + r.status);
  const d = await r.json();
  const ativas = (d.results || []).filter(a => a.status === 'authorized' && (a.payer_email || '').toLowerCase() === email);
  if (!ativas.length) return null;
  const valor = Math.max(...ativas.map(a => Number(a.auto_recurring?.transaction_amount || 0)));
  const anual = ativas.some(a => a.auto_recurring?.frequency_type === 'months' && Number(a.auto_recurring?.frequency) === 12);
  const duo = anual ? valor >= DUO_MIN * 8 : valor >= DUO_MIN;
  return { plano: duo ? 'duo' : 'solo', limite: duo ? 2 : 1 };
}

export default {
  async fetch(req, env) {
    const url = new URL(req.url);
    if (url.pathname === '/api/acesso' && req.method === 'POST') {
      let b; try { b = await req.json(); } catch { return json({ ok: false, msg: 'Pedido inválido.' }, 400); }
      const email = String(b.email || '').trim().toLowerCase(), dev = String(b.device || '').slice(0, 40);
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email) || !dev) return json({ ok: false, msg: 'Digite um e-mail válido.' }, 400);
      const cortesia = String(env.CORTESIA || '').toLowerCase().split(/[,;\s]+/).filter(Boolean);
      let a;
      if (cortesia.includes(email)) a = { plano: 'cortesia', limite: CORTESIA_CELULARES };
      else if (!env.MP_TOKEN) return json({ ok: true, teste: true, plano: 'solo' });          // ainda sem Mercado Pago: modo teste
      else {
        try { a = await assinatura(email, env.MP_TOKEN); } catch (e) { return json({ ok: false, msg: 'Não foi possível consultar o pagamento agora. Tente em instantes.' }, 502); }
        if (!a) return json({ ok: false, msg: 'Não encontramos assinatura ativa para este e-mail. Use o mesmo e-mail do pagamento no Mercado Pago.' });
      }
      if (env.ACESSOS) {
        const k = 'e:' + email, lista = JSON.parse((await env.ACESSOS.get(k)) || '[]');
        if (!lista.includes(dev)) {
          if (lista.length >= a.limite) return json({ ok: false, msg: a.limite === 1
            ? 'Esta assinatura Solo já está em uso em outro celular. Para usar em 2 celulares, assine o plano Duo.'
            : 'Esta assinatura já está em uso no limite de celulares do plano.' });
          lista.push(dev); await env.ACESSOS.put(k, JSON.stringify(lista));
        }
      }
      return json({ ok: true, plano: a.plano, limite: a.limite });
    }
    if (url.pathname.startsWith('/api/')) return json({ ok: false }, 404);
    if (url.pathname === '/assinar' || url.pathname === '/assinar/') return Response.redirect(new URL('/planos.html', url), 302);
    return env.ASSETS.fetch(req);
  }
};
