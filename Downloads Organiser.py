import os
import shutil
imagefiletypes = ('.jpg', '.png', 'jpeg', '.gif', '.webp')
videofiletypes = ('.mp4', '.mkv', '.mov', '.avi', '.m4v') 
audiofiletypes = ('mp3','.flac', '.wav', '.aac' ) 
documentfiletypes = ('.doc', '.docx', '.xls', '.xlsx', '.txt', '.html', '.ppt', '.pptx', '.pdf', '.epub')
download_folder = os.scandir(r'C:/Users/matth/Downloads')
for file in download_folder:
	if os.path.isfile(file):
		filename, file_extension = os.path.splitext(file)
		if file_extension in imagefiletypes :
			shutil.copy2(file, r'C:/Users/matth/Pictures')
			os.remove(file)

		elif file_extension in videofiletypes :
			shutil.copy2(file, r'C:/Users/matth/Videos')
			os.remove(file)

		elif file_extension in audiofiletypes :
			shutil.copy2(file, r'C:/Users/matth/Music')
			os.remove(file)

		elif file_extension in documentfiletypes :
			shutil.copy2(file, r'C:/Users/matth/Documents')
			os.remove(file)

		else:
			print('Cannot move',file)

print(' ')
print('Your downloads folder is sorted!')
