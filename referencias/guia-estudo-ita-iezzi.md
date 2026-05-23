# Guia de estudo ITA usando Fundamentos de Matemática Elementar — Iezzi

Este é um mapa de território, não uma fila única. A ideia é o aluno avançar por ilhas de domínio: estudar teoria no Iezzi, resolver exercícios do livro, depois validar com questões reais do ITA.

Base usada: `banco_questoes.jsonl` de matemática do repo, 495 questões catalogadas de 2008 a 2026.

## Como usar

Para cada território:

1. Ler o capítulo/bloco indicado no Iezzi.
2. Fazer exercícios básicos até ganhar fluência mecânica.
3. Fazer exercícios intermediários/desafiadores do próprio volume.
4. Resolver as questões ITA indicadas sem consulta.
5. Marcar como conhecido só se conseguir explicar a solução em voz alta.

Critério prático:

- **Conhecido**: acerta questões ITA do bloco em tempo razoável.
- **Fronteira**: sabe a teoria, mas trava em combinações de ideias.
- **Desconhecido**: ainda depende de fórmula/receita.

---

# Mapa macro da coleção vs ITA

## Núcleo pesado do ITA

- **FME 6 — Complexos, Polinômios e Equações**: 99 questões no banco.
- **FME 4 — Sequências, Matrizes, Determinantes e Sistemas**: 70 questões.
- **FME 1 — Conjuntos e Funções**: 60 questões.
- **FME 5 — Combinatória e Probabilidade**: 59 questões.
- **FME 7 — Geometria Analítica**: 53 questões.
- **FME 3 — Trigonometria**: 50 questões.
- **FME 10 — Geometria Espacial**: 49 questões.
- **FME 9 — Geometria Plana**: 48 questões.

## Baixa incidência como assunto principal

- **FME 2 — Logaritmos**: aparece muito dentro de Funções, mas raramente como território isolado.
- **FME 8 — Limites, Derivadas e Integral**: quase não é eixo principal do ITA nesse banco.
- **FME 11 — Financeira, Estatística**: não é prioridade para ITA matemática tradicional.

---

# Jornada recomendada

## Fase 0 — Ferramentas de base

Objetivo: parar de perder questão por álgebra, notação ou manipulação.

### Estudar

- **FME 1**: noções de lógica, conjuntos, conjuntos numéricos, intervalos, relações.
- **FME 1**: funções, domínio, imagem, composição, inversa, inequações.
- **FME 2**: propriedades de logaritmos, mudança de base, equações e inequações logarítmicas.
- Revisar álgebra: fatoração, produtos notáveis, radicais, módulo, inequações.

### Questões ITA para validar

- Conjuntos: `mat-2008-f1-q19`, `mat-2010-f1-q01`, `mat-2013-f1-q01`, `mat-2024-f1-q37`
- Números reais/inequações: `mat-2008-f1-q21`, `mat-2012-f1-q05`, `mat-2014-f1-q01`, `mat-2015-f1-q01`, `mat-2017-f1-q07`, `mat-2020-f1-q52`
- Funções/log/exponenciais: `mat-2008-f1-q14`, `mat-2008-f1-q15`, `mat-2008-f1-q23`, `mat-2009-f1-q03`, `mat-2009-f1-q21`, `mat-2010-f1-q02`, `mat-2010-f1-q06`, `mat-2011-f1-q11`

### Marco de domínio

O aluno deve conseguir descobrir domínio/imagem, inverter função, compor funções, resolver inequações e reconhecer quando uma questão de logaritmo é só uma questão de função disfarçada.

---

## Fase 1 — Álgebra forte: o coração da prova

## Território A — Complexos

### Estudar

- **FME 6**: forma algébrica, conjugado, módulo.
- **FME 6**: forma trigonométrica/polar.
- **FME 6**: potências, raízes da unidade, De Moivre.
- **FME 6**: interpretação geométrica no plano complexo.

### Questões ITA

