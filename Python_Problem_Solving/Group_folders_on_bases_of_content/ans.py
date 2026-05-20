from collections import defaultdict
import os

def group_files_by_content(folder_path):
    content_map = defaultdict(list)
    
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
    
            with open(file_path, 'r') as file:
                content = file.read()

            content_map[content].append(file_name)
            
    return list(content_map.values())

folder_path = r"C:\Users\PranavMangal\Desktop\Python my work deep dive\Python_Problem_Solving\Sort_folders_on_bases_of_content\Text_Files"

grouped_files = group_files_by_content(folder_path)

print(grouped_files)