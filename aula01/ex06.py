# Serie com pandas - Cenario 02: Nota de alunos

import pandas as pd

notas = pd.Series([7.5, 8.0, None, 6.0, 9.0],
                  index= ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"],
                  name= "Notas")
print(notas)

print("\n1) Alunos sem nota registrada:\n", notas[notas.isnull()])
print("2) Substituindo nulos por 0:\n", notas.fillna(0))
print("3) Alunos com nota >= 7:\n", notas[notas >= 7])
print("4) Média da turma:", notas.mean())

