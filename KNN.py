import math
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
h=[159,180,186,180,156,165,177.8,150,179,182,177,157,170,154,189,168,177,164,183,164,165,176.74,167,155.75,178,163,167,185,180,170,154,162,157,162.56,185,160,180,173,180,170,172.72,180,179,164,185,172,176,180,163,175,170,163,146,168,162,155,161,155.4,152.4,164,154,164,168,152,160,152.4,174,165,173.73,150,180]
w=[46,85,95,58,65,60,71,36,52,70,78,47,70,40,72,74,66,48,82,65,67,80,44,64.3,55,59,65,70,60,45,67,48,47,60,82,58,68,76,52,58,60,67,68,54,65,68,60,58,45,79,78,75,43,48,50,56,55,46,44,63,45,57,62,39,54,50,55,55,60,44,80]
g=['F','M','M','M','M','F','M','F','M','M','M','F','M','F','M','M','M','F','M','M','M','M','M','M','M','M','M','M','M','F','F','F','F','F','M','F','M','M','M','M','M','M','M','F','M','M','M','M','F','M','M','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','M','F','M','F','M']
dis=[]
x=int(input("Enter Weight:"))
y=int(input("Enter Height:"))
for i in range(len(h)):
    dis.append(math.sqrt((w[i]-x)**2+(h[i]-y)**2))


    
print("===============================================================================================================")
print("UNORDERED TABLE:-\n")
print("  WEIGHT  "+"\t  HEIGHT  "+"\t      DISTANCE  "+"\t\t  GENDER  ")
print("----------\t----------\t----------------------\t\t----------")
for i in range(len(h)):
    print(str(w[i]).center(10),str(h[i]).center(10),str(dis[i]).center(22),"\t"+str(g[i]).center(12),sep="\t",end="\n\n")
list_of_lists = [h,w,g,dis]
[oh,ow,og,odis]=list(map(list, list(zip(*sorted(zip(*list_of_lists), key=lambda sublist_to_sort_by: sublist_to_sort_by[-1])))))
print("===============================================================================================================")
print("ORDERED TABLE:-\n")
print("  WEIGHT  "+"\t  HEIGHT  "+"\t      DISTANCE  "+"\t\t  GENDER  ")
print("----------\t----------\t----------------------\t\t----------")
for i in range(len(h)):
    print(str(ow[i]).center(10),str(oh[i]).center(10),str(odis[i]).center(22),"\t"+str(og[i]).center(12),sep="\t",end="\n\n")
print("===============================================================================================================")
k=int(input("Enter the value for K:"))
if k<=len(oh):
    print("===============================================================================================================")
    print("  WEIGHT  "+"\t  HEIGHT  "+"\t      DISTANCE  "+"\t\t  GENDER  ")
    print("----------\t----------\t----------------------\t\t----------")
    for i in range(k):
        print(str(ow[i]).center(10),str(oh[i]).center(10),str(odis[i]).center(22),"\t"+str(og[i]).center(12),sep="\t",end="\n\n")
else:
    print("===============================================================================================================")
    print("  WEIGHT  "+"\t  HEIGHT  "+"\t      DISTANCE  "+"\t\t  GENDER  ")
    print("----------\t----------\t----------------------\t\t----------")
    print("Since K value is greater than the total size of the list, default value would be applied where K=3")
    for i in range(3):
        print(str(ow[i]).center(10),str(oh[i]).center(10),str(odis[i]).center(22),"\t"+str(og[i]).center(12),sep="\t",end="\n\n")
print("===============================================================================================================")
if og[0:k].count('M')>og[0:k].count('F'):
    gender_Predicted="Male"
    print("\nGENDER PREDICTED: MALE")
elif og[0:k].count('M')<og[0:k].count('F'):
    gender_Predicted="Female"
    print("\nGENDER PREDICTED: FEMALE")
else:
    print("\nGENDER PREDICTED: CANNOT TELL")
hm=[]
wm=[]
hf=[]
wf=[]
for i in range(len(g)):
    if g[i]=='M':
        hm.append(h[i])
        wm.append(w[i])
    else:
        hf.append(h[i])
        wf.append(w[i])

plt.scatter(wm,hm,color='blue',s=10)
plt.scatter(wf,hf,color='deeppink',s=10)
plt.scatter(x,y,color='red')
plt.title("K-Nearest Neighbour")
plt.xlabel("Weight")
plt.ylabel("Height")
plt.legend(handles=[mpatches.Patch(color='blue', label='Male'),mpatches.Patch(color='deeppink', label='Female'),mpatches.Patch(color='red', label='YOU')])
plt.show()
True_Male=2
True_Female=1
False_Male=1
False_Female=1
gender_actual=input("Enter your Actual Gender:")
if gender_actual=="Female" and gender_Predicted=="Female":
    True_Female+=1
elif gender_actual=="Male" and gender_Predicted=="Male":
    True_Male+=1
elif gender_actual=="Female" and gender_Predicted=="Male":
    False_Male+=1
elif gender_actual=="Male" and gender_Predicted=="Female":
    False_Female+=1
print("===============================================================================================================")
print("CONFUSION MATRIX:-")
print("True Male=",True_Male)
print("True Female=",True_Female)
print("False Male=",False_Male)
print("False Female=",False_Female)
print("===============================================================================================================")
print("Following are the Performance Metrics of Confusion Matrix:-\n")
print("1.Accuracy=",(True_Male+True_Female)/(True_Male+True_Female+False_Male+False_Female))
print("\n2.Misclassification Rate=",1-((True_Male+True_Female)/(True_Male+True_Female+False_Male+False_Female)))
print("\n3.i) Precision for Male=",(True_Male)/(True_Male+False_Male))
print("3.ii) Precision for Female=",(True_Female)/(True_Female+False_Female))
print("\n4.i) Recall for Male=",(True_Male)/(True_Male+False_Female))
print("4.ii) Recall for Female=",(True_Female)/(True_Female+False_Male))
print("\n5.i) F1-Score for Male=",(2*True_Male)/(2*True_Male+False_Male+False_Female))
print("5.ii) F1-Score for Female=",(2*True_Female)/(2*True_Female+False_Male+False_Female))
print("===============================================================================================================")








