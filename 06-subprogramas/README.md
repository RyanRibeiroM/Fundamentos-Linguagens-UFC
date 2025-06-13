# 6 - Subprogramas

## Contexto e motivação 
Subprogramas, conhecidos como funções ou métodos, são a principal ferramenta para a **abstração de processos** em linguagens de programação. Eles nos permitem encapsular uma lógica complexa em uma unidade reutilizável, que pode ser invocada de diferentes pontos do código sem que precisemos nos preocupar com seus detalhes internos. No centro dessa interação está a passagem de parâmetros, o mecanismo que permite a comunicação de dados entre o código que chama (chamador) e o subprograma (chamado).

A forma como essa comunicação acontece define se o subprograma recebe uma cópia dos dados ou um acesso direto a eles, impactando diretamente o estado do programa e a ocorrência de efeitos colaterais. Neste desafio, exploraremos os modelos mais fundamentais, usando **C, Python e C#** para ilustrar como diferentes linguagens implementam e interpretam esses conceitos.

## 1. Passagem por Valor e por Referência em C

### Passagem por valor
Na passagem por valor, o subprograma recebe uma cópia do valor do parâmetro real. O parâmetro formal dentro do subprograma atua como uma variável local, e qualquer modificação feita nele não afeta a variável original no escopo do chamador. Essa é a abordagem padrão em C para tipos primitivos (como `int`, `float`, `char`).
 - **Vantagem**: Segurança, pois a função não pode modificar acidentalmente os dados do chamador.
 - **Desvantagem**: Ineficiência ao passar grandes estruturas de dados, pois exige tempo e memória para criar a cópia.

```C
#include <stdio.h>

// 'numero' é uma cópia do valor original.
void tentar_modificar_por_valor(int numero) {
    printf("  -> Dentro da função (antes): %d\n", numero);
    numero = 100; // Modifica apenas a cópia local.
    printf("  -> Dentro da função (depois): %d\n", numero);
}

int main() {
    int valor_original = 10;
    printf("Valor original (antes): %d\n", valor_original);
    
    tentar_modificar_por_valor(valor_original); // Passa uma cópia de 'valor_original'.
    
    printf("Valor original (depois): %d\n", valor_original); // Permanece inalterado.
    return 0;
}
```

### Passagem por Referência (Simulada com Ponteiros)
Na passagem por referência, um caminho de acesso (geralmente o endereço de memória) à variável original é passado para o subprograma. Isso permite que o subprograma modifique diretamente o valor da variável no escopo do chamador. Em C, a passagem por referência é simulada utilizando ponteiros.
- **Vantagem**: Eficiência, pois evita a cópia de grandes volumes de dados e permite que uma função modifique múltiplas variáveis do chamador.
- **Desvantagem**: Menos seguro. A função pode causar efeitos colaterais, modificando dados de forma inesperada e dificultando a legibilidade.

```C
#include <stdio.h>

// 'ponteiro_numero' armazena o endereço da variável original.
void modificar_por_referencia(int* ponteiro_numero) {
    printf("  -> Dentro da função (antes): %d\n", *ponteiro_numero);
    *ponteiro_numero = 100; // Modifica o valor no endereço de memória apontado.
    printf("  -> Dentro da função (depois): %d\n", *ponteiro_numero);
}

int main() {
    int valor_original = 10;
    printf("Valor original (antes): %d\n", valor_original);

    // Passa o endereço de memória de 'valor_original'.
    modificar_por_referencia(&valor_original); 
    
    printf("Valor original (depois): %d\n", valor_original); // O valor é modificado.
    return 0;
}
```

## 2. Passagem por Atribuição em Python
Python utiliza um mecanismo conhecido como passagem por atribuição (pass-by-assignment), que se comporta de maneira diferente para tipos de dados mutáveis e imutáveis.
- **Tipos Imutáveis (int, str, tupla)**: Comportam-se como passagem por valor. Embora uma referência ao objeto seja passada, o objeto em si não pode ser alterado. Qualquer tentativa de "modificação" (como `x = x + 1`) cria um novo objeto e atribui sua referência ao parâmetro local, sem afetar a variável original.
- **Tipos Mutáveis (list, dict)**: Comportam-se como passagem por referência. O parâmetro local e a variável original apontam para o mesmo objeto na memória. Modificar o conteúdo desse objeto dentro da função (por exemplo, com `lista.append(item)`) afeta a variável original no escopo do chamador.

```python
# Exemplo 1: Usando tipo imutável (int)
def modificar_imutavel(numero):
    print(f"  -> Dentro da função (antes): {numero}")
    numero = 100  # Cria um novo objeto int e atribui a 'numero'. O original não é afetado.
    print(f"  -> Dentro da função (depois): {numero}")

# Exemplo 2: Usando tipo mutável (list)
def modificar_mutavel(lista):
    print(f"  -> Dentro da função (antes): {lista}")
    lista.append(30) # Modifica o objeto original.
    print(f"  -> Dentro da função (depois): {lista}")

# Teste com tipo imutável
valor_int = 10
print(f"Valor int (antes): {valor_int}")
modificar_imutavel(valor_int)
print(f"Valor int (depois): {valor_int}") # Inalterado

print("-" * 20)

# Teste com tipo mutável
valor_list = [10, 20]
print(f"Valor list (antes): {valor_list}")
modificar_mutavel(valor_list)
print(f"Valor list (depois): {valor_list}") # Alterado
```

## 3. Passagem de Parâmetros em C#
C# é uma linguagem estaticamente tipada que distingue claramente entre tipos de valor (`int`, `float`, `struct`) e tipos de referência (`class`, `arrays`, `string`). O comportamento da passagem de parâmetros depende explicitamente do uso de palavras-chave.

- Padrão (Passagem por Valor):
  - Para tipos de valor, uma cópia do dado é passada, exatamente como em C.
  - Para tipos de referência, uma cópia da referência (endereço do objeto no heap) é passada. A função pode modificar o conteúdo do objeto, mas não pode fazer a variável original apontar para um novo objeto.
  
- `ref` (Passagem por Referência):
  - Passa uma referência à variável original, independentemente de ser tipo de valor ou de referência. Permite que o método altere diretamente o valor ou o objeto para o qual a variável do chamador aponta.

- `out` (Parâmetro de Saída):
  - Similar ao ref, mas é usado especificamente para retornar valores. A variável passada não precisa ser inicializada, mas o método deve atribuir um valor a ela antes de retornar.

```C#
using System;

public class GerenciadorDeValores
{
    // Passagem por valor (padrão para value types)
    public void ModificarValor(int numero)
    {
        numero = 100; // Modifica apenas a cópia local
    }

    // Passagem por referência com a palavra-chave 'ref'
    public void ModificarComRef(ref int numero)
    {
        numero = 100; // Modifica a variável original
    }
}

public class Teste
{
    public static void Main(string[] args)
    {
        var gerenciador = new GerenciadorDeValores();

        // Teste com passagem por valor
        int val = 10;
        Console.WriteLine($"Valor original (antes): {val}");
        gerenciador.ModificarValor(val);
        Console.WriteLine($"Valor original (depois de 'ModificarValor'): {val}"); // Inalterado
        
        Console.WriteLine(new string('-', 20));

        // Teste com passagem por referência ('ref')
        int refVal = 10;
        Console.WriteLine($"Valor ref (antes): {refVal}");
        gerenciador.ModificarComRef(ref refVal);
        Console.WriteLine($"Valor ref (depois de 'ModificarComRef'): {refVal}"); // Alterado
    }
}

```
