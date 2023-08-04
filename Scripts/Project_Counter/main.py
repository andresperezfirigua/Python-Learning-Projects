import os

os.chdir('../../')

dir_list = [name for name in os.listdir(f'.') if os.path.isdir(f'{name}')]

count_dict = {name: len(os.listdir(f'{name}')) for name in dir_list if 'Apps' in name or 'Script' in name or 'Web' in name}

print(count_dict)

# Pending review

# for key, value in count_dict.items():
#     os.rename(key, f'{key}({value} projects)')
