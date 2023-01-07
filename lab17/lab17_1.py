import os

cwd = os.getcwd()
paths = (
    "/tree/switches/other/cisco",
    "/tree/switches/other/huawei",
    "/tree/routers/other/juniper",
    "/tree/routers/other/huawei",
    "/tree/routers/other/huawei",
    "/tree/cisco/other/cisco",
    "/tree/cisco/other/meraki",
)
for path in paths:
    os.makedirs(root + path, exist_ok=True)

os.rename(root + "/tree/routers/other/juniper", root + "/tree/routers/other/nokia")

with open(root + "/tree/cisco/other/readme.txt", 'w') as readme:
    readme.write("Don't forget to save all configurations!")

os.replace(root + "/tree/cisco/other/readme.txt", root + "/tree/cisco/other/meraki/readme1.txt")

with open(root + "/tree/cisco/other/meraki/readme1.txt") as readme1:
    print(readme1.read())

os.makedirs(root + "/tree/switches/other/juniper", exist_ok=True)

for dir_path, dir_names, filenames in os.walk(root + '/tree'):
    for dir_name in dir_names:
        print("Directory:", os.path.join(dir_path, dir_name))
    for filename in filenames:
        print("File:     ", os.path.join(dir_path, filename))

os.rmdir(root + "/tree/routers/other/nokia")