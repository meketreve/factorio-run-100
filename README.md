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
blueprints/                blueprints do arranque, prontos para importar
  00-livro-arranque.txt      livro com as 5 abaixo
  01-fundicao.txt            coluna de fundição 1:1, 8 fornos
  02-mall.txt                6 assemblers com saída em baú
  03-labs.txt                bloco de 6 labs
  04-circuito-verde.txt      9 cabo : 6 circuito (razão 3:2)
  05-muralha.txt             muro + gun turrets, sem laser
  gerar-blueprints.py        gera e valida os .txt acima
ferramentas/
  perfil-mods.sh             alterna o mod-list.json entre vanilla e modded
  analisar-seed.py           mede árvores, água, ninhos e minério num preview de mapa
  contar-crafts.py           conta crafts manuais recursivamente a partir das receitas
```

## Blueprints

Importe `blueprints/00-livro-arranque.txt` — é o livro com as cinco dentro.

Os blueprints foram gerados por script e validados contra os dados da instalação do jogo: todo nome de entidade existe, os tamanhos vêm dos `collision_box` reais, nenhuma entidade se sobrepõe, e cada inserter pega de uma entidade real e entrega em outra.

> **`direction` de um inserter é o lado de onde ele PEGA**, não onde entrega. `pickup_position = {0,-2}`, `insert_position = {0,2.2}`. Errar isso deixa o blueprint inteiro 180° virado.

Você ainda precisa definir a receita de cada assembler — blueprint sem receita vem em branco.

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

## Notas sobre seeds

A geração é determinística, mas depende de **seed + configurações + versão do jogo + mods carregados**. Seed de guia antigo não reproduz na 2.1, e o Space Age alterou a geração de Nauvis.

Numa varredura de 2000 seeds com configuração padrão, a cobertura de árvore mediana ficou em **3,5%**, com as melhores perto de **24%**. Já choke point de água praticamente não existe: o melhor perímetro bloqueado foi **4,1%**, e na maioria das seeds os anéis de raio 140 e 180 deram zero.

## Licença

MIT.
