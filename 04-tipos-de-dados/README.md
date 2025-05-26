# 04 – Tipos de Dados

## Contexto e Motivação

No mundo das linguagens de programação, entender os sistemas de tipagem é tão essencial quanto dominar sintaxes e APIs – é a base que garante desde a clareza do código até a robustez das aplicações. Neste quarto desafio, veremos nas prática os modelos de tipagem de três linguagens que fazem parte do meu dia a dia: **Python**, **C#** e **JavaScript**. Vou destrinchar como cada uma define e verifica seus tipos, lida com coerções e quais garantias de segurança oferecem. 

---

## 1. Tipagem em Python

* **Paradigma:** Dinâmico, forte.
* **Verificação:** Somente em tempo de execução.
* **Declaração de Variáveis:** Não há declaração explícita; o interpretador infere o tipo a partir do valor.
* **Coerção:** Sempre explícita; misturar tipos gera erros claros (TypeError).
* **Segurança:** Alta, pois evita conversões implícitas que mascaram bugs.

```python
# Exemplo em Python
a = 10              # int
b = 2.5             # float
c = "Olá"         # str

# Usando anotações
def saudacao(nome: str) -> str:
    return f"Olá, {nome}!"

# Operações seguras
soma = a + b        # 12.5
mensagem = saudacao(c)

# Erro de tipo detectado em runtime
# resultado = a + c  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
---

## 2. Tipagem em C\#

* **Paradigma:** Estático, forte.
* **Verificação:** Em tempo de compilação pelo compilador Roslyn.
* **Declaração de Variáveis:** Obrigatória, mas `var` usa inferência local.
* **Generics e Nullable:** Permitem coleções tipadas e controle de valores nulos (`int?`).
* **Coerção:** Implícita entre tipos compatíveis; casting obrigatório para demais.
* **Segurança:** Muito alta, graças à verificação estática, ao sistema de tipos do .NET e ao suporte a *nullable reference types*.

```csharp
// Exemplo em C#
int a = 10;
double b = 2.5;
string c = "Olá";
int? valorOpcional = null;  // Nullable

// Inferência com var
var total = a + b;        // total é double

// Uso de Generics
dictionary<string, int> contagem = new Dictionary<string, int>();
contagem["maçãs"] = 5;

// Casting explícito quando necessário
int truncado = (int)b;    // 2

// Erro de compilação se tipo for incompatível
// int x = c;            // Cannot implicitly convert type 'string' to 'int'
```
---

## 3. Tipagem em JavaScript

* **Paradigma:** Dinâmico, fraco.
* **Verificação:** Apenas em tempo de execução.
* **Declaração de Variáveis:** `var`, `let` ou `const`, sem anotação de tipo.
* **Coerção:** Implícita e muitas vezes surpreendente; o motor faz conversões automáticas.
* **TypeScript (adjacente):** Adiciona tipagem estática opcional ao ecossistema JS.
* **Segurança**: Baixa — as coerções implícitas e comparações frouxas (`==`) podem mascarar bugs, levar a condições inesperadas e expor falhas de validação de entrada.
```javascript
// Exemplo em JavaScript puro
let a = 10;           // Number
let b = "2.5";      // String

// Coerções automáticas
console.log(a + b);   // "102.5" (concatena)
console.log(a - b);   // 7.5     (converte b para Number)

// Valores falsy em operações lógicas
console.log(false == 0); // true

// Evitar surpresas convertendo explicitamente
let num = Number(b); // 2.5
```
---

## 4. Cenários de Uso Ideais

* **Python:** análise de dados, automação de tarefas, prototipação rápida e aplicações científicas, onde a produtividade e legibilidade são primordiais.
* **C#:** sistemas corporativos, APIs robustas, jogos com Unity e aplicações desktop, especialmente quando a estabilidade e manutenção em longo prazo importam.
* **JavaScript:** interfaces web reativas, scripts de automação no navegador e serviços serverless simples, em projetos que exigem flexibilidade e rápido feedback visual.
