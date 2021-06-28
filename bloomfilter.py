import hashlib
import glob



def hash_value(keys, bfindex, flag):
    for key_value in keys:
        md5 = int(hashlib.md5(key_value).hexdigest(),16) % 64
        sha256 = int(hashlib.sha256(key_value).hexdigest(),16)% 64
        sha512 = int(hashlib.sha512(key_value).hexdigest(),16) % 64
        
        if flag:
            bfindex[md5] = 1
            bfindex[sha256] = 1
            bfindex[sha512] = 1
        else:
            search(md5, sha256, sha512)

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

def search(md5,sha256,sha512):
    keyword_value = [md5,sha256,sha512]
    for bit in keyword_value:
        if bfindex[bit] == 0:
            print("検索したキーワードはありません")
            break
        else:
            print("aru")
            continue


def input_keyword():
    key = input("enter your keyword: ")
    word_list = key.split(" ")
    keyword_list = [x.encode() for x in word_list]

    return keyword_list


if __name__ == "__main__":
    bfindex = bytearray([0] * 64)
    file_data = []
    flag = True

    file_path = check_file_count()
    keys = input_value(file_path)
    bfindex = hash_value(keys, bfindex, flag)
    keyword = input_keyword()
    flag = False
    hash_value(keyword, bfindex, flag)


    