`mat-2008-f1-q02`, `mat-2008-f1-q22`, `mat-2009-f1-q04`, `mat-2009-f1-q22`, `mat-2010-f1-q03`, `mat-2010-f1-q04`, `mat-2011-f1-q01`, `mat-2011-f1-q02`, `mat-2011-f1-q03`, `mat-2011-f1-q22`, `mat-2012-f1-q03`, `mat-2012-f1-q04`

### Marco de domínio

Complexos deixam de ser “conta” e viram geometria: módulo como distância, argumento como ângulo, raiz como rotação.

## Território B — Polinômios e equações

### Estudar

- **FME 6**: grau, operações, divisão, resto, fatoração.
- **FME 6**: raízes, multiplicidade, relações de Girard.
- **FME 6**: raízes reais e complexas, conjugadas, inteiras/racionais.
- **FME 6**: equações algébricas e parâmetros.

### Questões ITA

`mat-2008-f1-q08`, `mat-2008-f1-q09`, `mat-2008-f1-q10`, `mat-2008-f1-q24`, `mat-2008-f1-q26`, `mat-2009-f1-q05`, `mat-2009-f1-q06`, `mat-2009-f1-q07`, `mat-2009-f1-q08`, `mat-2009-f1-q24`, `mat-2010-f1-q08`, `mat-2010-f1-q09`

### Marco de domínio

O aluno precisa enxergar fatoração, simetria de raízes, Girard e divisibilidade polinomial como uma caixa de ferramentas única.

---

## Fase 2 — Matrizes, sistemas e sequências

## Território C — Matrizes, determinantes e sistemas

### Estudar

- **FME 4**: matrizes, operações, produto, inversa.
- **FME 4**: determinantes e propriedades.
- **FME 4**: sistemas lineares, escalonamento, discussão com parâmetros.

### Questões ITA

`mat-2008-f1-q03`, `mat-2008-f1-q04`, `mat-2008-f1-q25`, `mat-2009-f1-q09`, `mat-2009-f1-q10`, `mat-2009-f1-q11`, `mat-2009-f1-q26`, `mat-2010-f1-q13`, `mat-2010-f1-q14`, `mat-2010-f1-q27`, `mat-2011-f1-q06`, `mat-2011-f1-q07`

### Marco de domínio

Saber calcular determinante não basta. O aluno precisa usar determinante como linguagem para dependência linear, inversibilidade e discussão de sistemas.

## Território D — Sequências e progressões

### Estudar

- **FME 4**: sequências, PA, PG, somas.
- **FME 4**: recorrências simples.
- **FME 4/FME 1**: somatórios, manipulação algébrica, indução informal.

### Questões ITA

`mat-2008-f1-q05`, `mat-2010-f1-q05`, `mat-2010-f1-q22`, `mat-2012-f1-q07`, `mat-2015-f1-q05`, `mat-2015-f1-q23`, `mat-2016-f1-q05`, `mat-2017-f1-q03`, `mat-2017-f1-q25`, `mat-2018-f1-q03`, `mat-2018-f1-q18`, `mat-2019-f1-q43`

### Marco de domínio

Reconhecer PA/PG escondida em geometria, polinômios, contagem e problemas de recorrência.

---

## Fase 3 — Contagem e probabilidade

## Território E — Combinatória

### Estudar

- **FME 5**: princípio fundamental da contagem.
- **FME 5**: permutações, arranjos, combinações.
- **FME 5**: binômio de Newton e identidades binomiais.
- **FME 5**: inclusão-exclusão, contagem por casos, simetria.

### Questões ITA

`mat-2008-f1-q17`, `mat-2009-f1-q01`, `mat-2009-f1-q02`, `mat-2010-f1-q11`, `mat-2010-f1-q21`, `mat-2011-f1-q23`, `mat-2012-f1-q01`, `mat-2012-f1-q14`, `mat-2012-f1-q21`, `mat-2014-f1-q07`, `mat-2016-f1-q19`, `mat-2018-f1-q26`

## Território F — Probabilidade

### Estudar

- **FME 5**: espaço amostral, eventos, complementar.
- **FME 5**: probabilidade condicional, independência, Bayes.
- **FME 5**: distribuição binomial, hipergeométrica, esperança simples.

