import csv
import os

if __name__ == "__main__":
    
    with open("DJI_20220712133408_0902.txt", 'r') as File:
        annots = File.readlines()
    
    converted_annots = []

    for i in range(len(annots)):
        annots[i] = annots[i].split(" ")[1:]
        temp = annots[i]
        annots[i] = [float(i) * 2000 for i in temp]
        
    count = 0
    for i in annots:
        l = i[0] - (i[2]/2)
        r = i[0] + (i[2]/2)
        u = i[1] - (i[3]/2)
        d = i[1] + (i[3]/2)
        l,r,u,d = l + 3096, r + 3096, u + 1730, d + 1730
        converted_annots.append([count,str([(l,u),(r,u),(r,d),(l,d)])])
        count += 1
    
    with open("DJI_20220712133408_0902.csv", 'w', newline = '') as CSVfile:
        wr = csv.writer(CSVfile)
        wr.writerow(['id','geometry'])
        wr.writerows(converted_annots)
        