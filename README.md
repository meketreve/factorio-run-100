# Run 100% — Factorio 2.1

Rota para pegar as **88 conquistas** de Factorio 2.1 (59 do base + 29 do Space Age) em **uma única partida**, sem mods, configurações padrão.

### 👉 [Abrir a rota interativa](https://meketreve.github.io/factorio-run-100/)

A página tem o checklist das 88 com progresso salvo no navegador, as travas de ordem, a sequência de crafting manual, o livro de blueprints e os macetes.

---

## As travas que decidem a run

Seis regras que, quebradas uma vez, matam a run inteira:

| Trava | Regra |
|---|---|
| **Mods** | Zero mods. Qualquer mod ativo troca a lista de conquistas por uma paralela que não sincroniza com a Steam. |
| **Mapa** | Padrão em inimigos, poluição, expansão, área inicial e árvores. Recursos e cliffs podem mudar. |
| **Artilharia** | A **primeira** estrutura inimiga destruída na partida tem que ser por artilharia (*Keeping your hands clean*). Só vem depois de Vulcanus. |
| **Solar / laser** | Nenhum painel solar e nenhuma laser turret até o primeiro foguete. |
| **Baús** | Nenhum requester, buffer ou active provider até pesquisar com space science. |
| **Ciência** | Nada de production ou utility science antes de pesquisar com um pack de outro planeta. |

Relógios: locomotiva em **1 h 30**, foguete em **8 h**, Solar System Edge em **40 h**.

## Sequência de crafting manual

*Lazy bastard* permite no máximo **111 itens** fabricados à mão até o foguete. Esta sequência fecha em **106**. Siga estritamente, sem fabricar nada extra — cada item fora da lista sai da sua folga.

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

A lista do que cada um precisa conter — e a ordem em que são usados — está na seção **O livro de blueprints** da [rota](https://meketreve.github.io/factorio-run-100/).

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

**Contador de crafts.** *Lazy bastard* conta cada **item** fabricado à mão, intermediários inclusive. O script expande a árvore de receitas a partir dos dados do jogo:

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

## Licença

MIT.
