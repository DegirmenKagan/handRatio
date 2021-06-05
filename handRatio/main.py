# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 18:04:45 2021

@author: kagan degirmen
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")
plt.hist(data["ratio"],stacked=True,label="HandRatio")
plt.title("HandRatio(MFinger/forehand)",fontweight ="bold")
print(data)
plt.show()


