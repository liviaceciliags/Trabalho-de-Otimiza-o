# Calculadora Simplex - Resolução de Problemas de Programação Linear

Este projeto implementa uma interface interativa em **Streamlit** para resolver problemas de **programação linear (PPL)** usando o método **Simplex**. A interface foi projetada para facilitar a entrada de dados, visualização de tabelas e análise de resultados, incluindo o impacto de alterações nas restrições sobre o lucro.

---

## Contribuidores
- Lívia Cecília Gomes Silva
- Álvaro Sampaio Careli
- Gustavo Pereira Dalboni

---

## Funcionalidades
1. **Entrada de Dados**:
   - Número de variáveis e restrições.
   - Coeficientes da função objetivo (lucro).
   - Coeficientes das variáveis para cada restrição.
   - Valores das constantes das restrições.

2. **Cálculos**:
   - Solução ótima utilizando o método Simplex.
   - Preços-sombra para as restrições.
   - Análise de vulnerabilidade para calcular o impacto de alterações nas restrições.

3. **Visualização**:
   - Exibição das tabelas inicial e final do método Simplex.
   - Exibição dos preços-sombra e resultados calculados.

---

## Uso

1. Execute o script principal:
   ```bash
   streamlit run interface.py
   ```

2. Insira os valores conforme solicitado pela interface:
   - Número de variáveis: 3.
   - Número de restrições: 2.
   - Coeficientes da função objetivo: **5, 7, 8**.
   - Coeficientes das variáveis para cada restrição:
     - Restrição 1: **1, 1, 2** com RHS: **1190**.
     - Restrição 2: **3, 4.5, 1** com RHS: **4000**.

3. Visualize os resultados:
   - Valores das variáveis ótimas: 
     - `x1 = 0.00`, `x2 = 851.25`, `x3 = 169.38`.
   - Lucro máximo: **7313.75**.

4. **Análise de Vulnerabilidade**:
   - Altere os valores das constantes das restrições.
   - O sistema calcula automaticamente o novo lucro máximo.

---

## Dependências
Certifique-se de instalar as bibliotecas necessárias:
```bash
pip install streamlit pulp pandas
```

---

## Exemplo

### Problema de Programação Linear:
**Maximizar Z = 5x1 + 7x2 + 8x3**  
**Sujeito a**:
- Restrição 1: `x1 + x2 + 2x3 <= 1190`
- Restrição 2: `3x1 + 4.5x2 + x3 <= 4000`
- `x1, x2, x3 >= 0`

### Passos na Interface:
1. Insira:
   - Número de variáveis: **3**.
   - Número de restrições: **2**.
   - Coeficientes da função objetivo: **5, 7, 8**.
   - Coeficientes das restrições:
     - Restrição 1: **1, 1, 2** com RHS **1190**.
     - Restrição 2: **3, 4.5, 1** com RHS **4000**.

2. Solução exibida:
   - Valores ótimos: `x1 = 0.00`, `x2 = 851.25`, `x3 = 169.38`.
   - Lucro máximo: **7313.75**.
   - Preços-sombra:
     - Restrição 1: **3.6250**.
     - Restrição 2: **0.7500**.

3. Realize a **Análise de Vulnerabilidade**:
   - Alterando a constante de Restrição 1 para **-119** e de Restrição 2 para **600**, o novo lucro máximo será atualizado automaticamente.

Com esta aplicação, resolver problemas de programação linear fica mais simples, interativo e visual. 🚀
