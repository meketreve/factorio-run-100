# Run 100% — Factorio 2.1

Rota para pegar as **88 conquistas** de Factorio 2.1 (59 do base + 29 do Space Age) em **uma única partida**, sem mods, configurações padrão.

### 👉 [Abrir a rota interativa](https://meketreve.github.io/factorio-run-100/)

A página tem o checklist das 88 com progresso salvo no navegador, as travas de ordem, a sequência de crafting manual, a lista de blueprints a montar e os macetes.

---

## As travas que decidem a run

Seis regras que, quebradas uma vez, matam a run inteira:

| Trava | Regra |
|---|---|
| **Mods** | Zero mods. Qualquer mod ativo troca a lista de conquistas por uma paralela que não sincroniza com a Steam. |
| **Mapa** | Padrão em inimigos, poluição, expansão, área inicial e árvores. Recursos e cliffs podem mudar. |
| **Artilharia** | A **primeira** estrutura inimiga destruída na partida tem que ser por artilharia (*Eu lavo minhas mãos*). Só vem depois de Vulcanus. |
| **Solar / laser** | Nenhum painel solar e nenhuma laser turret até o primeiro foguete. |
| **Baús** | Nenhum requester, buffer ou active provider até pesquisar com space science. |
| **Ciência** | Nada de production ou utility science antes de pesquisar com um pack de outro planeta. |

Relógios: locomotiva em **1 h 30**, foguete em **8 h**, Solar System Edge em **40 h**.

## Sequência de crafting manual

*Desgraçado preguiçoso* permite no máximo **111 itens** fabricados à mão até o foguete. Esta sequência fecha em **106**. Siga estritamente, sem fabricar nada extra — cada item fora da lista sai da sua folga.

| # | Item | |
|---:|---|---|
| 1 | 1× Burner mining drill | broca de mineração a queimador |
| 2 | 1× Stone furnace | fornalha de pedra |
| 3 | 1× Boiler | caldeira |
| 4 | 1× Steam engine | motor a vapor |
| 5 | 1× Offshore pump | bomba d'água costeira |
| 6 | 1× Small electric pole | poste elétrico pequeno |
| 7 | 1× Lab | laboratório |
| 8 | 10× Automation science pack | cartucho vermelho |
| 9 | 1× Assembling machine 1 | fábrica de montagem 1 |

**A partir da assembling machine, nada mais sai da mão** — ela fabrica tudo, inclusive as próximas máquinas. Acompanhe o contador em Produção → *hand crafted*.

## Conteúdo

```
index.html                 a rota interativa (é o que vira a página)
blueprints/                a preencher — montados à mão em jogo
ferramentas/
  perfil-mods.sh             alterna o mod-list.json entre vanilla e modded
  analisar-seed.py           mede árvores, água, ninhos e minério num preview de mapa
  contar-crafts.py           conta crafts manuais recursivamente a partir das receitas
```

## Blueprints

Ainda não há nenhum aqui. Os blueprints estão sendo montados à mão em jogo e vão ser commitados conforme ficarem prontos.

