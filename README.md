# Pima Indian Diabetes Classification: Group Project Overview

- Implemented K-Nearest Neighbours and Naive Bayes from scratch to predict presence of diabetes based on differing health measurements
- Algorithms produced accuracy of ~75% for 5NN and Naive Bayes
- Weka was utilised to conduct feature selection and compare our algorithms with those inbuilt into Weka
- Such algorithms can be used in conjuction with domain-specific knowledge to provide preliminary understanding of patient's likelihood of having diabetes

## Accuracy of Algorithms (%)

|                               | ZeroR | 1R   | 1NN  | 5NN  | NB   | DT   | MLP  | SVM  | RF   |
|-------------------------------|-------|------|------|------|------|------|------|------|------|
| No feature selection          | 65.1  | 70.8 | 67.8 | 74.5 | 75.1 | 71.7 | 75.4 | **76.3** | 74.9 |
| Correlation Feature Selection | 65.1  | 70.8 | 69   | 74.5 | 76.3 | 73.3 | 75.8 | **76.7**| 75.9 |

|                               | My1NN | My5NN | MyNB |
|-------------------------------|-------|-------|------|
| No feature selection          | 68.4  | **75.4**  | 75.3 |
| Correlation Feature Selection | 68.2  | 75.1  |**76.4** |

