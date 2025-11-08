import pandas as pd
import os 

# Create sample DF with column names
data={'Name':['A','B','C'],'Age':[25,30,35],'City':['Boston','Austin','LA']}

#Conveert to Dataframe
df=pd.DataFrame(data)



# Ensure the 'data' directory exists at the root level
data_dir='data'
os.makedirs(data_dir,exist_ok=True) #It will not ovverwrite if already exists

# Define file path
file_path=os.path.join(data_dir,'sample_data.csv')

# save dataFrame to csv file 
df.to_csv(file_path,index=False)

print(f"csv file has been saved at: {file_path}")