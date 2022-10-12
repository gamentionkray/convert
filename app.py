import os

def convert_to_webp():
    for root, dirs, files in os.walk("."):
        for file in files:
            if " " in file:
                os.rename(file, file.replace(" ", "_"))
        for file in files:
            if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
                os.system("cwebp -q 80 " + os.path.join(root, file) + " -o " + os.path.join(root, file[:-4] + ".webp"))
            elif file.endswith(".webp"):
                os.system("dwebp " + os.path.join(root, file) + " -o " + os.path.join(root, file[:-5] + ".png"))

if __name__ == "__main__":
    convert_to_webp()