### Questões ITA

`mat-2008-f1-q01`, `mat-2008-f1-q27`, `mat-2009-f1-q12`, `mat-2009-f1-q25`, `mat-2010-f1-q12`, `mat-2010-f1-q26`, `mat-2011-f1-q04`, `mat-2013-f1-q11`, `mat-2013-f1-q12`, `mat-2014-f1-q24`, `mat-2015-f1-q26`, `mat-2025-f2-q06`

### Marco de domínio

O aluno deve separar “contar casos” de “calcular probabilidade”. Em ITA, o erro comum é escolher o espaço amostral errado.

---

## Fase 4 — Trigonometria como linguagem

## Território G — Trigonometria

### Estudar

- **FME 3**: ciclo trigonométrico, seno, cosseno, tangente.
- **FME 3**: identidades fundamentais.
- **FME 3**: soma e diferença de arcos, arco duplo, arco metade.
- **FME 3**: equações trigonométricas.
- **FME 3 + FME 9**: lei dos senos, lei dos cossenos, área trigonométrica.

### Questões ITA

`mat-2008-f1-q11`, `mat-2008-f1-q13`, `mat-2008-f1-q16`, `mat-2009-f1-q13`, `mat-2009-f1-q17`, `mat-2009-f1-q27`, `mat-2010-f1-q07`, `mat-2010-f1-q15`, `mat-2010-f1-q16`, `mat-2010-f1-q28`, `mat-2011-f1-q14`, `mat-2011-f1-q17`

### Marco de domínio

Trigonometria não é decorar fórmula; é converter ângulo, comprimento, área e equação para a forma mais manipulável.

---

## Fase 5 — Geometria em três mapas

## Território H — Geometria plana

### Estudar

- **FME 9**: ângulos, paralelas, triângulos.
- **FME 9**: congruência, semelhança, relações métricas.
- **FME 9**: circunferência, potência de ponto, polígonos.
- **FME 9**: áreas.
- **FME 3**: lei dos senos/cossenos quando aparecer trigonometria.

### Questões ITA

`mat-2008-f1-q07`, `mat-2008-f1-q18`, `mat-2008-f1-q20`, `mat-2008-f1-q28`, `mat-2009-f1-q15`, `mat-2011-f1-q15`, `mat-2011-f1-q16`, `mat-2011-f1-q18`, `mat-2011-f1-q29`, `mat-2011-f1-q30`, `mat-2012-f1-q09`, `mat-2012-f1-q30`

## Território I — Geometria analítica

### Estudar

- **FME 7**: plano cartesiano, distância, ponto médio, área.
- **FME 7**: reta, inclinação, ângulo, distância ponto-reta.
- **FME 7**: circunferência.
- **FME 7**: cônicas — parábola, elipse, hipérbole.
- **FME 7 + FME 6**: lugares geométricos e álgebra pesada.

### Questões ITA

`mat-2008-f1-q12`, `mat-2008-f1-q30`, `mat-2009-f1-q14`, `mat-2009-f1-q16`, `mat-2009-f1-q18`, `mat-2009-f1-q28`, `mat-2009-f1-q29`, `mat-2010-f1-q17`, `mat-2010-f1-q19`, `mat-2010-f1-q29`, `mat-2011-f1-q13`, `mat-2012-f1-q10`

## Território J — Geometria espacial

### Estudar

- **FME 10**: posições relativas, paralelismo, perpendicularidade.
- **FME 10**: prismas, pirâmides, cilindros, cones, esfera.
- **FME 10**: áreas e volumes.
- **FME 10**: poliedros, Euler, sólidos inscritos/circunscritos.
- **FME 9/FME 3**: seções planas e trigonometria dentro do sólido.

### Questões ITA

`mat-2008-f1-q06`, `mat-2008-f1-q29`, `mat-2009-f1-q19`, `mat-2009-f1-q20`, `mat-2009-f1-q30`, `mat-2010-f1-q18`, `mat-2010-f1-q20`, `mat-2010-f1-q30`, `mat-2011-f1-q19`, `mat-2011-f1-q20`, `mat-2011-f1-q27`, `mat-2012-f1-q19`

