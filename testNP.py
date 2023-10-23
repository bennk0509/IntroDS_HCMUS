# import numpy as np
# import pandas as pd
# # Two lists
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list = []
# list.append(list1)
# list.append(list2)
# print(list)
# # # Convert the lists to NumPy arrays
# # array1 = np.array(list1)
# # array2 = np.array(list2)
# # arrays = [
# #     np.array(["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"]),
# #     np.array(["one", "two", "one", "two", "one", "two", "one", "two"]),
# # ]

# # # Stack the arrays horizontally to create a 2D array
# # result = np.row_stack((array1, array2))
# # df = pd.DataFrame(np.random.randn(8, 4), index=arrays)
# # # Print the result
# # print(df)
# # print(len(arrays))

import pandas as pd

df1 = pd.DataFrame({'A': ['None', 'A1'], 'B': ['B0', 'B1']})
df2 = pd.DataFrame({'A': ['A2', 'A3'], 'B': ['B2', 'B3']})

result = pd.concat([df1, df2], axis=0)