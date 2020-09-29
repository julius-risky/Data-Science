import pandas as pd
# Series
number_list = pd.Series([1,2,3,4,5,6])
print("Series:")
print(number_list)
# DataFrame
matrix = [[1,2,3],
          ['a','b','c'],
          [3,4,5],
          ['d',4,6]]
matrix_list = pd.DataFrame(matrix)
print("DataFrame:")
print(matrix_list)

#atribut data Frame
# [1] attribute .info()
print("[1] attribute .info()")
print(matrix_list.info())
# [2] attribute .shape
print("\n[2] attribute .shape")
print("    Shape dari number_list:", number_list.shape)
print("    Shape dari matrix_list:", matrix_list.shape)
