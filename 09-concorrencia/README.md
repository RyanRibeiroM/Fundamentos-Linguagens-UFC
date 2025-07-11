# 9 - Concorrência

### Contexto e Motivação
No mundo real, inúmeros eventos acontecem simultaneamente. Em software, a concorrência é o paradigma que nos permite modelar essa simultaneidade, gerenciando múltiplas tarefas que progridem ao mesmo tempo. Em uma era de processadores com múltiplos núcleos, executar tarefas de forma puramente sequencial é um desperdício de performance. Aplicações responsivas, servidores de alta performance e processamento de dados em larga escala dependem fundamentalmente da concorrência.
Este desafio explora os fundamentos da concorrência, diferenciando seus dois principais modelos de execução — **processos e threads** — e implementa um exemplo prático em C# para demonstrar como a concorrência pode acelerar drasticamente tarefas que são computacionalmente intensivas.

### Processos vs. Threads: As Unidades de Execução
Embora ambos permitam a execução paralela de tarefas, processos e threads são conceitualmente distintos e servem a propósitos diferentes.

#### Processo:

- **Definição:** Um programa em execução. Cada processo é uma "caixa" isolada, com seu próprio espaço de memória, recursos e identificador no sistema operacional.

- **Memória:** Totalmente independente. A comunicação entre processos é segura, porém mais lenta e complexa, exigindo mecanismos de IPC (*Inter-Process Communication*).

- **Robustez:** Alta. A falha de um processo não afeta os outros. Se o seu navegador travar, seu editor de texto continua funcionando.

- **Custo:** "Pesado". A criação de um processo consome uma quantidade significativa de tempo e recursos do sistema.

#### Thread:

- **Definição:** Uma unidade de execução dentro de um processo. Um único processo pode ter múltiplas threads, que são como "mini-programas" rodando em paralelo.

- **Memória:** Compartilham o mesmo espaço de memória do processo pai. Isso torna a comunicação entre elas extremamente rápida, mas também perigosa se não for bem gerenciada (risco de race conditions).

- **Robustez:** Baixa. Uma falha em uma thread (como um acesso indevido à memória) pode derrubar o processo inteiro.

- **Custo:** "Leve". Threads são muito mais rápidas de criar e destruir.

### Cenário Prático: Processamento de Imagens em Lote
Para demonstrar a concorrência, simulamos um cenário onde um programa precisa aplicar um filtro (como redimensionar ou converter para preto e branco) em um lote de imagens.

- **O Problema (Abordagem Sequencial):** O programa processa uma imagem, termina, processa a próxima, e assim por diante. Se houver 8 imagens e cada uma levar 1 segundo para processar, o tempo total será de 8 segundos. Apenas um núcleo do processador é utilizado.

- **A Solução (Abordagem Concorrente):** O programa cria uma thread para cada imagem (ou para um grupo de imagens). Se o computador tiver 8 núcleos, ele pode, teoricamente, processar todas as 8 imagens simultaneamente, reduzindo o tempo total para aproximadamente 1 segundo.

### Implementação em C# com `System.Threading`
O código em C# a implementa essa simulação. Ele executa a tarefa de "processamento de imagem" de forma sequencial, mede o tempo, e depois a executa de forma concorrente, comparando os resultados.
A implementação completa pode ser encontrada no arquivo `ProcessadorDeImagens.cs`.

### Explicação da Implementação
1. **Função de Trabalho (`ProcessarImagem`):** Uma função simples que recebe o nome de um arquivo de imagem e simula um trabalho computacional intenso usando `Thread.Sleep()`.

2. **Execução Sequencial:** Um laço `foreach` simples chama a função `ProcessarImagem` para cada item da lista, um de cada vez.

3. Execução Concorrente:

- Um laço cria e inicia uma nova `Thread` para cada imagem.

- Cada `Thread` é adicionada a uma lista para controle.

- Um segundo laço usa o método `thread.Join()` em cada thread. Este comando faz com que o programa principal espere até que aquela thread específica termine sua execução. Isso é crucial para garantir que todas as tarefas sejam concluídas antes de medirmos o tempo final.

4. Medição de Performance: A classe `System.Diagnostics.Stopwatch` é usada para medir com precisão o tempo decorrido em ambas as abordagens, permitindo uma comparação clara da eficiência.

### Conclusão
A concorrência é uma ferramenta indispensável no cinto de utilidades de um desenvolvedor. Como demonstrado, o uso de threads pode proporcionar ganhos de performance expressivos, especialmente em tarefas paralelizáveis em máquinas com múltiplos núcleos.

No entanto, programar com concorrência introduz novos desafios, como a necessidade de sincronizar o acesso a dados compartilhados para evitar condições de corrida e deadlocks. Frameworks e linguagens modernas oferecem abstrações de alto nível (como a TPL - *Task Parallel Library* em .NET) para simplificar o gerenciamento dessas complexidades.
