# CreateURealmsTileImages
This utility creates all the images you need for creating URealms tiles.

This script requires you to have Gimp 2.8 installed. To use this script execute the following command line commands:

cd <the file path for this script>
  
"C:\Program Files\GIMP 2\bin\gimp-2.8.exe" gimp -idf --batch-interpreter=python-fu-eval -b "import sys; sys.path =['.'] + sys.path; import batch_CreateURealmsTileImages; batch_CreateURealmsTileImages.run('<insert file path and name here>')" -b "pdb.gimp_quit(1)"
