import os 


fnames = [f"{str(i).zfill(3)}_sales.csv" for i in range(1, 25)]
full_path = []
for file in fnames:
    whole_path = os.path.join(os.getcwd(), file)
    full_path.append(whole_path)

print(full_path)