# ITA Brain

> Banco de provas do vestibular do ITA organizado por matéria, com cada questão catalogada por assunto e competências. Objetivo: estudar de forma direcionada e mapear o que o ITA cobra.

## Sources

- `ita_provas_2008_2023/` — PDFs baixados do repo Mika-IO/vestibular-ita (GitHub)
- `ita_provas_2024_2026/` — `.rar`/`.zip` de brasilescola.uol.com.br

## Structure

    ita-brain/
    ├── MAP.md                  — este arquivo
    ├── banco_questoes.jsonl    — banco searchable; 1 linha por questão
    ├── taxonomia.md            — assuntos + competências catalogados (cresce com ingestão)
    ├── _inbox/                 — PDFs por processar
    ├── _processed/             — PDFs já ingeridos
    ├── matematica/
    │   ├── prova{ANO}.md       — reconstrução da prova (metadata + imagens)
    │   ├── prova{ANO}/         — imagens das questões (q01.png, q02.png, ...)
    │   └── prova{ANO}_f2.md    — quando há 2ª fase separada
    ├── fisica/        (mesma estrutura)
    ├── quimica/       (mesma estrutura)
    ├── ingles/        (mesma estrutura — adaptada)
    ├── portugues/     (mesma estrutura — adaptada)
    └── redacao/       (estrutura especial — tema/gênero, sem questões objetivas)

## Convenções

- **ID de questão (JSONL):** `{materia3}-{ano}-{fase}-q{NN}` — ex: `mat-2015-f1-q03`
- **Arquivos de prova:** `prova{ANO}.md` (1ª fase) e `prova{ANO}_f2.md` (2ª fase)
- **Imagens:** uma por questão dentro de `prova{ANO}/q{NN}.png`
- **Enunciado:** NÃO transcrito em markdown — só a imagem cropada
- **Metadata por questão:** assunto (1) + competências (N)

## Schema do JSONL

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

Para redação, campos extras: `tema`, `genero`.

## Gaps

- **1996–2007:** PDFs não obtidos (site oficial deu timeout na coleta)
- **Inglês/Português:** só 2008–2018 (a partir de 2019 saíram do vestibular)
- **Redação:** só 2019–2023 (introduzida na 2ª fase a partir de 2019)
- **Gabaritos:** existem como PDFs em `_inbox/` mas estão fora do escopo inicial — só catalogamos questões agora

## Last Updated

2026-05-16 — criação inicial do brain
