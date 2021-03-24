import argparse
import requests
import pprint

def main():

    api_url = "https://script.google.com/macros/s/AKfycbw1LNap_3dkdCQv-lmT__r_4ZCicSo5vNNQJ4Ly_h1Yag2twD2m3jKppr7GuV6BjyGkpw/exec"
    # headers = {"Authorization": "Bearer ya29.***************************************************************************************************************"}  #google翻訳APIで, 認証が必要な場合

    parser = argparse.ArgumentParser()
    parser.add_argument("-input", type=str, required=True)
    args = parser.parse_args()

    input = ""
    with open(args.input, 'r',encoding="utf-8") as f:
        for line in f:
            print(line)
            line = line.strip()
            input += line

    params = {
        'text': "\"" + input + "\"",
        'source': 'en',
        'target': 'ja'
    }

    # r_post = requests.post(api_url, headers=headers, data=params)
    r_post = requests.post(api_url, data=params)
    print(r_post.text)


if __name__ == "__main__":
    main()
