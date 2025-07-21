# 12 – Programação Lógica
### Contexto e Motivação
A **Programação Lógica** nos introduz a uma abordagem radicalmente diferente e puramente declarativa: em vez de escrever algoritmos, nós descrevemos um universo de conhecimento através de fatos e regras, e então fazemos perguntas (consultas) a esse universo. A linguagem mais emblemática deste paradigma é o **Prolog**. O programador define as relações lógicas entre as entidades, e o motor de inferência do Prolog se encarrega de deduzir as respostas. Para este desafio, modelaremos um problema clássico e intuitivo – uma árvore genealógica – para demonstrar os conceitos fundamentais da programação lógica.

### Programação Lógica em Prolog
Um programa em Prolog não tem um fluxo de execução tradicional. Ele é composto por uma base de conhecimento e uma consulta.

1. **Fatos (Facts):** São declarações incondicionalmente verdadeiras sobre o nosso domínio. São os "átomos" do nosso conhecimento. Por exemplo: `homem(joao).`

2. **Regras (Rules):** São declarações que definem novas verdades com base em fatos ou outras regras existentes. Elas nos permitem inferir conhecimento. A sintaxe é `cabeca :- corpo.`, que pode ser lida como "A cabeça é verdadeira se o corpo for verdadeiro".

3. **Consultas (Queries):** São as perguntas que fazemos à base de conhecimento. O motor do Prolog tenta encontrar todas as soluções possíveis que tornam a consulta verdadeira.

### Modelagem e Estrutura do Código
A solução completa para este desafio foi implementada em um arquivo Prolog nesse diretório, que contém toda a base de conhecimento sobre uma família fictícia.
Ele está dividido em duas seções principais:
- **Base de Fatos:** Contém as declarações básicas e irrefutáveis sobre o nosso domínio, como o sexo de cada indivíduo (`homem(joao).`, `mulher(ana)`.) e as relações diretas de progenitor (`progenitor(joao, pedro).`).

- **Base de Regras:** Define as relações mais complexas com base nos fatos. Por exemplo, a regra para `pai` (`pai(X, Y) :- progenitor(X, Y), homem(X).`) nos permite inferir quem é o pai de alguém, combinando a relação de progenitor com o sexo do indivíduo. Outras regras como `mae`, `avo` e `irmao` também foram definidas.

### Exemplos de Consultas (Queries)
- **Consulta:** `pai(joao, ana).`

    - **Tradução:** "João é pai de Ana?"

    - **Resposta Esperada:** `true`.

- **Consulta:** ` avo(joao, teresa).`

    - **Tradução:** "João é avô de Teresa?"

    - **Resposta Esperada:** `true`.

- **Consulta:** `irmao(pedro, X).`

    - **Tradução:** "Quem são os irmãos de Pedro?"

    - **Resposta Esperada:** `X = ana.`
 
### Conclusão
A programação lógica, exemplificada pelo Prolog, oferece uma forma poderosa de resolver problemas que envolvem lógica, raciocínio e busca em bases de conhecimento complexas. Ao invés de nos preocuparmos com laços e controle de fluxo, focamos em descrever o problema de forma precisa e declarativa. A modelagem da árvore genealógica demonstra a elegância e o poder de inferência deste paradigma, que é amplamente utilizado em áreas como inteligência artificial, processamento de linguagem natural e sistemas especialistas.