### Marco de domínio

Geometria espacial do ITA costuma exigir reduzir o sólido a triângulos bons, seções planas e relações métricas conhecidas.

---

## Fase 6 — Territórios complementares

## Teoria dos números

Não há um volume dedicado na coleção FME clássica, mas aparece em problemas de divisibilidade, paridade, congruência e fatoração.

### Estudar por fora/complementar

- Divisibilidade.
- MDC/MMC.
- Congruências modulares.
- Paridade.
- Fatoração única.
- Expoente de primo em fatorial.
- Equações diofantinas simples.

### Questões ITA

`mat-2013-f1-q08`, `mat-2017-f1-q13`, `mat-2019-f2-q07`, `mat-2020-f1-q49`, `mat-2020-f2-q03`, `mat-2025-f1-q12`

## Cálculo / FME 8

Baixa prioridade como eixo principal para ITA, mas útil como maturidade matemática.

### Estudar se houver tempo

- Limite intuitivo e algébrico.
- Derivada como taxa/otimização.
- Noções de integral.

### Uso real

Serve mais para fortalecer raciocínio e algumas soluções alternativas do que como frente central de prova.

## Financeira/Estatística / FME 11

Baixa prioridade para ITA matemática. Estudar depois do núcleo, se a preparação estiver folgada.

---

# Ordem sugerida para um aluno começando sério

## Ciclo 1 — Base algébrica

1. FME 1 — conjuntos, reais, funções.
2. FME 2 — logaritmos, como extensão de funções.
3. FME 6 — complexos.
4. FME 6 — polinômios/equações.

## Ciclo 2 — Estrutura e contagem

5. FME 4 — matrizes, determinantes, sistemas.
6. FME 4 — sequências e progressões.
7. FME 5 — combinatória.
8. FME 5 — probabilidade.

## Ciclo 3 — Geometria e trigonometria

9. FME 3 — trigonometria.
10. FME 9 — geometria plana.
11. FME 7 — geometria analítica.
12. FME 10 — geometria espacial.

## Ciclo 4 — Revisão ITA

13. Refazer questões erradas por assunto.
14. Misturar assuntos em simulados.
15. Criar caderno de padrões: “quando vejo X, tento Y”.
16. Voltar ao Iezzi só nos buracos detectados.

---

# Checklist de conquista por território

- [ ] FME 1 — conjuntos e lógica básica.
- [ ] FME 1 — funções, composição, inversa, domínio/imagem.
- [ ] FME 2 — logaritmos e exponenciais.
- [ ] FME 6 — complexos algébricos e geométricos.
- [ ] FME 6 — polinômios, raízes, Girard, fatoração.
- [ ] FME 4 — matrizes, determinantes, sistemas.
- [ ] FME 4 — PA, PG, somas, recorrências.
- [ ] FME 5 — contagem e binômio.
- [ ] FME 5 — probabilidade, condicional, Bayes.
- [ ] FME 3 — identidades e equações trigonométricas.
- [ ] FME 9 — geometria plana.
- [ ] FME 7 — geometria analítica.
- [ ] FME 10 — geometria espacial.
- [ ] Teoria dos números complementar.
- [ ] Simulados mistos com questões ITA.

---

# Receita semanal simples

Para cada semana de estudo:

1. Escolher um território.
2. Ler teoria e exemplos do Iezzi.
3. Fazer 30–60 exercícios do livro, começando fáceis e subindo.
4. Resolver 8–12 questões ITA do mesmo território.
5. Registrar erros em três categorias:
   - não sabia teoria;
   - sabia, mas não viu o caminho;
   - erro algébrico/atenção.
6. Reestudar só o que apareceu como buraco real.

---

# Observação importante

O Iezzi é ótimo para construir musculatura. Mas a prova do ITA cobra mistura: uma questão catalogada como geometria pode usar trigonometria; uma de combinatória pode usar polinômio; uma de espacial pode virar geometria plana. Por isso o mapa deve ser usado como exploração de territórios, não como lista rígida de capítulos.
