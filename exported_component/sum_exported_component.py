import pandas as pd 
import numpy as numpy
import os
import csv
from matplotlib import pyplot as plt

year_item = ['2016','2019','2021']

exp_path = '/home/budi/adblocker_project/adblocker_code/exported_component/'

average_list=[]

for item in year_item:
    file_path = exp_path+'exported_component_'+item+'.csv'
    df = pd.read_csv(file_path)
    average = round((df.mean(axis=0)),2)
    # average_list.append(average)
    item_list={'Year':item,'activities':average[0],'exported activities':average[1],\
        'services':average[2],'exported services':average[3],\
        'receivers':average[4],'exported receivers':average[5],'providers':average[6],'exported providers':average[7]}
    average_list.append(item_list)
sum_df = pd.DataFrame(average_list)
# aver = df.mean(axis=0)

dest_path = exp_path+'exp_summary.txt'
dest_fig = exp_path+'perc_exp_comp.pdf'

sum_df.to_csv(dest_path,index=None,sep='&')
print(sum_df)

sum_df.plot.bar(x='Year',width=0.9,figsize=(7,4))
plt.axis('tight')
# sum_df.plot.bar(x='Average # of Component and Exported Component per Apps', logy=True)
plt.xticks(rotation=0)
plt.ylabel('Average # per Apps')
plt.legend(bbox_to_anchor=(0.75, 1), loc='upper left')
plt.savefig(dest_fig)
plt.show()