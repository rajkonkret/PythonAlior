import pandas as pd

product_data = {
    "product a": [13, 20, 0, 10],
    "product b": [10, 30, 17, 10],
    "product c": [6, 9, 10, 10],
}
print(product_data)
miasta = ["Kielce", "Poznań", "Warszawa", "Kraków"]
print(miasta)

data = pd.DataFrame(product_data, index=miasta)
print(data)
#           product a  product b  product c
# Kielce           13         10          6
# Poznań           20         30          9
# Warszawa          0         17         10
# Kraków           10         10         10

print(data.loc["Warszawa"] > 10)
# product a    False
# product b     True
# product c    False
# Name: Warszawa, dtype: bool

import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt
# pip install matplotlib

data['product b'].plot(kind="hist", title='product b')
plt.show()
