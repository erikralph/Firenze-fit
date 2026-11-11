# Catálogo mestre Firenze Fit: equipamentos, exercícios, pools e mobilidade (vale para todos os grupos).
EQUIP = {
 "polia_alta":"Polia alta","polia_baixa":"Polia baixa","polia_triceps":"Polia de tríceps",
 "leg_press_h":"Leg press horizontal","maq_supino":"Máquina de supino","peck_deck":"Peck deck (peito / ombro invertido)",
 "extensora":"Cadeira extensora","flexora":"Cadeira flexora","mesa_flexora":"Mesa flexora",
 "adutora":"Cadeira adutora","abdutora":"Cadeira abdutora","smith":"Smith machine",
 "panturrilha_sent":"Panturrilha sentada","banco_scott":"Banco Scott","mesa_supino":"Mesa de supino regulável",
 "barra_supino":"Barra de supino","barra_w":"Barra W","barra_h":"Barra H","barra_reta":"Barra reta","anilhas":"Anilhas",
 "barra_fixa":"Barra fixa","halter_leve":"Halteres leves","halter":"Halteres pesados","banco":"Banco reto",
 "banco_reg":"Banco regulável","esteira":"Esteira","bike":"Bicicleta","transport":"Transport",
 "cama_elastica":"Cama elástica","bola_suica":"Bola suíça","colchonete":"Colchonete","caixote":"Caixote","grama":"Área de grama sintética"
}
G12_EQUIP = [k for k in EQUIP if k != "maq_supino"]   # Grupo 12 NÃO tem máquina de supino
GRUPOS = {
 "12": dict(nome="Grupo 12", torres=4, equip=G12_EQUIP,
   detalhes={"leg_press_h":"Horizontal, sentado","peck_deck":"De frente: peito · de costas: ombro posterior",
             "mesa_supino":"2 unidades, reguláveis","banco_reg":"2 unidades","halter_leve":"1 a 10 kg","halter":"12 a 20 kg (de 2 em 2)",
             "anilhas":"2,5 · 3 · 5 · 10 · 20 kg","esteira":"4 unidades","bike":"2 unidades","transport":"1 unidade","bola_suica":"2 unidades"},
   obs="Sem rack para agachamento livre: pernas com Smith, leg press e halteres."),
}
X = {}
def ex(id, nome, equip, musc, img, dicas, alt=None, tipo="forca", nota=None):
    X[id] = dict(id=id, nome=nome, equip=equip, musc=musc, img=img, dicas=dicas, alt=alt, tipo=tipo, **({"nota":nota} if nota else {}))

# ---- PEITO
ex("supino_maquina","Supino na máquina",["maq_supino"],"Peito","Machine_Bench_Press",["Pegada na linha do meio do peito","Escápulas presas no encosto","Empurre sem travar o cotovelo"],"supino_halter_reto")
ex("supino_barra","Supino reto com barra",["mesa_supino","barra_supino","anilhas"],"Peito","Barbell_Bench_Press_-_Medium_Grip",["Pés firmes no chão","Desça a barra até a linha do mamilo","Peça ajuda nas séries pesadas"],"supino_smith")
ex("supino_smith","Supino reto no Smith",["smith","banco","anilhas"],"Peito","Smith_Machine_Bench_Press",["Banco alinhado para a barra descer no meio do peito","Destrave girando o punho","Controle a descida em 2s"],"supino_halter_reto")
ex("supino_halter_reto","Supino reto com halteres",["banco","halter"],"Peito","Dumbbell_Bench_Press",["Halteres na linha do peito","Desça até sentir alongar","Suba em arco, sem bater"],"supino_smith")
ex("supino_inclinado_halter","Supino inclinado com halteres",["banco_reg","halter"],"Peito superior","Incline_Dumbbell_Press",["Banco em 30°","Halteres descem ao lado do peito","Junte sem bater no topo"],"supino_inclinado_barra")
ex("supino_inclinado_barra","Supino inclinado com barra",["mesa_supino","barra_supino","anilhas"],"Peito superior","Barbell_Incline_Bench_Press_-_Medium_Grip",["Mesa inclinada em ~30°","Barra desce na parte alta do peito","Cotovelos a ~45° do tronco"],"supino_inclinado_halter")
ex("crucifixo_inclinado","Crucifixo inclinado com halteres",["banco_reg","halter_leve"],"Peito superior","Incline_Dumbbell_Flyes",["Banco em 30°","Abra até a linha do ombro","Cotovelos levemente dobrados"],"crucifixo_maquina")
ex("crucifixo_maquina","Crucifixo no peck deck",["peck_deck"],"Peito","Butterfly",["Sente de frente para fora, costas no encosto","Feche os braços à frente do peito","Volte devagar, sem soltar o peso"],"crucifixo_halter",
   nota="O peck deck da sua academia pode ter pegadores em vez de apoio para os cotovelos. O movimento é o mesmo.")