A lista do que cada um precisa conter — e a ordem em que são usados — está na seção **Os blueprints a montar** da [rota](https://meketreve.github.io/factorio-run-100/).

Duas regras ao salvar: **só entidades vanilla** (blueprint com entidade de mod chega quebrado na run) e **blueprint de space platform é um tipo separado**, que não mistura com blueprint de superfície.

## Ferramentas

**Perfil de mods.** Alterna entre vanilla (só base + DLC, conquistas ativas) e sua lista completa. Rodar com o jogo fechado:

```bash
./ferramentas/perfil-mods.sh vanilla
./ferramentas/perfil-mods.sh modded
```

**Busca de seed.** O binário do Factorio gera previews de mapa sem abrir o jogo:

```bash
factorio --generate-map-preview ./prev/ --map-gen-seed 1 --map-gen-seed-max 3999 --map-preview-size 512
python3 ferramentas/analisar-seed.py prev/*.png
```

O script classifica pixels pelas cores do `map_color` dos protótipos — ferro `(106,134,148)`, cobre `(205,99,55)`, carvão preto, pedra bege, água `(51,83,95)` — e ninhos pelo `default_enemy_color` `(255,25,25)`. Mede cobertura de árvore, distância do ninho mais próximo e quanto do perímetro está bloqueado por água.

**Contador de crafts.** *Desgraçado preguiçoso* conta cada **item** fabricado à mão, intermediários inclusive. O script expande a árvore de receitas a partir dos dados do jogo:

```bash
python3 ferramentas/contar-crafts.py
```

## Seeds avaliadas

A geração é determinística, mas depende de **seed + configurações + versão do jogo + mods carregados**. Seed de guia antigo não reproduz na 2.1, e o Space Age alterou a geração de Nauvis. Os números abaixo saíram de previews gerados na **2.1.20** com base + Space Age.

Medidas num raio de 512 tiles do spawn. `d.` é a distância até a mancha mais próxima, em tiles.

| seed | preset | árvore | **ninho** | ferro | cobre | carvão | pedra | d.fe | d.cu | d.ca |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **4249654844** ✓ | padrão | 17,0% | 181 | 365 | 201 | 193 | 98 | 63 | 25 | 29 |
| 1607 | padrão | 24,4% | **246** | 495 | 187 | 225 | 124 | 30 | 37 | 57 |
| 3407 | padrão | **24,7%** | **272** | 274 | 152 | 228 | 36 | 55 | 37 | 33 |
| 1982385249 | ferroviário | 24,7% | 149 | 540 | 296 | 253 | 70 | **21** | 69 | 33 |

### 4249654844 — a escolhida

**A favor:** tem **nós de rocha grandes perto do spawn**, que dão pedra e carvão juntos ao serem minerados — resolve o gargalo dos primeiros 20 minutos sem montar mineração de nenhum dos dois. Cobre a 25 e carvão a 29 tiles. Cobertura de árvore de 17%, cerca de cinco vezes a mediana.

**Contra:** ninho mais próximo a **181 tiles**, abaixo do piso de 200 que a varredura usava — e com a trava da artilharia você passa ~12 h sem poder limpar nada. Ferro a 63 tiles, o mais distante das candidatas.

### 1607 — a mais segura

**A favor:** folga de **246 tiles** até o ninho com 24,4% de árvore, a combinação mais confortável para a fase pré-artilharia. Ferro farto e perto (495 a 30 tiles).

**Contra:** carvão a 57 e pedra a 78 tiles. Começo mais burocrático: precisa montar mineração de pedra e carvão cedo.

### 3407 — a mais folgada e a mais pobre

**A favor:** maior distância de ninho (**272**) e maior floresta (24,7%) das 2000 varridas.

**Contra:** a mais pobre em minério das quatro. Ferro 274 a 55 tiles, cobre 152, e pedra quase inexistente (36, a 82 tiles) — aperta justamente o foguete de 8 h.

### 1982385249 — ferroviário, alto risco

**A favor:** ferro a **21 tiles** com 540 de área, e floresta de 24,7%.

**Contra:** ninho a **149 tiles**, o pior número medido. Pedra escassa (70). E por ser preset, exige reativar expansão de inimigos e conferir que evolução está em 40/200/9 antes de gerar — senão as conquistas caem.

### O que a medição não enxerga

O `analisar-seed.py` classifica pixels por `map_color` de **jazida**. **Rochas não são jazidas** — são entidades de classe decorativa, sem cor de minério no preview. Uma seed com rochas grandes ao redor do spawn (pedra e carvão de graça, cedo) aparece como pobre em pedra na tabela. Foi o caso da 4249654844. Olhe o preview no jogo, não só os números.

Petróleo também não entra: `crude-oil` não tem `map_color` próprio.

### Sobre água

Choke point de água praticamente não existe com configuração padrão. Nas 2000 seeds varridas, o melhor perímetro bloqueado por água foi **4,1%**, e na maioria os anéis de raio 140 e 180 deram **zero**. O preset ferroviário, que aumenta lagos, também não mudou isso de forma útil.

## Glossário das 88 conquistas

Nomes oficiais em pt-BR, extraídos do locale do jogo (`data/base/locale/pt-BR/base.cfg` e `data/space-age/locale/pt-BR/space-age.cfg`). O nome em inglês fica ao lado porque é o que guias e a wiki da comunidade usam. `·SA` marca as 29 do Space Age.

| pt-BR | inglês | condição |
|---|---|---|
| **Automatize isso!** | Automate this! | Construa uma máquina de montagem. |
| **Mantendo-se nos trilhos** | Getting on track | Construa uma locomotiva. |
| **Mantendo-se nos trilhos com maestria** | Getting on track like a pro | Construa uma locomotiva nos primeiros 90 minutos do jogo. |
| **Energia a vapor** | Steam power | Comece a produzir eletricidade com um motor a vapor. |
| **Energia Solar** | Solar power | Comece a produzir eletricidade com painéis solares. |
| **Energia nuclear** | Nuclear power | Comece a produzir eletricidade com uma usina nuclear. |
| **Inimigo da natureza** | Eco unfriendly | Pesquise refinamento de petróleo. |
| **Chega de fazer na mão** | Research with automation | Pesquise uma tecnologia usando pacotes científicos de automação. |
| **Hora de organizar** | Research with logistics | Pesquise uma tecnologia usando pacotes científicos de logística. |
| **Onde compro armas?** | Research with military | Pesquise uma tecnologia usando pacotes científicos militares. |
| **Traga o meu jaleco** | Research with chemicals | Pesquise uma tecnologia usando pacotes científicos de química. |
| **É fábrica de carro é?** | Research with production | Pesquise uma tecnologia usando pacotes científicos de produção. |
| **Isso deve ser útil** | Research with utility | Pesquise uma tecnologia usando pacotes científicos de utilitários. |
| **O doce som do espaço** | Research with space | Pesquise uma tecnologia usando pacotes científicos espaciais. |
| **Está fedendo e eles não gostam disso** | It stinks and they don't like it | Desencadeie um ataque alienígena pela poluição. |
| **Faça-me um banquete, estarei de volta para o café da manhã** | Smoke me a kipper… | Lance um foguete para o espaço. |
| **Sem tempo para conversa fiada** | No time for chitchat | Lance um foguete para o espaço dentro de 15 horas. |
| **Não existe colher** | There is no spoon | Lance um foguete para o espaço dentro de 8 horas. |
| **Desgraçado preguiçoso** | Lazy bastard | Vença o jogo criando não mais do que 111 itens. |
| **Vapor até o fim** | Steam all the way | Lance um foguete para o espaço sem construir painéis solares. |
| **Chuva de balas** | Raining bullets | Vença o jogo sem construir nenhuma torreta laser. |
| **Embargo de rede logística** | Logistic network embargo | Conclua todas as pesquisas com ciência espacial (Jogo base) ou qualquer pesquisa com ciência planetária (Space Age) sem usar baús provedores ativos, buffer ou solicitadores. |
| **Eu lavo minhas mãos** | Keeping your hands clean | Destrua sua primeira estrutura inimiga usando artilharia. |
| **A arte do estouro** | Art of siege | Destrua uma estrutura inimiga usando artilharia. |
| **O dedetizador chegou** | Pest control | Destrua um ninho de mordedores. |
| **Panquecas para a sogra** | Steamrolled | Destrua 10 ninhos por impacto. |
| **Corra Forrest, corra** | Run Forrest, run | Destrua 100 arvores por impacto. |
| **Piromaníaco** | Pyromaniac | Destrua 10.000 árvores com fogo. |
| **Isso está atrapalhando** | Terraformer | Destrua um penhasco. |
| **Eu sou o destruidor de mundos** | I am the destroyer of worlds | Use e faça CABUM! com uma bomba atômica. |
| **Golem** | Golem | Sobreviva a um ataque de 500 de dano ou mais. |
| **Cuidado onde pisa** | Watch your step | Seja morto por uma locomotiva em movimento. |
| **Minions** | Minions | Tenha 100 robôs de combate ou mais te seguindo. |
| **Aracnofobia** | Arachnophilia | Construa uma Spidertron. |
| **Expresso Trans-Factorio** | Trans-Factorio express | Tenha um trem que planeje uma trajetória de 1000 blocos ou mais. |
| **Até o último minério** | Mining with determination | Esgote completamente uma área de recursos. |
| **Você tem uma entrega** | You've got a package | Abasteça o personagem usando um robô logístico. |
| **Serviço de entrega** | Delivery service | Abasteça o personagem com 10k itens entregues por robôs logísticos. |
| **Construção automatizada** | Automated construction | Construa 100 estruturas usando robôs. |
| **Limpeza automatizada** | Automated cleanup | Desconstrua 100 objetos com robôs. |
| **Você está fazendo isso certo** | You are doing it right | Construa mais máquinas usando robôs do que manualmente. |
| **Acelera, que é sucesso** | Crafting with speed | Fabrique um módulo de velocidade 3. |
| **As árvores agradecem** | Crafting with efficiency | Fabrique um módulo de eficiência 3. |
| **Quanto mais, Melhor** | Crafting with productivity | Fabrique um módulo de produtividade 3. |
| **Solaris** | Solaris | Produza mais de 10 GJ por hora, usando apenas painéis solares. |
| **Produção em massa 1** | Mass production 1 | Produza 10k de circuitos eletrônicos. |
| **Produção em massa 2** | Mass production 2 | Produza 1M de circuitos eletrônicos. |
| **Produção em massa 3** | Mass production 3 | Produza 20M de circuitos eletrônicos. |
| **Veterano de circuitos 1** | Circuit veteran 1 | Produza 1k de circuitos avançados por hora. |
| **Veterano de circuitos 2** | Circuit veteran 2 | Produza 10k de circuitos avançados por hora. |
| **Veterano de circuitos 3** | Circuit veteran 3 | Produza 25k de circuitos avançados por hora. |
| **Era dos computadores 1** | Computer age 1 | Produza 500 unidades de processamento por hora. |
| **Era dos computadores 2** | Computer age 2 | Produza 1k de unidades de processamento por hora. |
| **Era dos computadores 3** | Computer age 3 | Produza 5k de unidades de processamento por hora. |
| **Trono de ferro 1** | Iron throne 1 | Produza 20k chapas de ferro por hora. |
| **Trono de ferro 2** | Iron throne 2 | Produza 200k chapas de ferro por hora. |
| **Trono de ferro 3** | Iron throne 3 | Produza 400k de chapas de ferro por hora. |
| **Cientista maluco** | Tech maniac | Pesquise todas as tecnologias. |
| **Até mais, e obrigado pelos peixes** | So long and thanks for all the fish | Mande um peixe cru ao espaço num foguete. |
| **Caminhando para as estrelas** ·SA | Reach for the stars | Crie uma plataforma espacial. |
| **Agora a chapa vai esquentar** ·SA | Visit Vulcanus | Viaje para o planeta Vulcanus. |
| **Um grande planeta rosa** ·SA | Visit Fulgora | Viaje para o planeta Fulgora. |
| **Eu tenho certeza que vou me arrepender disso** ·SA | Visit Gleba | Viaje para o planeta Gleba. |
| **Em Áquilo, o calor é lenda** ·SA | Visit Aquilo | Viaje para o planeta Áquilo. |
| **Está quente aqui** ·SA | Research with metallurgics | Pesquise uma tecnologia usando pacotes científicos de metalurgia. |
| **Quem ligou o imã?** ·SA | Research with electromagnetics | Pesquise uma tecnologia usando pacotes científicos eletromagnéticos. |
| **Elas crescem tão rápido** ·SA | Research with agriculture | Pesquise uma tecnologia usando pacotes científicos de agricultura. |
| **Está frio aqui** ·SA | Research with cryogenics | Pesquise uma tecnologia usando pacotes científicos criogênicos. |
| **Deixaram recado** ·SA | Research with promethium | Pesquise uma tecnologia usando pacotes científicos de Prometheus. |
| **Eu gosto assim, apressadinho** ·SA | Rush to space | Pesquise com ciência interplanetária antes de desbloquear pacotes científicos de produção ou de utilitários. |
| **Sai do meu gramado** ·SA | Get off my lawn | Irrite um demolidor construindo no seu território. |
| **Não foi tão difícil assim** ·SA | If it bleeds, we can kill it | Mate um demolidor pequeno. |
| **Precisamos de armas maiores** ·SA | We need bigger guns | Mate um demolidor médio. |
| **Tamanho não é documento** ·SA | Size doesn't matter | Mate um demolidor grande. |
| **Isso não me cheira bem** ·SA | It stinks and they do like it | Atraia um grupo de pentapods usando esporos. |
| **Faça melhor** ·SA | Make it better | Insira manualmente um módulo de qualidade em uma máquina. |
| **Isso está ficando bom** ·SA | Crafting with quality | Fabrique um módulo de qualidade 3. |
| **Uma lenda em forma de módulo** ·SA | My modules are legendary | Fabrique um módulo lendário de qualidade 3. |
| **Olhe para minha rara e brilhante armadura** ·SA | Look at my shiny rare armor | Equipe uma armadura MK2 rara, ou melhor. Ou uma armadura MK3. |
| **Há um burguês entre nós** ·SA | No room for more | Encha cada slot de uma armadura MK3 lendária com equipamentos lendários. |
| **Hoje teremos peixe 'a la creme'** ·SA | Today's fish is trout a la creme | Coma um peixe lendário. |
| **Energia de fusão nuclear** ·SA | Fusion power | Comece a produzir eletricidade com uma usina de fusão nuclear. |
| **Ao infinito e além....** ·SA | Second star to the right… | Termine o jogo. |
| **O melhor amigo do relógio** ·SA | Work around the clock | Termine o jogo dentro de 100 horas. |
| **Segunda estrela à direita e depois reto até amanhã** ·SA | Express delivery | Termine o jogo dentro de 40 horas. |
| **A primeira parada do Infinito** ·SA | Going to shattered planet 1 | Viaje 10 000 km se aproximando do planeta destruído. |
| **A escuridão além do Horizonte** ·SA | Going to shattered planet 2 | Viaje 30 000 km se aproximando do planeta destruído. |
| **Onde nem a luz se atreve a brilhar** ·SA | Going to shattered planet 3 | Viaje 60 000 km se aproximando do planeta destruído. |

> Duas curiosidades da localização: **Aracnofobia** traduz *Arachnophilia* (o oposto), e os nomes de *Express delivery* e *Second star to the right* aparecem **trocados** em relação ao inglês — as descrições é que estão certas. Vá pela descrição, não pelo nome.

## Licença

MIT.
