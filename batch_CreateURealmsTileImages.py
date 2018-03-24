#!/usr/bin/env python

import os
from gimpfu import *

def run(inputFileNameAndPath):

	##########################################################
	#Instructions
	##########################################################

	#To run this script:
	#Open cmd.exe
	#Run cd <directory where this script is>
	#Paste the code below and press enter

	#"C:\Program Files\GIMP 2\bin\gimp-2.8.exe" gimp -idf --batch-interpreter=python-fu-eval -b "import sys; sys.path =['.'] + sys.path; import batch_CreateURealmsTileImages; batch_CreateURealmsTileImages.run('<insert file path and name here>')" -b "pdb.gimp_quit(1)"


	##########################################################
	#Part 0 - Setup
	##########################################################
	
	#Vars from Input File	
	#inputFileNameAndPath = 'C:\Users\Public\GimpSandbox\example.png'
	filePath = os.path.dirname(inputFileNameAndPath)
	fileName = os.path.basename(inputFileNameAndPath)
	fileNameNoExt = os.path.splitext(os.path.basename(fileName))[0]
	outputFolder = filePath + '\\' + fileNameNoExt 
	outputFileName = fileNameNoExt
	inputFile = inputFileNameAndPath
	
	#Create output folder
	if not os.path.exists(outputFolder):
		os.makedirs(outputFolder)
	
	#Get current directory to set asset paths
	currentDirectory = os.getcwd()
	
	#Set images assets path
	imageAssetPath = currentDirectory + "\image_Assets"
	
	imageAssetPath_Blinded = imageAssetPath+'\statuseffect_blinded.png'
	imageAssetPath_Burning = imageAssetPath+'\statuseffect_burning.png'
	imageAssetPath_Charmed = imageAssetPath+'\statuseffect_charmed.png'
	imageAssetPath_Defeated = imageAssetPath+'\statuseffect_defeated.png'
	imageAssetPath_Frozen =imageAssetPath+'\statuseffect_frozen.png'
	imageAssetPath_Poisoned = imageAssetPath+'\statuseffect_poisoned.png'
	imageAssetPath_Silenced =imageAssetPath+'\statuseffect_silenced.png'
	imageAssetPath_Stunned = imageAssetPath+'\statuseffect_stunned.png'

	##########################################################
	#Part 1 - Get the circle image
	##########################################################
	#Load File
	image_Input = pdb.file_png_load(inputFile, inputFile)

	#Scale file to correct size
	pdb.gimp_image_scale(image_Input, 284, 284)

	#Get ellipse selection (circle)
	pdb.gimp_image_select_ellipse(image_Input, 2, 0, 0, 286, 286)

	#Copy circle
	pdb.gimp_edit_copy(image_Input.layers[0])

	#Paste Circle to new image_Input
	newImage = pdb.gimp_edit_paste_as_new()

	#Resize image_Input
	pdb.gimp_layer_resize(newImage.layers[0], 512, 512, 0, 0)

	#Save circle as new image_Input
	outputFile = "C:\Users\Public\GimpSandbox\saved_imageAsCircle.png"
	pdb.file_png_save_defaults(newImage, newImage.active_layer, outputFile, outputFile)

	##########################################################
	#Part 2 - Put Circle image on template
	##########################################################

	#Create new image
	image_New = gimp.Image(512, 512)

	#Adds tile template to image
	File_template = "C:\Users\Public\GimpSandbox\Assets\BlankTileTemplate.png"
	layer_Template = pdb.gimp_file_load_layer(image_New, File_template)
	pdb.gimp_image_insert_layer(image_New, layer_Template, None, 0)
	#layer = pdb.gimp_image_merge_down(image_New, layer_Template, 1)


	#Adds circle image to image
	File_circle = "C:\Users\Public\GimpSandbox\saved_imageAsCircle.png"
	layer_Circle = pdb.gimp_file_load_layer(image_New, File_circle)
	pdb.gimp_image_insert_layer(image_New, layer_Circle, None, 0)
	layer = pdb.gimp_image_merge_down(image_New, layer_Circle, 1)

	#Saves base new image
	File_Base = outputFolder + "\saved_BaseTile.png"
	pdb.file_png_save_defaults(image_New, image_New.active_layer, File_Base, File_Base)

	##########################################################
	#Part 3 - Create Status Effect images
	##########################################################

	##########################################################
	#Blind
	##########################################################
	
	status = 'Blind'
	filepath = imageAssetPath_Blinded

	#Create new image
	image_New = gimp.Image(512, 512)

	#Adds tile template to image
	layer_Base = pdb.gimp_file_load_layer(image_New, File_Base)
	pdb.gimp_image_insert_layer(image_New, layer_Base, None, 0)

	#Adds circle image to image
	layer_Circle = pdb.gimp_file_load_layer(image_New, filepath)
	pdb.gimp_image_insert_layer(image_New, layer_Circle, None, 0)
	layer = pdb.gimp_image_merge_down(image_New, layer_Circle, 1)

	#Saves base new image
	File_Base = outputFolder + "\\" + outputFileName + "_" + status + ".png"
	pdb.file_png_save_defaults(image_New, image_New.active_layer, File_Base, File_Base)
	
	##########################################################
	#Burning
	##########################################################
	status =  'Burning'
	filepath = imageAssetPath_Burning

	#Create new image
	image_New = gimp.Image(512, 512)

	#Adds tile template to image
	layer_Base = pdb.gimp_file_load_layer(image_New, File_Base)
	pdb.gimp_image_insert_layer(image_New, layer_Base, None, 0)

	#Adds circle image to image
	layer_Circle = pdb.gimp_file_load_layer(image_New, filepath)
	pdb.gimp_image_insert_layer(image_New, layer_Circle, None, 0)
	layer = pdb.gimp_image_merge_down(image_New, layer_Circle, 1)

	#Saves base new image
	File_Base = outputFolder + "\\" + outputFileName + "_" + status + ".png"
	pdb.file_png_save_defaults(image_New, image_New.active_layer, File_Base, File_Base)
	
	##########################################################
	#Charmed
	##########################################################	
	status = 'Charmed'
	filepath = imageAssetPath_Charmed

	#Create new image
	image_New = gimp.Image(512, 512)

	#Adds tile template to image
	layer_Base = pdb.gimp_file_load_layer(image_New, File_Base)
	pdb.gimp_image_insert_layer(image_New, layer_Base, None, 0)

	#Adds circle image to image
	layer_Circle = pdb.gimp_file_load_layer(image_New, filepath)
	pdb.gimp_image_insert_layer(image_New, layer_Circle, None, 0)
	layer = pdb.gimp_image_merge_down(image_New, layer_Circle, 1)

	#Saves base new image
	File_Base = outputFolder + "\\" + outputFileName + "_" + status + ".png"
	pdb.file_png_save_defaults(image_New, image_New.active_layer, File_Base, File_Base)
	
	##########################################################
	#Defeated
	##########################################################	
	status = 'Defeated'
	filepath = imageAssetPath_Defeated

	#Create new image
	image_New = gimp.Image(512, 512)

	#Adds tile template to image
	layer_Base = pdb.gimp_file_load_layer(image_New, File_Base)
	pdb.gimp_image_insert_layer(image_New, layer_Base, None, 0)

	#Adds circle image to image
	layer_Circle = pdb.gimp_file_load_layer(image_New, filepath)
	pdb.gimp_image_insert_layer(image_New, layer_Circle, None, 0)
	layer = pdb.gimp_image_merge_down(image_New, layer_Circle, 1)

	#Saves base new image
	File_Base = outputFolder + "\\" + outputFileName + "_" + status + ".png"
	pdb.file_png_save_defaults(image_New, image_New.active_layer, File_Base, File_Base)

	##########################################################
	#Frozen
	##########################################################	
	status = 'Frozen'
	filepath = imageAssetPath_Frozen
	
	#Create new image
	image_New = gimp.Image(512, 512)

	#Adds tile template to image
	layer_Base = pdb.gimp_file_load_layer(image_New, File_Base)
	pdb.gimp_image_insert_layer(image_New, layer_Base, None, 0)

	#Adds circle image to image
	layer_Circle = pdb.gimp_file_load_layer(image_New, filepath)
	pdb.gimp_image_insert_layer(image_New, layer_Circle, None, 0)
	layer = pdb.gimp_image_merge_down(image_New, layer_Circle, 1)

	#Saves base new image
	File_Base = outputFolder + "\\" + outputFileName + "_" + status + ".png"
	pdb.file_png_save_defaults(image_New, image_New.active_layer, File_Base, File_Base)

	##########################################################
	#Poisoned
	##########################################################	
	status = 'Poisoned'
	filepath = imageAssetPath_Poisoned
	
	#Create new image
	image_New = gimp.Image(512, 512)

	#Adds tile template to image
	layer_Base = pdb.gimp_file_load_layer(image_New, File_Base)
	pdb.gimp_image_insert_layer(image_New, layer_Base, None, 0)

	#Adds circle image to image
	layer_Circle = pdb.gimp_file_load_layer(image_New, filepath)
	pdb.gimp_image_insert_layer(image_New, layer_Circle, None, 0)
	layer = pdb.gimp_image_merge_down(image_New, layer_Circle, 1)

	#Saves base new image
	File_Base = outputFolder + "\\" + outputFileName + "_" + status + ".png"
	pdb.file_png_save_defaults(image_New, image_New.active_layer, File_Base, File_Base)

	##########################################################
	#Silenced
	##########################################################	
	status = 'Silenced'
	filepath = imageAssetPath_Silenced
	
	#Create new image
	image_New = gimp.Image(512, 512)

	#Adds tile template to image
	layer_Base = pdb.gimp_file_load_layer(image_New, File_Base)
	pdb.gimp_image_insert_layer(image_New, layer_Base, None, 0)

	#Adds circle image to image
	layer_Circle = pdb.gimp_file_load_layer(image_New, filepath)
	pdb.gimp_image_insert_layer(image_New, layer_Circle, None, 0)
	layer = pdb.gimp_image_merge_down(image_New, layer_Circle, 1)

	#Saves base new image
	File_Base = outputFolder + "\\" + outputFileName + "_" + status + ".png"
	pdb.file_png_save_defaults(image_New, image_New.active_layer, File_Base, File_Base)
	
	##########################################################
	#Stunned
	##########################################################	

	status = 'Stunned'
	filepath = imageAssetPath_Stunned
	
	#Create new image
	image_New = gimp.Image(512, 512)

	#Adds tile template to image
	layer_Base = pdb.gimp_file_load_layer(image_New, File_Base)
	pdb.gimp_image_insert_layer(image_New, layer_Base, None, 0)

	#Adds circle image to image
	layer_Circle = pdb.gimp_file_load_layer(image_New, filepath)
	pdb.gimp_image_insert_layer(image_New, layer_Circle, None, 0)
	layer = pdb.gimp_image_merge_down(image_New, layer_Circle, 1)

	#Saves base new image
	File_Base = outputFolder + "\\" + outputFileName + "_" + status + ".png"
	pdb.file_png_save_defaults(image_New, image_New.active_layer, File_Base, File_Base)
	
	##########################################################
	#Clean up
	##########################################################	
	os.remove(outputFile) 

	


