def TinyURL(url):
    """
    设计一个可以简化加密网址的函数，包含加密encode和解密decode两个过程
    当输入一个url时，先通过encode将网址变短加密，然后再通过decode将短网址还原
    :param url: 输入的网址 [str]
    :return: 返回加密网址 [str] 和 解密网址 [str]
    """
    # 思路是基于ascii码值进行处理后还原
    def encode(longUrl):
        asc_ls = []
        for c in longUrl:
            ascii_c = str(ord(c))
            asc_ls.append(ascii_c)
        encodeUrl = ",".join(asc_ls)
        return encodeUrl

    def decode(shortUrl):
        res_ls = []
        asc_ls = shortUrl.split(",")
        for num in asc_ls:
            c = chr(int(num))
            res_ls.append(c)
        decodeUrl = "".join(res_ls)
        return decodeUrl

    encode_url = encode(url)
    decode_url = decode(encode_url)

    assert decode_url == url, "解密失败, 解密网址必须与原网址相同!"
    return encode_url, decode_url


# 测试
if __name__ == "__main__":
    url = "http://www.leetcode.com/faq/?id=10"
    encode_url, decode_url = TinyURL(url)
    print(f"加密成功!, 输入原网址为：'{url}'")
    print(f"经过加密的网址为：'{encode_url}'")
    print(f"经过解密的网址为：'{decode_url}'")