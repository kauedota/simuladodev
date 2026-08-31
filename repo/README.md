<p align="center">
  <img src="assets/logo.svg" alt="Simulado.dev" width="360">
</p>

<p align="center">
  Simulado de entrevista técnica para pessoas desenvolvedoras, em português.<br>
  252 perguntas de múltipla escolha, 15 temas, três níveis de senioridade.
</p>

<p align="center">
  <a href="#"><strong>Acesse o simulado</strong></a>
</p>

---

## O que é

Um simulado no estilo do que costuma cair em processos seletivos de bancos,
marketplaces, fintechs e empresas de software. Você escolhe o nível, o tema e a
quantidade de perguntas, responde, e no final recebe um nível estimado com uma
explicação simples de cada resposta.

Roda inteiro no navegador. Não tem back-end, não tem cadastro e nenhum dado sai
do seu aparelho: o histórico das tentativas fica no `localStorage`.

## Como rodar

Abra o `index.html` no navegador. É só isso.

Para servir localmente por HTTP, o que evita diferenças de comportamento em
relação ao ambiente publicado:

```bash
python3 -m http.server 8000
# abra http://localhost:8000
```

## Banco de perguntas

| | |
|---|---|
| Total | 252 perguntas |
| Temas | 15 |
| Níveis | júnior, pleno e sênior |
| Mínimo por tema | 5 júnior, 6 pleno e 5 sênior |

Temas cobertos: Fundamentos & Lógica, Java & Spring Boot, Python,
JavaScript & TypeScript, Frontend, Banco de Dados, Git, API/REST/Microsserviços,
Testes, Cloud/DevOps/Docker, Segurança, Arquitetura & Sistemas Distribuídos,
Mobile, Comportamental & Agile, e Linux/Redes/Performance.

### Como as alternativas foram escritas

Bancos de questões gerados sem cuidado vazam a resposta pela forma, não pelo
conteúdo. Uma versão anterior deste projeto tinha a resposta correta como a
alternativa mais longa em 96% das perguntas, o que permitia acertar 28 de 30 sem
ler nenhum enunciado. As regras abaixo existem para fechar isso:

- Toda alternativa tem entre 60 e 145 caracteres, e a diferença entre a maior e a
  menor da mesma pergunta fica em no máximo 18 caracteres.
- A correta é a mais curta em cerca de um quarto das perguntas, de propósito.
- As palavras `sempre`, `nunca`, `apenas`, `somente`, `totalmente`,
  `exclusivamente`, `obrigatoriamente` e `jamais` não aparecem em nenhuma
  alternativa, porque marcavam as erradas.
- As quatro alternativas de cada pergunta seguem o mesmo padrão gramatical.
- Distratores são conceitos vizinhos corretos ou equívocos reais, nunca absurdos.

Resultado medido com um bot que responde sem ler: clicar na alternativa mais
longa acerta 32%, contra 25% do acaso puro.

Se você adicionar perguntas, vale rodar essa checagem antes de commitar.

## Estrutura

```
index.html        aplicação inteira: HTML, CSS, JS e o banco de perguntas
gerar-logo.py     regenera os arquivos de logotipo a partir da fonte
assets/           logotipo em SVG e PNG, e o ícone para as lojas
```

O arquivo é único de propósito. Sem build, sem bundler e sem dependência de
runtime, o que também facilita empacotar como aplicativo depois.

## Contribuindo com perguntas

As perguntas ficam no array `QUESTIONS`, dentro do `index.html`. O formato:

```js
{nivel:"pleno", tema:"Banco de Dados", empresa:"Nubank",
 pergunta:"O que é normalização de um banco de dados relacional?",
 opcoes:["...","...","...","..."],
 correta:1, explicacao:"..."},
```

O campo `empresa` não indica autoria: ele é traduzido para um rótulo de segmento
pelo mapa `PERFIL`, porque as perguntas não são cópias de processos seletivos
reais dessas empresas.

## Logotipo

O logotipo é SVG com o texto já convertido em curvas, então não depende de fonte
instalada e não perde nitidez em nenhuma tela. As cores saem das variáveis CSS do
próprio app, o que faz um único ativo servir o tema claro e o escuro.

Para regenerar depois de mudar cor, corpo ou formato:

```bash
npm install
python3 -m pip install fonttools brotli
python3 gerar-logo.py
```

## Licença

Código sob licença MIT, veja o arquivo `LICENSE`.

O wordmark usa a tipografia [Inter](https://rsms.me/inter/), de Rasmus Andersson,
distribuída sob SIL Open Font License 1.1.
