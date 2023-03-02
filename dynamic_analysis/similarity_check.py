import os
import csv


baseline_path = '/home/budi/adblocker_project/adblocker_code/dynamic_analysis/distinct_traffic/domain_result_all_normal/baseline.har_fld.csv'
compared_file_path = '/home/budi/adblocker_project/adblocker_code/dynamic_analysis/distinct_traffic/domain_result_all_normal/2021/appinventor.ai_rockanarghya.browser_fld.csv'

def similarity_percentage(baseline_path,compared_file_path):
    baseline_list=[]
    file_list=[]
    
    with open(baseline_path,'r') as baseline:
        baseline_csv = csv.reader(baseline)
        next(baseline_csv,None)
        for line in baseline_csv:
            baseline_list.append(line[2].strip())

    with open (compared_file_path,'r') as file:
        file_csv = csv.reader(file)
        next(file_csv,None)
        for item in file_csv:
            file_list.append(item[2].strip())

    # print (baseline_list)
    # print(file_list)
    intersection_list = Intersection(baseline_list,file_list)
    union_list = Union(baseline_list,file_list)

    efectivenes = (len(baseline_list)-len(intersection_list))/len(baseline_list)
    print(round(1-efectivenes,3))
def Intersection(lst1, lst2):
    return set(lst1).intersection(lst2)

def Union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list

def main():
    similarity_percentage(baseline_path,compared_file_path)

if __name__=='__main__':
    main()