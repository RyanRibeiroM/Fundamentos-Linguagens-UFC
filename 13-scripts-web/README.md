# 13 – Linguagens para Scripts e Web

### Contexto e Motivação
Linguagens de script, como Python e JavaScript, são projetadas para automação de tarefas, manipulação de dados e desenvolvimento rápido. Diferente de linguagens de sistema como C ou C++, o foco aqui não é a performance bruta, mas sim a produtividade do desenvolvedor e a facilidade de interação com o sistema operacional e outras ferramentas. Para este desafio, foi desenvolvido um script de automação para resolver um problema extremamente comum e que por vezes enfrento no meu dia a dia: a desorganização da pasta de "Downloads". Com o tempo, essa pasta se acumula com dezenas de arquivos de todos os tipos — imagens, documentos, instaladores, arquivos compactados — tornando difícil encontrar qualquer coisa. Este script automatiza o processo de organização, movendo cada arquivo para uma subpasta correspondente ao seu tipo.

### A Organização de Arquivos Inteligente
O script em Python realiza uma tarefa de automação simples, mas de grande impacto. Ele escaneia um diretório de origem (a pasta a ser organizada) e move os arquivos para um diretório de destino, criando subpastas categorizadas.
#### Funcionalidades Principais:
- **Mapeamento de Extensões:** O script possui um dicionário que mapeia extensões de arquivo (como `.jpg`, `.pdf`, `.zip`) a nomes de pastas de destino (como "Imagens", "Documentos", "Arquivos Compactados").

- **Criação Automática de Pastas:** Antes de mover qualquer arquivo, o script verifica se a pasta de destino para aquela categoria já existe. Se não existir, ele a cria automaticamente.

- **Movimentação Segura:** Utiliza o módulo `shutil` para mover os arquivos do diretório de origem para a pasta de destino correta.

- **Relatório de Ações:** Ao final da execução, o script exibe um relatório claro de quantos arquivos foram movidos e para quais categorias, além de listar os arquivos que não foram classificados.

### Como Executar o Script
1. **Estrutura de Pastas:** O script foi projetado para ser simples. Ele irá criar automaticamente duas pastas, `origem` e `destino`, no mesmo local onde o script for executado, caso elas não existam.

2. **Adicione os arquivos:** Coloque alguns arquivos de diferentes tipos (ex: `.txt`, `.jpg`, `.pdf`) dentro da pasta origem que foi criada.

3. **Execute:** Abra o terminal, navegue até o diretório onde o script está salvo e execute o seguinte comando:
```bash
python organizador_de_arquivos.py
```

O script irá mover os arquivos da pasta `origem` para subpastas categorizadas dentro da pasta `destino` e exibirá um relatório no console.

### Conclusão
Este desafio demonstra o poder e a simplicidade das linguagens de script para resolver problemas práticos de automação. Com poucas linhas de Python e o uso de módulos nativos como `os` e `shutil`, foi possível criar uma ferramenta útil que economiza tempo e mantém o sistema de arquivos organizado.
