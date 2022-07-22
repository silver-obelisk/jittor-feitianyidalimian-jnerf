import os
import glob
import shutil
os.system("python tools/run_net.py --config-file ./projects/ngp/configs/ngp_Coffee.py --task test")
filePath="./logs/Coffee/test"
newFilePath="./result"
filename=os.listdir(filePath)
len1=len(filename)
for i in filename:
  for a in range(len1):
    if i ==f"Coffee_r_{a}.png":
      shutil.copy(filePath+'/'+i,newFilePath+'/'+i)
    
os.system("python tools/run_net.py --config-file ./projects/ngp/configs/ngp_Scarf.py --task test")
filePath="./logs/Scarf/test"
newFilePath="./result"
filename=os.listdir(filePath)
len1=len(filename)
for i in filename:
  for a in range(len1):
    if i ==f"Scarf_r_{a}.png":
      shutil.copy(filePath+'/'+i,newFilePath+'/'+i)
      
os.system("python tools/run_net.py --config-file ./projects/ngp/configs/ngp_Easyship.py --task test")
filePath="./logs/Easyship/test"
newFilePath="./result"
filename=os.listdir(filePath)
len1=len(filename)
for i in filename:
  for a in range(len1):
    if i ==f"Easyship_r_{a}.png":
      shutil.copy(filePath+'/'+i,newFilePath+'/'+i)
      
os.system("python tools/run_net.py --config-file ./projects/ngp/configs/ngp_Scar.py --task test")
filePath="./logs/Scar/test"
newFilePath="./result"
filename=os.listdir(filePath)
len1=len(filename)
for i in filename:
  for a in range(len1):
    if i ==f"Scar_r_{a}.png":
      shutil.copy(filePath+'/'+i,newFilePath+'/'+i)
      
os.system("python tools/run_net.py --config-file ./projects/ngp/configs/ngp_Car.py --task test")
filePath="./logs/Car/test"
newFilePath="./result"
filename=os.listdir(filePath)
len1=len(filename)
for i in filename:
  for a in range(len1):
    if i ==f"Car_r_{a}.png":
      shutil.copy(filePath+'/'+i,newFilePath+'/'+i)