ex("crucifixo_halter","Crucifixo com halteres",["banco","halter_leve"],"Peito","Dumbbell_Flyes",["Carga leve","Abra até a linha do ombro","Cotovelos fixos levemente dobrados"],"crucifixo_maquina")
# ---- COSTAS
ex("puxada_frente","Puxada alta pela frente",["polia_alta"],"Costas","Wide-Grip_Lat_Pulldown",["Peito aberto, leve inclinação para trás","Puxe a barra até o queixo","Cotovelos apontando para o chão"],"barra_fixa_ex")
ex("puxada_supinada","Puxada alta supinada",["polia_alta"],"Costas / bíceps","Underhand_Cable_Pulldowns",["Pegada na largura dos ombros, palmas para você","Puxe até a parte alta do peito","Suba controlando"],"barra_fixa_ex")
ex("puxada_fechada","Puxada alta pegada fechada",["polia_alta"],"Costas","Close-Grip_Front_Lat_Pulldown",["Mãos próximas","Puxe até o peito","Cotovelos rentes ao corpo"],"barra_fixa_ex")
ex("barra_fixa_ex","Barra fixa",["barra_fixa"],"Costas","Pullups",["Pegada um pouco mais aberta que os ombros","Peito em direção à barra","Se não conseguir, faça só a descida lenta (5s)"],"puxada_frente")
ex("remada_baixa","Remada baixa na polia",["polia_baixa"],"Costas","Seated_Cable_Rows",["Coluna neutra, sem balançar","Puxe em direção ao umbigo","Junte as escápulas no final"],"remada_halter")
ex("remada_halter","Remada unilateral com halter",["banco","halter"],"Costas","One-Arm_Dumbbell_Row",["Joelho e mão apoiados no banco","Puxe o halter em direção ao quadril","Não gire o tronco"],"remada_baixa")
ex("remada_curvada_halter","Remada curvada com halteres",["halter"],"Costas","Bent_Over_Two-Dumbbell_Row",["Tronco inclinado, coluna neutra","Puxe os halteres até o quadril","Junte as escápulas"],"remada_baixa")
ex("remada_curvada_smith","Remada curvada no Smith",["smith","anilhas"],"Costas","Smith_Machine_Bent_Over_Row",["Quadril para trás, tronco a ~45°","Puxe a barra até o abdome","Coluna sempre neutra"],"remada_baixa")
ex("pulldown_braco_reto","Pulldown com braços estendidos",["polia_alta"],"Costas","Straight-Arm_Pulldown",["Braços quase retos","Leve a barra até as coxas","Sinta a lateral das costas"],"pullover_halter")
ex("pullover_halter","Pullover com halter",["banco","halter"],"Costas / peito","Bent-Arm_Dumbbell_Pullover",["Deitado no banco","Leve o halter atrás da cabeça","Volte até acima do peito"],"pulldown_braco_reto")
# ---- OMBROS
ex("desenv_halter","Desenvolvimento com halteres",["banco_reg","halter"],"Ombros","Seated_Dumbbell_Press",["Encosto a 90°","Halteres na altura das orelhas","Não arqueie a lombar"],"desenv_smith")
ex("desenv_smith","Desenvolvimento no Smith",["smith","banco_reg","anilhas"],"Ombros","Smith_Machine_Overhead_Shoulder_Press",["Banco a 90° sob a barra","Barra desce até o queixo","Core firme"],"desenv_halter")
ex("desenv_arnold","Desenvolvimento Arnold",["banco_reg","halter_leve"],"Ombros","Arnold_Dumbbell_Press",["Comece com as palmas para você","Gire as mãos enquanto sobe","Desça girando de volta"],"desenv_smith")
ex("elevacao_lateral","Elevação lateral com halteres",["halter_leve"],"Ombros","Side_Lateral_Raise",["Carga leve","Suba até a linha do ombro","Cotovelo levemente dobrado"],"elevacao_lateral_polia")
ex("elevacao_lateral_polia","Elevação lateral na polia",["polia_baixa"],"Ombros","Cable_Seated_Lateral_Raise",["Fique de lado para a polia","Puxe cruzando o corpo até o ombro","Desça devagar"],"elevacao_lateral")
ex("elevacao_frontal","Elevação frontal com halteres",["halter_leve"],"Ombro anterior","Front_Dumbbell_Raise",["Suba até a linha dos olhos","Sem balançar o tronco","Alterne os braços"],"elevacao_lateral_polia")
ex("crucifixo_invertido","Crucifixo invertido no peck deck",["peck_deck"],"Ombro posterior","Reverse_Machine_Flyes",["Sente de frente para o encosto, peito apoiado","Abra os braços até a linha do corpo","Não use impulso"],"crucifixo_inv_halter",
   nota="É o mesmo peck deck do crucifixo, usado ao contrário (sentado de frente para o encosto).")
