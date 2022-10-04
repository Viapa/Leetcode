def TinyURL(url):
    """
    设计一个可以简化加密网址的函数，包含加密encode和解密decode两个过程
    当输入一个url时，先通过encode将网址变短加密，然后再通过decode将短网址还原
    :param url: 输入的网址 [str]
    :return: 返回加密网址 [str] 和 解密网址 [str]
    """
    def encode(longUrl):
        tmp_url = longUrl.replace("https", "http")
        encodeUrl = tmp_url.replace(".com/", "?")
        return encodeUrl

    def decode(shortUrl):
        tmp_url = shortUrl.replace("http", "https")
        decodeUrl = tmp_url.replace("?", ".com/")
        return decodeUrl

    encode_url = encode(url)
    decode_url = decode(encode_url)

    assert len(encode_url) < len(url), "加密失败, 加密网址必须短于原网址长度!"
    assert decode_url == url, "解密失败, 解密网址必须与原网址相同!"
    return encode_url, decode_url


# 测试
if __name__ == "__main__":
    url = "https://leetcode.com/problems/design-tinyurl"
    encode_url, decode_url = TinyURL(url)
    print(f"加密成功!, 输入原网址为：{url}")
    print(f"经过加密的网址为：{encode_url}")
    print(f"经过解密的网址为：{decode_url}")