# Aapt

Android Asset Packaging Tool 2 for Python3

## Install

`pip3 install aapt2`

## Example

```python
from aapt2 import aapt

help = aapt.aapt('--help')
print(help)

ls = aapt.ls('./xxx.apk')
print(ls)

apk_info = aapt.get_apk_info('./xxx.apk')
print(apk_info)

# save icon
apk_info = aapt.get_apk_and_icon('./xxx.apk')

if 'png' in apk_info['icon_suffix']:
    from PIL import Image
    import io
    byte_stream = io.BytesIO(apk_info['icon_byte_value'])
    img = Image.open(byte_stream)
    img.save('./1.png')

# upload file

requests.post(url, files={'file': apk_info['icon_byte_value']})

# The xml suffix is connected with adaptive icon presentation
# introduced in Android 8.0
if 'xml' in apk_info['icon_suffix']:
    with open('app_icon.xml', 'wb') as appIcon:
        appIcon.write(apk_info['icon_byte_value'])

# If you are intrested to collect png image, or any other file
# please use:

aapt.ls('./xxx.apk')

# To extract the file from pkg you can use:
# if destination is None, the file will not be saved but byte presentation will
# be return as:
#
# {
#   'name': 'app_icon.png',
#   'byte_value': xff\xff\xff
# }
#
# in other way it will be save in destination folder as"
#
#      destination/app_icon.png
#
extracted_file = aapt.extract_file_from_apk('./xxx.apk', 'res/drawable-hdpi-v4/app_icon.png', destination)
print(extracted_file)


```

## API

* aapt(args)
* ls(file_path)
* dump(file_path, values)
* packagecmd(file_path, command)
* remove(file_path, files)
* add(file_path, files)
* crunch(resource, output_folder)
* single_crunch(input_file, output_file):
* version()
* get_apk_info(file_path)
* extract_file_from_apk('./xxx.apk', file_of_interest, destination)
