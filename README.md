# CreateURealmsTileImages
This utility creates all the images you need for creating URealms tiles.

This script requires you to have Gimp 2.8 installed. To use this script execute the following command line commands:

cd "the file path for this script"
  
Set var=C:\Users\sean-\Desktop\urealms\Tiles\example.png
"C:\Program Files\GIMP 2\bin\gimp-2.8.exe" gimp -idf --batch-interpreter=python-fu-eval -b "import sys; sys.path =['.'] + sys.path; import batch_CreateURealmsTileImages; batch_CreateURealmsTileImages.run('%var%')" -b "pdb.gimp_quit(1)"


Once run, a folder with the same name as the input image will be put in the same folder of the image. All newly generated files will appear there.
