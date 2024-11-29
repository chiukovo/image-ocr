import ddddocr
import requests
import sys
import json

def ocr_from_url(url):
    # 下載圖片
    response = requests.get(url)
    if response.status_code == 200:
        image_data = response.content
        # 使用 ddddocr 進行文字辨識
        ocr = ddddocr.DdddOcr(show_ad=False)
        result = ocr.classification(image_data)
        return result
    else:
        raise Exception(f"無法下載圖片，HTTP 狀態碼: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "用法: python test.py <圖片URL>"}))
        sys.exit(1)

    image_url = sys.argv[1]
    try:
        result = ocr_from_url(image_url)
        # 將結果封裝成 JSON 格式
        output = {
            "status": "success",
            "data": {
                "url": image_url,
                "ocr_result": result
            }
        }
        print(json.dumps(output, ensure_ascii=False, indent=4))
    except Exception as e:
        # 將錯誤訊息封裝成 JSON 格式
        error_output = {
            "status": "error",
            "message": str(e)
        }
        print(json.dumps(error_output, ensure_ascii=False, indent=4))
