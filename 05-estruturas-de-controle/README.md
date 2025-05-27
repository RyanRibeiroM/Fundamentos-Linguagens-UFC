# 5 – Estruturas de Controle

### Contexto e Motivação

No universo da programação, o domínio de estruturas de seleção e repetição é essencial para criar sistemas dinâmicos e responsivos. Para tornar o aprendizado mais concreto, escolhi ambientar este desafio num cenário de **jardinagem automatizada**, em que um robô responsável pela manutenção de um jardim precisa ajustar comportamentos de irrigação e monitoramento de nutrientes com base em condições reais, como clima e saúde do solo. Esse contexto não só reforça conceitos de lógica de controle, como também estimula a aplicação de ideias de sensores, tomada de decisão e relatórios de atividades.

---

### Funcionalidades Principais

1. **Detecção de clima**

   * Identifica automaticamente o estado meteorológico (ensolarado, nublado ou chuvoso) para guiar as ações.

2. **Rotina de irrigação**

   * Em dia ensolarado: rega apenas no período da manhã.
   * Em dia nublado: rega tanto pela manhã quanto à tarde.
   * Em dia chuvoso: interrompe a irrigação e prioriza o monitoramento do solo.

3. **Monitoramento de nutrientes**

   * Sempre que a rega é suspensa, avalia níveis de Nitrogênio (N), Fósforo (P) e Potássio (K).
   * Compara valores simulados com parâmetros de referência e sugere fertilização caso algum nutriente esteja abaixo do ideal.

4. **Relatório de ações**

   * Ao término de cada execução, exibe um sumário detalhado das atividades por setor, incluindo rega e recomendações de solo.

---

### Como executar

1. Garanta que o **Python 3** esteja instalado.
2. Coloque `jardineiro_robot.py` e este README no mesmo diretório.
3. No terminal, execute:

   ```bash
   python jardineiro_robot.py
   ```
4. A saída mostrará o clima detectado e o relatório de ações para cada setor do jardim.


