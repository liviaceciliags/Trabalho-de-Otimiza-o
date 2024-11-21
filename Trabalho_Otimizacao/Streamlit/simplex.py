import pulp
import pandas as pd

class SimplexSolver:
    def __init__(self, c, A, b):
        self.c = c
        self.A = A
        self.b = b
        self.initial_b = b[:]  # Armazena os valores iniciais de b

    def solve(self):
        # Definir o problema de maximização
        problem = pulp.LpProblem("Problema_Simplex", pulp.LpMaximize)

        # Criar variáveis de decisão
        num_vars = len(self.c)
        vars = [pulp.LpVariable(f"x{i+1}", lowBound=0) for i in range(num_vars)]

        # Definir a função objetivo
        problem += pulp.lpDot(self.c, vars), "Função Objetivo"

        # Adicionar as restrições
        for i in range(len(self.A)):
            problem += (pulp.lpDot(self.A[i], vars) <= self.b[i]), f"Restrição_{i+1}"

        # Resolver o problema usando o método Simplex
        problem.solve()

        # Obter os valores das variáveis e o valor ótimo
        solution = [v.varValue for v in vars]
        optimal_value = pulp.value(problem.objective)

        # Extrair os preços-sombra (dual values)
        shadow_prices = [constraint.pi for name, constraint in problem.constraints.items()]

        # Criar as tabelas inicial e final
        initial_table = self._create_initial_table(vars)
        final_table = self._create_final_table(vars, solution, shadow_prices)

        return solution, optimal_value, shadow_prices, initial_table, final_table

    def _create_initial_table(self, vars):
        # Criar a tabela inicial com coeficientes da função objetivo e restrições
        columns = [var.name for var in vars] + ["RHS"]
        data = [self.c + [""]]
        for i, row in enumerate(self.A):
            data.append(row + [self.b[i]])

        # Converter todos os dados para strings para evitar problemas de serialização
        df = pd.DataFrame(data, columns=columns, index=["Função Objetivo"] + [f"Restrição {i+1}" for i in range(len(self.A))])
        return df.astype(str)

    def _create_final_table(self, vars, solution, shadow_prices):
        # Colunas: uma para cada variável e uma para cada preço-sombra
        columns = [var.name for var in vars] + [f"Preço-Sombra {i+1}" for i in range(len(shadow_prices))]
        # Dados: combinar a solução das variáveis com os preços-sombra
        data = [solution + shadow_prices]

        # Converter todos os dados para strings para evitar problemas de serialização
        df = pd.DataFrame(data, columns=columns, index=["Solução Ótima"])
        return df.astype(str)

    def calculate_new_profit(self, shadow_prices, new_b, previous_optimal_value):
        """
        Calcula o novo lucro diretamente somando o impacto calculado ao lucro anterior.
        """
        delta_b = [new_b[i] - self.initial_b[i] for i in range(len(new_b))]
        profit_change = sum((shadow_prices[i] * delta_b[i]) for i in range(len(delta_b)))
        return previous_optimal_value + profit_change
