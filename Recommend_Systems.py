##### IMPORTS #####
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

df = pd.read_csv("./ecommerce_sample_dataset.csv")

##### FUNCTIONS FOR FINDING DIFFERENT LEVELS OF PRODUCT_CATEGORY_TREE #####
def new_cat1(string):
    ctr = 0
    size = 0
    for i in range(len(string)):
        if(ctr==8):
            break
        if(string[i]=='>'):
            ctr += 1
        size += 1
    return size-3

def new_cat2(string):
    ctr = 0
    size = 0
    for i in range(len(string)):
        if(ctr==6):
            break
        if(string[i]=='>'):
            ctr += 1
        size += 1
    return size-3

def new_cat3(string):
    ctr = 0
    size = 0
    for i in range(len(string)):
        if(ctr==4):
            break
        if(string[i]=='>'):
            ctr += 1
        size += 1
    return size-3

def new_cat4(string):
    ctr = 0
    size = 0
    for i in range(len(string)):
        if(ctr==2):
            break
        if(string[i]=='>'):
            ctr += 1
        size += 1
    return size-3

##### SORTING THE DATABASE AS PER THE DISCOUNTED PRICE #####
sorted_df = df.sort_values('discounted_price')

##### DICTIONARY OF PRODUCTS #####
database = {
    
}

for i in range(20000):
    database[sorted_df.iloc[i][0]] = sorted_df.iloc[i][3:]


##### FUNCTION FOR FINDING THE RECOMMENDATIONS #####
def recommendations(string):
    items = 0
    list_ids = []
    temp = database[string][1]
    temp1 = temp[2:new_cat1(temp)]
    temp2 = temp[2:new_cat2(temp)]
    temp3 = temp[2:new_cat3(temp)]
    temp4 = temp[2:new_cat4(temp)]
    brand = database[string][10]
    
    flag = [0 for i in range(20000)]
    
    for i in range(0, 20000):
        test = sorted_df.iloc[i][4][2:new_cat1(sorted_df.iloc[i][4])]
        
        if(temp1 == test and flag[i]==0 and string!=sorted_df.iloc[i][0]):
            items += 1
            flag[i] = 1
            list_ids.append(sorted_df.iloc[i][0])
        if(items>=5):
            return list_ids
    for i in range(0, 20000):
        test = sorted_df.iloc[i][4][2:new_cat2(sorted_df.iloc[i][4])]
        
        if(temp2 == test and flag[i]==0 and string!=sorted_df.iloc[i][0]):
            items += 1
            flag[i] = 1
            list_ids.append(sorted_df.iloc[i][0])
        if(items>=5):
            return list_ids
    for i in range(0, 20000):
        test = sorted_df.iloc[i][4][2:new_cat3(sorted_df.iloc[i][4])]
        
        if(temp3 == test and flag[i]==0 and string!=sorted_df.iloc[i][0]):
            items += 1
            flag[i] = 1
            list_ids.append(sorted_df.iloc[i][0])
        if(items>=5):
            return list_ids
    for i in range(0, 20000):
        test = sorted_df.iloc[i][4][2:new_cat4(sorted_df.iloc[i][4])]
        
        if(temp4 == test and flag[i]==0 and string!=sorted_df.iloc[i][0]):
            items += 1
            flag[i] = 1
            list_ids.append(sorted_df.iloc[i][0])
        if(items>=5):
            return list_ids
    for i in range(0, 20000):
        test = sorted_df.iloc[i][13]
        
        if(brand == test and flag[i]==0 and string!=sorted_df.iloc[i][0]):
            items += 1
            flag[i] = 1
            list_ids.append(sorted_df.iloc[i][0])
        if(items>=5):
            return list_ids
    for i in range(0, 20000):
        if(flag[i]==0 and string!=sorted_df.iloc[i][0]):
            items += 1
            list_ids.append(sorted_df.iloc[i][0])
        if(items>=5):
            return list_ids

print("\nEnter the Product Unique ID: ")

query_id = str(input())
try:
	r = recommendations(query_id)
	print("\nRecommendations for: " + database[query_id][0] + " : " + query_id + "\n")
	for x in r:
		print(database[x][0]+" : "+x)
except:
	print("Invalid product id!!")
