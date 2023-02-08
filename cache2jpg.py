import os

for count, filename in enumerate(os.listdir()):
    dst =filename + ".jpg"
    src =filename
    dst =dst
    if os.path.getsize(filename) > 40000 and os.path.getsize(filename) < 150000 and filename[-1].isnumeric(): 
        os.rename(src, dst)
