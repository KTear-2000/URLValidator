import requests

def save_status_200_urls(url_file, output_file, timeout=5):
    try:
        # 打开URL文件
        with open(url_file, 'r', encoding='utf-8') as f_urls:
            # 打开输出文件
            with open(output_file, 'w', encoding='utf-8') as f_output:
                # 逐行读取URL
                for url in f_urls:
                    url = url.strip()  # 去除换行符和空白字符
                    try:
                        # 发送HTTP HEAD请求获取网页头信息，这里仅获取状态码，不下载页面内容
                        response = requests.head(url, timeout=timeout)

                        # 打印URL的状态码
                        print(f"URL: {url}, 状态码: {response.status_code}")

                        # 如果状态码为200，则将URL写入输出文件
                        if response.status_code == 200:
                            f_output.write(url + '\n')
                    except requests.exceptions.Timeout:
                        print(f"URL: {url}, 连接超时")
                    except Exception as e:
                        print(f"URL: {url}, 发生异常：{e}")

    except Exception as e:
        print(f"发生异常：{e}")


# URL文件路径
url_file = "urls.txt"
# 输出文件路径
output_file = "status_200_urls.txt"

# 调用函数获取状态码为200的URL，并写入文本文件
save_status_200_urls(url_file, output_file)
