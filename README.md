# ITA Brain — Banco de Questões do Vestibular do ITA

Banco searchable das provas do vestibular do ITA, organizado por matéria, ano e fase. Cada questão é catalogada por **assunto** e **competências** específicas, com a imagem original da questão preservada.

Objetivo: estudar de forma direcionada e mapear o que o ITA cobra.

## Estrutura

```
ita-brain/
├── MAP.md                  — meta-mapa do brain (leia primeiro)
├── banco_questoes.jsonl    — banco searchable; 1 linha JSON por questão
├── taxonomia.md            — assuntos + competências mapeados
├── _inbox/                 — PDFs por processar
├── _processed/             — PDFs já ingeridos
├── matematica/
│   ├── prova{ANO}.md       — reconstrução da prova (metadata + imagens)
│   └── prova{ANO}/         — imagens das questões (q01.png, q02.png, ...)
├── fisica/        (mesma estrutura)
├── quimica/       (mesma estrutura)
├── ingles/        (mesma estrutura)
├── portugues/     (mesma estrutura)
├── redacao/       (estrutura especial com tema/gênero)
└── scripts/
    ├── extract_questions.py  — extrai imagens de questões de um PDF
    └── build_index.py        — gera banco_questoes.jsonl + taxonomia.md a partir dos .md
```

## Schema do JSONL

Cada linha de `banco_questoes.jsonl`:

```json
{
  "id": "mat-2015-f1-q03",
  "materia": "matematica",
  "ano": 2015,
  "fase": 1,
  "numero": 3,
  "assunto": "logaritmo",
  "competencias": ["mudança de base", "equação logarítmica"],
  "tipo": "multipla_escolha",
  "imagem": "matematica/prova2015/q03.png",
  "arquivo": "matematica/prova2015.md"
}
```

Filtros fáceis com `jq`:

```bash
# Todas questões de matemática 2015
jq -c 'select(.materia=="matematica" and .ano==2015)' banco_questoes.jsonl

# Tudo de logaritmos
jq -c 'select(.assunto=="logaritmos")' banco_questoes.jsonl

# Discursivas de 2018+
jq -c 'select(.ano>=2018 and .tipo=="discursiva")' banco_questoes.jsonl
```

## Como ingerir uma prova nova

```bash
# 1. Coloque o PDF em _inbox/ com o nome convencional:
#    matematica_YYYY.pdf, fisica_YYYY_2f.pdf, ingles_YYYY.pdf, etc.

# 2. Extraia imagens (cria pasta com qNN.png + manifest.json):
python3 scripts/extract_questions.py _inbox/PROVA.pdf MATERIA/provaXXXX

# 3. Classifique manualmente cada questão e escreva o markdown
#    (formato: cada `## QNN` com Assunto/Competências/Tipo + imagem)

# 4. Rebuild dos índices derivados:
python3 scripts/build_index.py .

# 5. Mova PDF: mv _inbox/PROVA.pdf _processed/
```

## Convenções de nomes

- **Mono-matéria pré-2019** (fase única, 30 questões: 20 MC + 10 discursivas):
  `matematica_2015.pdf` → `matematica/prova2015.md`
- **Mono-matéria 2ª fase pós-2019** (só discursivas, ~10 questões):
  `fisica_2020_2f.pdf` → `fisica/prova2020_f2.md`
- **Fase 1 combinada pós-2019** (todas matérias juntas, ainda não processado):
  `2019_fase1.pdf` → splitter ainda não implementado

## Estado atual

Veja `MAP.md` para o catálogo completo de provas já processadas e gaps conhecidos.

## Stack

- `pdftoppm` + `pdftotext -bbox-layout` (poppler) para análise de PDFs
- `magick` (ImageMagick) para crops e stitching vertical
- `PyMuPDF` / `ocrmypdf` como fallbacks para PDFs problemáticos

## Licença

Material das provas é propriedade do ITA. Este repo organiza o conteúdo público das provas oficiais para fins de estudo.
