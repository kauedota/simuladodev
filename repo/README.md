# Simulado.dev

Simulado de entrevista técnica para desenvolvedores, em português. O projeto reúne perguntas de múltipla escolha, organiza por tema e nível de senioridade, e ao final mostra uma avaliação estimada com explicações sobre cada resposta.

<p align="center">
  <img src="assets/logo.svg" alt="Logo do Simulado.dev" width="360" />
</p>

## Visão geral

Este projeto é uma aplicação web estática que simula a experiência de uma entrevista técnica. O usuário escolhe:

- nível de senioridade
- tema da prova
- quantidade de questões
- se prefere incluir ou não o modo de revisão com explicações

Ao final, o sistema calcula uma nota aproximada, classifica o perfil e mostra o desempenho por tema.

## Funcionalidades

- 252 perguntas de múltipla escolha
- 15 áreas de conhecimento
- suporte a níveis júnior, pleno e sênior
- explicação para cada alternativa correta e incorreta
- histórico e progresso salvos no navegador via localStorage
- tema claro e escuro
- sem backend, sem login e sem banco externo

## Stack

- HTML
- CSS
- JavaScript
- Python para geração do logo

## Estrutura do projeto

```text
repo/
├── index.html
├── gerar-logo.py
├── package.json
├── README.md
├── LICENSE
├── assets/
│   ├── logo.svg
│   ├── logo-tema-claro.svg
│   ├── logo-icone.svg
│   └── ...
└── .gitignore
```

## Como executar localmente

Você pode abrir o arquivo diretamente no navegador, mas o ideal é rodar por HTTP para evitar diferenças de comportamento:

```bash
cd repo
python3 -m http.server 8000
```

Em seguida, abra:

```text
http://localhost:8000
```

Se quiser usar o script do projeto:

```bash
npm install
npm start
```

## Deploy

Como o projeto é estático, ele pode ser publicado facilmente em plataformas como Vercel, Netlify ou GitHub Pages.

### Vercel (recomendado)

1. Faça push do projeto para um repositório GitHub.
2. Acesse o Vercel e clique em "New Project".
3. Importe o repositório.
4. Configure como projeto estático:
   - Framework: Other
   - Build command: vazio ou não obrigatório
   - Output directory: "."
5. Faça o deploy.

Também é possível publicar via CLI:

```bash
npm install
npx vercel --prod
```

### GitHub Pages

1. Ative o GitHub Pages no repositório.
2. Escolha a branch principal.
3. O site estático será servido diretamente pela pasta raiz do projeto.

> O projeto não precisa de build step, então qualquer serviço de hosting estático atende.

## Banco de perguntas

A base de dados de questões está dentro do arquivo principal do app, no objeto `QUESTIONS`, localizado em `index.html`.

## Logotipo

Para regenerar os arquivos de logo após alterações de estilo, execute:

```bash
npm install
python3 -m pip install fonttools brotli
python3 gerar-logo.py
```

## Contribuição

As perguntas e regras do app podem ser ajustadas diretamente no `index.html`, mas convém manter a estrutura de cada item consistente com o formato já usado no projeto.

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE).

## Créditos

- Tipografia: Inter
- A aplicação foi pensada para prática de entrevistas técnicas em português
