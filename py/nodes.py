import re
import shutil
import os
import hashlib
import json
import glob
import mimetypes
import random
import folder_paths

class LoadFile:
    '''
    文件加载器，文件上传到输入目录
    '''
    CATEGORY = "work_utils/input"

    # 常量，使用本地文件
    USE_LOCAL_FILE = "USE_LOCAL_FILE"

    @classmethod
    def INPUT_TYPES(s):
        input_dir = folder_paths.get_input_directory()
        files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
        return {
            "required": {
                "file": ([s.USE_LOCAL_FILE] + sorted(files), {"file_upload": True, "accept": "*"}),
            },
            "optional": {
                "local_file": ("STRING", {"multiline": True, "default": ""}),
            },
        }

    RETURN_TYPES = ("FILE",)

    FUNCTION = "load_file"

    def load_file(self, file, local_file):
        if file == LoadFile.USE_LOCAL_FILE:
            file_path = local_file
        else:
            file_path = folder_paths.get_annotated_filepath(file)
        if not os.path.isfile(file_path):
            raise Exception(f"非法文件:{file_path}")
        return (file_path,)

    @classmethod
    def IS_CHANGED(s, file):
        if file == s.USE_LOCAL_FILE:
            return s.USE_LOCAL_FILE
        file_path = folder_paths.get_annotated_filepath(file)
        m = hashlib.sha256()
        with open(file_path, 'rb') as f:
            m.update(f.read())
        return m.digest().hex()

    @classmethod
    def VALIDATE_INPUTS(s, file):
        if file == LoadFile.USE_LOCAL_FILE:
            return True
        if not folder_paths.exists_annotated_filepath(file):
            return f"非法文件:{file}"
        return True


class UnzipFile:
    '''
    解压文件
    '''
    CATEGORY = "work_utils/handler"

    # 支持的压缩包类型
    SUPPORT_TYPES = ("zip",)

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "file": ("FILE",),
            },
            "optional": {
                "output_dir": ("STRING", {"multiline": True, "default": ""}),
            }
        }

    RETURN_TYPES = ("DIR",)

    FUNCTION = "unzip"

    def unzip(self, file, output_dir):
        if not os.path.isfile(file) or not file.split('.')[-1] in UnzipFile.SUPPORT_TYPES:
            raise Exception(f"文件不存在或者压缩类型不支持:{file}")
        if len(output_dir) == 0:
            output_dir = folder_paths.get_input_directory()
        unzip_dir = os.path.join(output_dir, os.path.splitext(os.path.basename(file))[0])
        shutil.unpack_archive(file, unzip_dir)
        return (unzip_dir,)

    @classmethod
    def IS_CHANGED(s, file, ):
        return file


class ListDir:
    CATEGORY = "work_utils/handler"

    @classmethod
    def INPUT_TYPES(s):
        # 参数可以加一些exclude之类的，或者指定后缀
        return {
            "required": {
                "dir": ("DIR",),
                "glob_parttern": ("STRING", {"default": "**/*"})
            },
        }

    RETURN_TYPES = ("FILES", "JSON",)

    FUNCTION = "list_dir"

    def list_dir(self, dir, glob_parttern):
        if not os.path.isdir(dir):
            raise Exception(f"文件夹不存在:{dir}")
        data = glob.glob(os.path.join(dir, glob_parttern), recursive=True)
        data = [os.path.join(dir, x) for x in data]
        # FILES, JSON
        return (data, data)

    @classmethod
    def IS_CHANGED(s, dir, glob_parttern):
        return dir


NODE_CLASS_MAPPINGS = {
    "LoadFile": LoadFile,
    "UnzipFile": UnzipFile,
    "ListDir": ListDir,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadFile": "LoadFile",
    "UnzipFile": "UnzipFile",
    "ListDir": "ListDir",
}
