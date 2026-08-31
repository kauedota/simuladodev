# Simulado.dev

<p align="center">
  <img src="assets/logo.svg" alt="Logo do Simulado.dev" width="360" />
</p>

<p align="center">
  <a href="#">
    <img src="https://img.shields.io/badge/Status-Online-success" alt="Status online" />
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Tipo-Website%20Estática-7c3aed" alt="Tipo do projeto" />
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Linguagens-HTML%20%7C%20CSS%20%7C%20JS-0ea5e9" alt="Linguagens" />
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Deploy-Vercel-000000" alt="Deploy no Vercel" />
  </a>
</p>

Simulado de entrevistas técnicas para desenvolvedores em português. O projeto oferece um banco de perguntas por nível de senioridade, tema e dificuldade, com explicações completas ao final da sessão.

## ✨ Sobre o projeto

Este projeto simula uma experiência de entrevista técnica em navegador, com foco em candidatos que querem praticar lógica, arquitetura, frontend, backend, banco de dados, segurança, testes, DevOps e muito mais.

O usuário pode:

- escolher o nível: júnior, pleno ou sênior
- selecionar o tema da prova
- definir a quantidade de perguntas
- responder em sequência
- visualizar o resultado final com classificação estimada
- revisar as explicações de cada questão

Tudo acontece no navegador, sem backend, sem login e sem necessidade de instalação complexa.

## 🚀 Funcionalidades

- 252 perguntas de múltipla escolha
- 15 áreas de conhecimento
- suporte a níveis de senioridade diferentes
- explicações detalhadas das respostas
- persistência local via `localStorage`
- modo claro e escuro
- layout responsivo
- deploy como site estático

## 🧰 Stack

- HTML5
- CSS3
- JavaScript
- Python (geração do logo)

## 📁 Estrutura do projeto

```text
repo/
├── index.html
├── gerar-logo.py
├── package.json
├── README.md
├── LICENSE
├── vercel.json
├── .gitignore
├── assets/
│   ├── logo.svg
│   ├── logo-tema-claro.svg
│   ├── logo-icone.svg
│   └── ...
└── README.md
```

## ▶️ Como executar localmente

Você pode abrir o arquivo `index.html` diretamente no navegador, mas o ideal é servir a aplicação via HTTP:

```bash
cd repo
python3 -m http.server 8000
```

Depois acesse:

```text
http://localhost:8000
```

Ou use os scripts do projeto:

```bash
npm install
npm start
```

## 🌐 Deploy

Como o projeto é estático, ele pode ser publicado facilmente em plataformas como Vercel, Netlify e GitHub Pages.

### Vercel

```bash
npm install
npx vercel --prod
```

### GitHub Pages

1. Suba o projeto para o GitHub.
2. Ative o GitHub Pages no repositório.
3. Escolha a branch principal como fonte.

> O projeto não precisa de build step, então qualquer serviço de hospedagem estática funciona corretamente.

## 🧠 Banco de perguntas

A base de questões está no objeto `QUESTIONS` dentro do arquivo [index.html](index.html).

## 🎨 Logotipo

Para regenerar os arquivos de logo após alterações visuais, execute:

```bash
npm install
python3 -m pip install fonttools brotli
python3 gerar-logo.py
```

## 🤝 Contribuição

Contribuições são bem-vindas. Se quiser melhorar perguntas, corrigir explicações ou ajustar o design, basta abrir uma issue ou enviar um pull request.

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE).

## 🙌 Créditos

- Tipografia: Inter
- Design e estrutura do app: Simulado.dev
- Foco: prática de entrevistas técnicas em português
