import pandas as pd 
import numpy as numpy
import os
import csv
from matplotlib import pyplot as plt

year_item = ['2016','2019','2021']

exp_path = '/home/budi/adblocker_project/adblocker_code/exported_component/'

average_list=[]

for item in year_item:
    file_path = exp_path+'percentage_exp_comp_'+item+'.csv'
    df = pd.read_csv(file_path)
    average = round((df.mean(axis=0)),2)
    # average_list.append(average)
    item_list={'Year':item,'exported activities':average[0],'exported services':average[1],\
        'exported receivers':average[2],'exported providers':average[3]}
    average_list.append(item_list)
sum_df = pd.DataFrame(average_list)
# aver = df.mean(axis=0)

dest_path = exp_path+'perc_exp_summary.txt'
dest_fig = exp_path+'exp_number.pdf'
sum_df.to_csv(dest_path,index=None,sep='&')
print(sum_df)

sum_df.plot.bar(x='Year',width=0.9,figsize=(5,4))
# sum_df.plot.bar(x='Average # of Component and Exported Component per Apps', logy=True)
plt.xticks(rotation=0)
plt.ylabel('Average Percentage')
plt.legend(bbox_to_anchor=(0.5, 1), loc='upper left')
plt.savefig(dest_fig)
plt.show()