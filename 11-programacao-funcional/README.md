# 11 – Programação Funcional

### Contexto e Motivação
Enquanto a Programação Orientada a Objetos modela o mundo através de objetos que encapsulam estado e comportamento, a **Programação Funcional (PF)** oferece um paradigma diferente: ela trata a computação como a avaliação de funções matemáticas, evitando estados mutáveis e dados compartilhados. A PF promove um estilo de código mais **declarativo**, onde descrevemos o que queremos fazer, em vez de como fazer passo a passo. Para este desafio, foi implementado um pipeline de análise de transações financeiras, um cenário do mundo real onde a clareza e a robustez da PF se destacam.

### Conceitos Funcionais em Ação
A solução implementada em Python demonstra os três pilares solicitados para este desafio:

1. **Funções de Alta Ordem (`map`, `filter`, `reduce`)**
   
As funções de alta ordem são o coração da programação funcional. São funções que podem receber outras funções como argumento ou retorná-las como resultado. Na solução utilizo o trio fundamental:

- `filter`: Usada para selecionar apenas os dados que atendem a um critério específico. No código, ela filtra a lista inicial para manter apenas as transações do tipo "Crédito".

- `map`: Aplicada para transformar cada elemento de uma coleção. Foi usada duas vezes: primeiro para calcular e adicionar a taxa de processamento a cada transação e, depois, para formatar cada objeto de transação em uma string legível para o relatório.

- `reduce`: Utilizada para "reduzir" uma coleção a um único valor. No nosso caso, ela calcula o valor total bruto somando os valores de todas as transações processadas.

O encadeamento dessas funções cria um **pipeline de dados**: map(calcular_taxa, filter(..., transacoes)). Essa abordagem é muito expressiva e fácil de entender.

2. Funções Puras e Imutabilidade
A implementação se baseia em funções puras, que são blocos de construção previsíveis. Uma função é pura se:

    1. Seu resultado depende unicamente de seus argumentos de entrada.

    2. Ela não produz efeitos colaterais observáveis (não modifica variáveis globais, não escreve em arquivos, etc.).

As funções `eh_do_tipo` e `formatar_para_relatorio` são exemplos claros. Um detalhe crucial que demonstra o princípio da imutabilidade está na função `calcular_taxa`:
```python
# Em vez de modificar o dicionário original, uma cópia é criada.
nova_transacao = transacao.copy()
nova_transacao["taxa"] = ...
return nova_transacao
```
Essa prática evita a modificação de dados originais, um dos pilares da PF, tornando o fluxo de dados mais seguro e fácil de rastrear.

3. Recursão
Para cumprir todos os requisitos do desafio, foi implementada uma função recursiva (`calcular_total_recursivo`) como uma alternativa ao `reduce` para agregar os valores. Ela segue o padrão clássico:

- **Caso Base:** Se a lista estiver vazia, retorna 0.

- **Passo Recursivo:** Soma o valor do primeiro elemento com o resultado da chamada da função para o restante da lista.

### Conclusão
Este desafio demonstrou como a Programação Funcional permite construir soluções robustas e expressivas para problemas de processamento de dados. Ao compor um pipeline com funções puras e de alta ordem, criamos um código que não é apenas conciso, mas também mais fácil de manter e testar. A solução para a análise de transações evidencia como os princípios de imutabilidade, funções como cidadãos de primeira classe e recursão se unem para formar uma alternativa poderosa aos laços e condicionais do paradigma imperativo.