ex("crucifixo_inv_halter","Crucifixo invertido com halteres",["halter_leve","banco_reg"],"Ombro posterior","Reverse_Flyes",["Tronco inclinado à frente","Abra os braços como asas","Carga leve"],"crucifixo_invertido")
ex("face_pull","Face pull na polia alta",["polia_alta"],"Ombro posterior","Face_Pull",["Use a corda","Puxe em direção ao rosto","Cotovelos altos"],"crucifixo_invertido")
ex("encolhimento","Encolhimento com halteres",["halter"],"Trapézio","Dumbbell_Shrug",["Braços estendidos","Suba os ombros em direção às orelhas","Segure 1s"],"remada_curvada_smith")
# ---- BRAÇOS
ex("rosca_direta","Rosca direta com barra reta",["barra_reta","anilhas"],"Bíceps","Barbell_Curl",["Cotovelos colados ao corpo","Sem balançar o tronco","Desça até quase estender"],"rosca_halter")
ex("rosca_w","Rosca com barra W",["barra_w","anilhas"],"Bíceps","EZ-Bar_Curl",["Pegada na curva da barra","Cotovelos fixos","Controle a descida"],"rosca_halter")
ex("rosca_scott","Rosca Scott",["banco_scott","barra_w","anilhas"],"Bíceps","Preacher_Curl",["Axilas encaixadas no apoio","Não estenda totalmente no fim","Braço sempre no apoio"],"rosca_halter")
ex("rosca_halter","Rosca alternada com halteres",["halter_leve"],"Bíceps","Dumbbell_Alternate_Bicep_Curl",["Gire a palma para cima ao subir","Um braço por vez","Sem impulso"],"rosca_w")
ex("rosca_martelo","Rosca martelo",["halter_leve"],"Bíceps / antebraço","Hammer_Curls",["Palmas viradas uma para a outra","Cotovelos fixos","Desça devagar"],"rosca_w")
ex("rosca_concentrada","Rosca concentrada",["banco","halter_leve"],"Bíceps","Concentration_Curls",["Cotovelo apoiado na parte interna da coxa","Suba girando o punho","Desça devagar"],"rosca_w")
ex("triceps_polia","Tríceps na polia (barra)",["polia_triceps"],"Tríceps","Triceps_Pushdown",["Cotovelos colados ao corpo","Estenda totalmente","Volte só até 90°"],"triceps_frances")
ex("triceps_corda","Tríceps na polia (corda)",["polia_triceps"],"Tríceps","Triceps_Pushdown_-_Rope_Attachment",["Abra a corda no final","Cotovelos parados","Controle a subida"],"triceps_frances")
ex("triceps_frances","Tríceps francês com halter",["banco_reg","halter"],"Tríceps","Seated_Triceps_Press",["Sentado, halter atrás da cabeça","Cotovelos apontando para cima","Estenda sem abrir os cotovelos"],"triceps_polia")
ex("triceps_testa","Tríceps testa com barra W",["banco","barra_w","anilhas"],"Tríceps","EZ-Bar_Skullcrusher",["Barra desce até a testa","Cotovelos apontando para o teto","Carga moderada"],"triceps_polia")
ex("triceps_coice","Tríceps coice com halter",["banco","halter_leve"],"Tríceps","Tricep_Dumbbell_Kickback",["Tronco paralelo ao chão","Cotovelo fixo alto","Estenda o braço todo"],"triceps_polia")
ex("mergulho_banco","Mergulho no banco",["banco"],"Tríceps","Bench_Dips",["Mãos na borda do banco","Desça até 90° de cotovelo","Corpo perto do banco"],"triceps_polia")
# ---- PERNAS
ex("leg_press","Leg press horizontal",["leg_press_h"],"Quadríceps / glúteo","Leg_Press",["Costas inteiras no encosto","Pés na largura do quadril","Desça até 90° de joelho, não trave no fim"],"agachamento_smith",
   nota="A foto mostra o leg press inclinado. Na sua academia ele é horizontal (sentado): o movimento das pernas é o mesmo.")
