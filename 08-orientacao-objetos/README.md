# 8 – Programação Orientada a Objetos
### Contexto e Motivação
A Programação Orientada a Objetos (POO) nos permite modelar sistemas complexos de forma intuitiva, espelhando o mundo real. Para este desafio, foi desenvolvido um sistema para gerenciar assinaturas de serviços de streaming, um domínio moderno que ilustra claramente como os pilares da POO podem ser usados para criar um código flexível, organizado e fácil de estender.

### Pilares da POO
O projeto foi estruturado para demonstrar na prática os quatro pilares fundamentais da POO:

- **Abstração:** A classe `Assinatura` foi definida como `abstract`. Ela serve como um "contrato", estabelecendo as características essenciais que todo plano de assinatura deve ter (como `PrecoMensal` e `DataRenovacao`), sem que seja possível criar uma instância de uma assinatura genérica.

- **Herança:** As classes `PlanoBasico` e `PlanoPremium` herdam diretamente de `Assinatura`. Elas reutilizam os atributos e a estrutura da classe base, adicionando apenas os comportamentos e propriedades que as tornam únicas, como `LimiteDeTelas` e `Qualidade4K`.

- **Encapsulamento:** Os dados internos das classes são protegidos. Propriedades como `PrecoMensal` utilizam `protected set`, garantindo que seu valor só possa ser definido durante a construção do objeto pela própria classe ou por suas derivadas, evitando modificações externas indevidas.

- **Polimorfismo:** O método `ExibirDetalhes()` foi declarado como `abstract` na classe mãe, forçando cada classe filha a fornecer sua própria implementação. Isso permite que, no programa principal, tratemos todos os tipos de assinatura de maneira uniforme, e o sistema se encarrega de chamar a versão correta do método para cada objeto. A eficácia disso é visível no laço principal:
```C#
foreach (var assinatura in minhasAssinaturas)
{
    assinatura.ExibirDetalhes();
}
```

### Estrutura do Projeto
O código está organizado em três arquivos de classe principais, que modelam a hierarquia, e um arquivo `Program.cs` que orquestra a execução:

1. `Assinatura.cs`: A classe base abstrata que define o modelo de uma assinatura.

2. `PlanoBasico.cs`: Primeira classe derivada, que implementa o plano mais simples.

3. `PlanoPremium.cs`: Segunda classe derivada, com funcionalidades adicionais.

O arquivo `Program.cs` cria instâncias desses planos e as exibe no console, demonstrando o sistema em funcionamento.


