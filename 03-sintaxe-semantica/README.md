# 03 - Sintaxe e Semântica

## 1. Contexto e Motivação
A sintaxe de uma linguagem de programação define o formato correto de suas instruções, enquanto a semântica atribui significado a elas em tempo de compilação e execução.  
Nesta mini‑linguagem, voltada para cálculos de orçamentos financeiros, estendemos a gramática de expressões aritméticas para incluir porcentagens e funções matemáticas simples (por exemplo, `ceil`, `floor`). Além disso, detalhamos como o lexer ignora espaços em branco e comentários, e apresentamos tanto uma visão de semântica estática (tipagem) quanto dinâmica (avaliação).

---

## Análise Léxica

| Token    | Regex                        | Exemplo de lexema      |
|:---------|:----------------------------:|-----------------------:|
| PRINT    | `^print\b`                   | `print`                |
| CEIL     | `^ceil\b`                    | `ceil`                 |
| FLOOR    | `^floor\b`                   | `floor`                |
| IDENT    | `^[A-Za-z_][A-Za-z0-9_]*`    | `taxa`, `base_anos`    |
| NUM      | `^[0-9]+(\.[0-9]+)?`         | `100`, `42.5`          |
| PLUS     | `^\+`                        | `+`                    |
| MINUS    | `^-`                         | `-`                    |
| TIMES    | `^\*`                        | `*`                    |
| DIV      | `^/`                         | `/`                    |
| PERCENT  | `^%`                         | `%`                    |
| LPAREN   | `^\(`                        | `(`                    |
| RPAREN   | `^\)`                        | `)`                    |
| EQ       | `^=`                         | `=`                    |
| SEMI     | `^;`                         | `;`                    |

### Ignorando Espaços e Comentários
Antes de cada token, o lexer descarta zero ou mais subsequências de:
```bnf
<ws> ::= (" " | "\t" | "\n" | "//" .* "\n")*
```
Assim, espaços, quebras de linha e comentários de linha (// comentário) não interferem na análise de tokens.

## Gramática em EBNF
```bnf
<programa>     ::= { <instrucao> }

<instrucao>    ::= <atribuicao> ";"
                 | <print_instr> ";"

<atribuicao>   ::= IDENT "=" <expr>

<print_instr>  ::= "print" "(" <expr> ")"

<expr>         ::= <term> { ("+" | "-" ) <term> }

<term>         ::= <factor> { ("*" | "/" ) <factor> }

<factor>       ::= IDENT
                 | NUM [ "%" ]
                 | "ceil" "(" <expr> ")"
                 | "floor" "(" <expr> ")"
                 | "(" <expr> ")"
```

- Porcentagem: quando um NUM é seguido de %, o valor é interpretado como `NUM / 100`.
- Funções: ceil e floor arredondam, respectivamente, para cima e para baixo.
  
## Semântica  
Agora que vimos a sintaxe e a gramática em EBNF, vale a pena explorar a semântica para entender como nossas instruções realmente ganham vida.

### Semântica Estática  
- **Tipagem única**: todas as variáveis são `float`.  
- **Declaração antes do uso**: cada `IDENT` deve ser atribuído antes de usar.  
- **Compatibilidade**: operadores só aceitam operandos numéricos.

### Semântica Dinâmica  
- Literais retornam seu valor; identificadores buscam no ambiente.  
- Operações aritméticas avaliam recursivamente esquerda → direita.  
- `%` converte em decimal; `ceil`/`floor` arredondam após avaliação.  
- `print(expr)` exibe resultado sem modificar o ambiente.


## Exemplo de Código usando a mini-linguagem
```plaintext

// Define valor base do orçamento (em reais)
base = 100.0;           // NUM

// Aplica taxa de juros de 5% sobre o valor base
juros = base * (5 %);   // IDENT, TIMES, LPAREN, NUM, PERCENT, RPAREN

// Usa função ceil para arredondar para o inteiro superior
total = ceil(base + juros);

// Exibe resultado formatado
print(total);

```

### Sequência de tokens gerados pelo lexer:

```plaintext

IDENT("base"), EQ("="), NUM("100.0"), SEMI(";")
IDENT("juros"), EQ("="), IDENT("base"),
TIMES("*"), LPAREN("("), NUM("5"), PERCENT("%"), RPAREN(")"), SEMI(";")
IDENT("total"), EQ("="), CEIL("ceil"), LPAREN("("),
IDENT("base"), PLUS("+"), IDENT("juros"), RPAREN(")"), SEMI(";")
PRINT("print"), LPAREN("("), IDENT("total"), RPAREN(")"), SEMI(";")

```


