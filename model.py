# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

orderdata = pd.read_csv('orderdata.csv')


def create_dummies(df,column_name):
    dummies = pd.get_dummies(df[column_name],prefix=column_name)
    df = pd.concat([df,dummies],axis=1)
    return df
for column in ['Segment','Region','Ship Mode','Category']:
    orderdata = create_dummies(orderdata,column)
    
orderdata.head()

all_X_columns = ['Quantity', 'Discount', 'Profit',
       'Segment_Consumer', 'Segment_Corporate', 'Segment_Home Office',
       'Region_Central', 'Region_East', 'Region_South', 'Region_West',
       'Ship Mode_First Class', 'Ship Mode_Same Day', 'Ship Mode_Second Class',
       'Ship Mode_Standard Class', 'Category_Furniture',
       'Category_Office Supplies', 'Category_Technology']
all_X = orderdata[all_X_columns]
all_y = orderdata['Sales']




from sklearn.tree import DecisionTreeRegressor
dtr = DecisionTreeRegressor(max_leaf_nodes=50, random_state=0)

dtr.fit(all_X, all_y)

pickle.dump(dtr, open('model.pkl','wb'))