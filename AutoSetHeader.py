def AutoSetHeader():
    rawHeader = '''GET /test HTTP/1.1
    Host: xxx.xxx.com
    Accept: application/json, text/plain, */*
    Sec-Ch-Ua-Mobile: ?0
    User-Agent: xxxxxx
    Origin: https://xxx.xxx.com
    Sec-Fetch-Site: same-site
    Sec-Fetch-Mode: cors
    Sec-Fetch-Dest: empty
    Referer: https://xxx.xxx.com/
    Accept-Encoding: gzip, deflate
    Accept-Language: zh-CN,zh;q=0.9
    Connection: close

    '''

    splitHeaderA = rawHeader.strip().split("\n")
    splitHeaderB = splitHeaderA[1:]
    HeaderInfo = {}
    for i in splitHeaderB:
        listHeader = i.strip().split(":",1)
        HeaderInfo[listHeader[0]] = listHeader[1].strip()

    return HeaderInfo

print(AutoSetHeader())
