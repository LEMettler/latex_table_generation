# latex_table_generation
A simple python module to convert your data arrays/lists to code for a LaTeX table.

## Examples

```python
table_string = generateLatexTable(a1, a2, a3, a4, column_names=variables, round_values=[2,0,0,3],
                                  table_caption='CAPTION', table_label='LABEL', booktabs=False,
                                  file_name='test_numbers.txt')
```

![](https://github.com/Lmeerlu/latex_table_generation/blob/main/examples/test_numbers.JPG)

```python
from sklearn import datasets

iris = datasets.load_iris()
labels = iris.feature_names
data = iris.data[:10]

table = generateLatexTable(*data, column_names=labels, seperate_values=True,
                           table_caption='Wine', table_label='tab:iris', 
                           file_name='iris_table.txt')
```

![](https://github.com/Lmeerlu/latex_table_generation/blob/main/examples/wine_table.JPG)
