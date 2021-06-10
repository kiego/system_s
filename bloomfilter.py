import hashlib
import glob

bfindex = bytearray([0] * 64)
file_data = []

def bloomfilter(keys):
    for key_value in keys:
        md5 = int(hashlib.md5(key_value).hexdigest(),16) % 64
        sha256 = int(hashlib.sha256(key_value).hexdigest(),16)% 64
        sha512 = int(hashlib.sha512(key_value).hexdigest(),16) % 64
        bfindex[md5] = 1
        bfindex[sha256] = 1
        bfindex[sha512] = 12

    return bfindex


def check_file_count():
    # ファイル一覧取得
    download_files = glob.glob(f'database_file/*.dat')
    # if len(download_files) >= 10:
    return download_files
    # else:
    #     print("ファイル数が規定に達していません")

def input_value(file_path):
    for num in file_path:
        with open(num,'rb') as f:
            file_data.append(f.read())
        return file_data


if __name__ == '__main__':


    file_path = check_file_count()
    keys = input_value(file_path)
    bloomfilter(keys)

    