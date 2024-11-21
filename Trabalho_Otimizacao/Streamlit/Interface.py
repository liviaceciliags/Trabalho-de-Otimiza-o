import streamlit as st
from simplex import SimplexSolver
import pandas as pd

def main():
    st.title("Resolução de Problemas de Programação Linear usando Simplex")

    if "solver" not in st.session_state:
        st.session_state.solver = None
        st.session_state.solution = None
        st.session_state.optimal_value = None
        st.session_state.shadow_prices = None
        st.session_state.b = None
        st.session_state.initial_table = None
        st.session_state.final_table = None
        st.session_state.new_b = None
        st.session_state.new_optimal_value = None

    st.markdown("**Número de variáveis (produtos)**")
    num_vars = st.number_input("Insira o número de variáveis", min_value=1, value=3)

    st.markdown("**Número de restrições**")
    num_constraints = st.number_input("Insira o número de restrições", min_value=1, value=2)

    st.markdown("**Coeficientes da Função Objetivo**")
    c = [st.number_input(f"Coeficiente x{i + 1}", value=1.0, key=f"c_{i}") for i in range(num_vars)]

    A = []
    b = []
    st.markdown("**Defina as Restrições**")
    for j in range(num_constraints):
        st.markdown(f"**Restrição {j + 1}**")
        row = [st.number_input(f"Coeficiente x{i + 1} para restrição {j + 1}", value=1.0, key=f"A_{j}_{i}") for i in range(num_vars)]
        A.append(row)
        rhs = st.number_input(f"Valor à direita da restrição {j + 1} (≤)", value=10.0, key=f"b_{j}")
        b.append(rhs)

    if st.button("Resolver"):
        solver = SimplexSolver(c, A, b)
        solution, optimal_value, shadow_prices, initial_table, final_table = solver.solve()

        st.session_state.solver = solver
        st.session_state.solution = solution
        st.session_state.optimal_value = optimal_value
        st.session_state.shadow_prices = shadow_prices
        st.session_state.b = b
        st.session_state.initial_table = initial_table
        st.session_state.final_table = final_table

    if st.session_state.solution is not None:
        st.success("Solução encontrada!")
        st.write("Valores das variáveis:")
        for i, val in enumerate(st.session_state.solution):
            st.write(f"x{i + 1} = {val:.2f}")
        st.write(f"Lucro máximo: {st.session_state.optimal_value:.2f}")

        st.markdown("**Tabela Inicial**")
        st.dataframe(st.session_state.initial_table)

        st.markdown("**Tabela Final**")
        st.dataframe(st.session_state.final_table)

        shadow_df = pd.DataFrame({
            'Restrição': [f"Restrição {i + 1}" for i in range(len(st.session_state.shadow_prices))],
            'Preço-Sombra': st.session_state.shadow_prices
        })
        st.markdown("**Preços-Sombra**")
        st.table(shadow_df)

        st.subheader("Análise de Vulnerabilidade")
        if st.checkbox("Deseja realizar a análise de vulnerabilidade?"):
            st.session_state.new_b = [st.number_input(f"Novo valor para Restrição {j + 1}", value=st.session_state.b[j], key=f"new_b_{j}") for j in range(len(st.session_state.b))]
            
            if st.button("Calcular Novo Lucro Máximo"):
                try:
                    # Calcular o novo lucro máximo diretamente
                    new_optimal_value = st.session_state.solver.calculate_new_profit(
                        st.session_state.shadow_prices,
                        st.session_state.new_b,
                        st.session_state.optimal_value
                    )

                    # Exibir os resultados
                    st.success("Novo lucro máximo calculado!")
                    st.write(f"Novo lucro máximo: {new_optimal_value + st.session_state.optimal_value:.2f}")
                    st.write(f"Variação no lucro: {new_optimal_value:.2f}")
                except Exception as e:
                    st.error(f"Erro: {e}")


if __name__ == "__main__":
    main()
