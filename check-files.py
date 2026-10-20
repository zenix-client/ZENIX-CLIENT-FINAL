import os
import zipfile
import tarfile

for name in os.listdir("."):
    if name.startswith("."):
        continue

    if not os.path.isfile(name):
        continue

    size = os.path.getsize(name)
    print(f"\nFILE: {name} ({size} bytes)")

    if zipfile.is_zipfile(name):
        print("FORMAT: ZIP")
        with zipfile.ZipFile(name) as archive:
            for item in archive.namelist()[:30]:
                print(" ", item)
    elif tarfile.is_tarfile(name):
        print("FORMAT: TAR")
    else:
        with open(name, "rb") as f:
            print("HEADER:", f.read(16).hex())
        print("FORMAT: not ZIP/TAR")
