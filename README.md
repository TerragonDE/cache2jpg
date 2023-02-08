# cache2jpg
Batch-rename Chromebrowser cache images to .jpg files
![Original Chrome Cache Folder](https://github.com/TerragonDE/cache2jpg/blob/main/csm_Bildschirmfoto_2021-11-26_um_18.46.19_c0ea8220a1.png?raw=true)

## How-to
1. Download file "cache2jpg.py"
2. Place "cache2jpg.py" in Cache folder

On Windows, the regular Path for the Chrome Browser Cache is:
C:\Users\ ###Username### \AppData\Local\Google\Chrome\User Data\Default\Cache
Most cached files are named like "f_007e24" with random numbers.

3. Run the file from command line: python3 "cache2jpg.py" 
4. Files will be renamed and you can open JPG files directly from Windows Explorer 

![Original Chrome Cache Folder](https://github.com/TerragonDE/cache2jpg/blob/main/csm_Bildschirmfoto_2021-11-26_um_18.55.37_1c11d97ef0.png?raw=true)
![Original Chrome Cache Folder](https://github.com/TerragonDE/cache2jpg/blob/main/csm_Bildschirmfoto_2021-11-26_um_18.58.05_812b66ff42.png?raw=true)


## Tweaks
You can change the filter for the filesize (min and max) in the script by changing the values (40000 and 150000).