ex("agachamento_smith","Agachamento no Smith",["smith","anilhas"],"Quadríceps / glúteo","Smith_Machine_Squat",["Pés um pouco à frente da barra","Desça até a coxa paralela","Joelhos na direção dos pés"],"leg_press")
ex("agachamento_goblet","Agachamento goblet",["halter"],"Quadríceps / glúteo","Goblet_Squat",["Halter junto ao peito","Desça entre as pernas","Tronco ereto"],"leg_press")
ex("agachamento_sumo","Agachamento sumô com halter",["halter"],"Adutores / glúteo","Plie_Dumbbell_Squat",["Pés afastados, pontas para fora","Halter entre as pernas","Tronco ereto"],"adutora_ex")
ex("bulgaro_halter","Agachamento búlgaro",["banco","halter_leve"],"Quadríceps / glúteo","Split_Squat_with_Dumbbells",["Peito do pé de trás apoiado no banco","Desça o joelho de trás em direção ao chão","Tronco levemente à frente para mais glúteo"],"afundo_halter",
   nota="No búlgaro o pé de trás fica apoiado no banco, mais alto que na foto.")
ex("afundo_halter","Afundo com halteres",["halter_leve"],"Quadríceps / glúteo","Dumbbell_Lunges",["Passo à frente","Joelho de trás quase no chão","Tronco ereto"],"step_up")
ex("step_up","Subida no caixote",["caixote","halter_leve"],"Quadríceps / glúteo","Dumbbell_Step_Ups",["Pé inteiro no caixote","Suba empurrando com a perna de cima","Desça controlando"],"afundo_halter")
ex("extensora_ex","Cadeira extensora",["extensora"],"Quadríceps","Leg_Extensions",["Joelho alinhado ao eixo da máquina","Segure 1s no topo","Desça em 2s"],"agachamento_goblet")
ex("flexora_sentada","Cadeira flexora",["flexora"],"Posterior de coxa","Seated_Leg_Curl",["Trave a coxa no apoio","Flexione até o fim","Volte devagar"],"mesa_flexora_ex")
ex("mesa_flexora_ex","Mesa flexora",["mesa_flexora"],"Posterior de coxa","Lying_Leg_Curls",["Quadril colado no banco","Puxe os calcanhares até o glúteo","Desça em 2s"],"flexora_sentada")
ex("stiff_halter","Stiff com halteres",["halter"],"Posterior / glúteo","Stiff-Legged_Dumbbell_Deadlift",["Joelhos levemente dobrados","Empurre o quadril para trás","Halteres rentes às pernas"],"stiff_smith")
ex("stiff_smith","Stiff no Smith",["smith","anilhas"],"Posterior / glúteo","Smith_Machine_Stiff-Legged_Deadlift",["Barra rente às coxas","Desça até alongar o posterior","Suba contraindo o glúteo"],"stiff_halter")
ex("elevacao_pelvica_smith","Elevação pélvica no Smith",["smith","banco","anilhas"],"Glúteo","Barbell_Hip_Thrust",["Costas apoiadas no banco","Colchonete sobre a barra","Contraia o glúteo 1s no topo"],"elevacao_pelvica_halter")
ex("elevacao_pelvica_halter","Elevação pélvica com halter",["banco","halter"],"Glúteo","Barbell_Glute_Bridge",["Halter apoiado no quadril","Suba até alinhar tronco e coxas","Segure 1s no topo"],"elevacao_pelvica_smith")
ex("adutora_ex","Cadeira adutora",["adutora"],"Adutores","Thigh_Adductor",["Costas apoiadas","Feche controlando","Abra devagar"],"agachamento_sumo")
ex("abdutora_ex","Cadeira abdutora",["abdutora"],"Glúteo médio","Thigh_Abductor",["Tronco levemente à frente","Abra até o máximo","Volte sem bater as placas"],"elevacao_pelvica_halter")
ex("panturrilha_sentada","Panturrilha sentada",["panturrilha_sent"],"Panturrilha","Seated_Calf_Raise",["Amplitude total","Segure 1s embaixo e em cima","Sem quicar"],"panturrilha_leg")
ex("panturrilha_leg","Panturrilha no leg press",["leg_press_h"],"Panturrilha","Calf_Press_On_The_Leg_Press_Machine",["Só a ponta dos pés na plataforma","Joelhos estendidos sem travar","Amplitude total"],"panturrilha_sentada")
ex("panturrilha_smith","Panturrilha em pé no Smith",["smith","anilhas"],"Panturrilha","Smith_Machine_Calf_Raise",["Ponta dos pés numa anilha","Suba o máximo","Desça alongando"],"panturrilha_sentada")
# ---- CORE
ex("prancha","Prancha",["colchonete"],"Core","Plank",["Cotovelos sob os ombros","Corpo em linha reta","Contraia abdome e glúteo"],"abdominal_bola",tipo="tempo")
ex("prancha_lateral","Prancha lateral",["colchonete"],"Oblíquos","Side_Bridge",["Cotovelo sob o ombro","Quadril alto","Lados alternados"],"abdominal_bola",tipo="tempo")
ex("abdominal_bola","Abdominal na bola suíça",["bola_suica"],"Abdome","Exercise_Ball_Crunch",["Lombar apoiada na bola","Suba só até tirar as escápulas","Expire ao subir"],"abdominal_solo")
ex("abdominal_solo","Abdominal no colchonete",["colchonete"],"Abdome","Crunches",["Mãos ao lado da cabeça, sem puxar","Suba o tronco curto","Expire ao subir"],"abdominal_bola")
ex("abdominal_infra","Abdominal infra no banco",["banco"],"Abdome inferior","Flat_Bench_Lying_Leg_Raise",["Segure no banco atrás da cabeça","Suba as pernas juntas","Desça sem tocar o chão"],"abdominal_bola")
ex("elevacao_pernas","Elevação de pernas na barra fixa",["barra_fixa"],"Abdome inferior","Hanging_Leg_Raise",["Pendurado, sem balançar","Suba os joelhos até o quadril","Desça devagar"],"abdominal_infra")

