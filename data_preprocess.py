import zipfile
from glob import glob
import os
import shutil

for zip_file in glob(os.path.join("jingjing", "id*.zip")):
    print(zip_file)
    z_f = zipfile.ZipFile(zip_file, "r")
    for fileM in z_f.namelist():
        print(fileM)
        z_f.extract(fileM, "D:\programm\workspace\zijian\jingjing_dataset_preprocess/all_file")
    z_f.close()

for dir in glob(os.path.join("D:\programm\workspace\zijian\jingjing_dataset_preprocess/all_file", "*")):
    for audio_path in glob(os.path.join(dir, "*.wav")):
        audio_name = os.path.basename(audio_path)
        if audio_name.startswith("00"):
            shutil.copyfile(audio_path, os.path.join("Wave", audio_name))
        pass
    pass