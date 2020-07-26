import os , shutil

dict_extension={

'audio_extensions' :('.mp3', '.m4a', '.wav', 'flac'),
'video_extension' :('.mp4', '.mkv','.MKV','.flv','.mpeg','.3gp'),
'document_extension' :('.doc', '.pdf','.txt','.py'),

}


folder_path= input("Folder Path :")

def file_folder(folder, extension):
    empty_list=[]
    for file in os.listdir(folder):
        for extensions in extension:
            if file.endswith(extensions):
                empty_list.append(file)
    return empty_list

# print(file_folder(folder_path, document_extension))

for extension_type, extension_tuple in dict_extension.items():
    print(file_folder(folder_path, extension_tuple))