SO_INT = {"barra_fixa_ex","elevacao_pernas","triceps_testa","remada_curvada_smith","stiff_smith","supino_barra","supino_inclinado_barra","bulgaro_halter","desenv_arnold","encolhimento"}
POOLS = {
 "peito":["supino_maquina","supino_halter_reto","supino_barra","supino_smith"],
 "peito_inc":["supino_inclinado_halter","supino_inclinado_barra","crucifixo_inclinado"],
 "peito_iso":["crucifixo_maquina","crucifixo_halter"],
 "costas_v":["puxada_frente","puxada_supinada","puxada_fechada","barra_fixa_ex"],
 "costas_h":["remada_baixa","remada_halter","remada_curvada_halter","remada_curvada_smith"],
 "costas_iso":["pulldown_braco_reto","pullover_halter"],
 "ombro":["desenv_halter","desenv_smith","desenv_arnold"],
 "ombro_lat":["elevacao_lateral","elevacao_lateral_polia","elevacao_frontal"],
 "ombro_post":["crucifixo_invertido","face_pull","crucifixo_inv_halter"],
 "biceps":["rosca_w","rosca_halter","rosca_martelo","rosca_direta","rosca_scott","rosca_concentrada"],
 "triceps":["triceps_polia","triceps_corda","triceps_frances","triceps_testa","triceps_coice","mergulho_banco"],
 "quad":["leg_press","agachamento_smith","agachamento_goblet"],
 "uni":["afundo_halter","bulgaro_halter","step_up"],
 "quad_iso":["extensora_ex"],
 "post":["stiff_halter","stiff_smith"],
 "post_iso":["mesa_flexora_ex","flexora_sentada"],
 "gluteo":["elevacao_pelvica_halter","elevacao_pelvica_smith"],
 "abdutor":["abdutora_ex"],
 "adutor":["adutora_ex","agachamento_sumo"],
 "pant":["panturrilha_sentada","panturrilha_leg","panturrilha_smith"],
 "core":["prancha","abdominal_bola","abdominal_infra","prancha_lateral","abdominal_solo","elevacao_pernas"],
 "trap":["encolhimento"],
}
# ---- MOBILIDADE: cada item tem passo a passo + imagem (2 fotos)
def M(nome, equip, dose, img, *passos): return dict(nome=nome, equip=equip, dose=dose, img=img, passos=list(passos))
MOBX = {
 "circ_bracos": M("Círculos com os braços","grama","15 para frente + 15 para trás","Arm_Circles","Em pé, braços abertos na altura dos ombros","Faça círculos pequenos e vá aumentando","Troque o sentido no meio"),
 "gato": M("Gato-camelo","colchonete","10 repetições lentas","Cat_Stretch","De quatro apoios, mãos sob os ombros e joelhos sob o quadril","Arredonde as costas olhando para o umbigo","Depois afunde a coluna olhando para frente"),
 "toracica": M("Abertura torácica deitado de lado","colchonete","8 por lado","Side-Lying_Floor_Stretch","Deitado de lado, joelhos dobrados à frente","Braços esticados juntos à frente do peito","Abra o braço de cima até o outro lado, acompanhando com o olhar"),
 "rot_tronco": M("Rotação de tronco em pé","grama","10 por lado","Torso_Rotation","Pés afastados, joelhos levemente dobrados","Gire o tronco para um lado e para o outro","Quadril fica parado, só o tronco gira"),
 "agach_livre": M("Agachamento sem peso","grama","12 repetições lentas","Bodyweight_Squat","Pés na largura dos ombros","Desça como se fosse sentar numa cadeira","Suba devagar, calcanhar no chão"),
 "ponte": M("Ponte de glúteo no solo","colchonete","15 repetições","Butt_Lift_Bridge","Deitado de costas, joelhos dobrados e pés no chão","Suba o quadril contraindo o glúteo","Segure 1 segundo e desça devagar"),
 "quadril_4": M("Círculos de quadril em quatro apoios","colchonete","8 por perna","Hip_Circles_prone","De quatro apoios","Leve um joelho para o lado e faça círculos grandes","Troque de perna"),
 "posterior": M("Elevação de perna deitado (posterior)","colchonete","10 por perna","90_90_Hamstring","Deitado de costas, uma perna esticada no chão","A outra com quadril e joelho a 90°","Estique o joelho para cima, pause e volte"),
 "quadriceps": M("Alongamento de quadríceps em quatro apoios","colchonete","20 segundos por perna","All_Fours_Quad_Stretch","De quatro apoios","Segure o pé com a mão do mesmo lado","Puxe suave até sentir a frente da coxa"),
 "tornozelo": M("Círculos de tornozelo","grama","10 por lado","Ankle_Circles","Apoie-se em algo para equilíbrio","Tire um pé do chão","Faça círculos com o tornozelo nos dois sentidos"),
}
MOB = {
 "superior":["circ_bracos","gato","toracica","rot_tronco","ponte","quadril_4"],
 "inferior":["agach_livre","quadril_4","ponte","posterior","quadriceps","tornozelo"],
 "geral":["gato","agach_livre","circ_bracos","ponte","rot_tronco","posterior"],
}
