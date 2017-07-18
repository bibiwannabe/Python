import urllib.request
import http.cookiejar


class HtmlDownload(object):
    def download(self, new_url):
        if new_url is None:
            return None
        request = urllib.request.Request(new_url)
        cookie = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
        opener.handle_open["http"][0].set_http_debuglevel(1)  # 设定开启回显
        user_agent = "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 BIDUBrowser/6.x Safari/537.31"
        request.add_header("User-Agent", user_agent)
        cookie = "JSESSIONID=nru8-3hd9KiRZdEGugo1v"  # 设定cookie的内容
        request.add_header("Cookie", cookie)
        respond = opener.open(request)
        respond_code = respond.getcode()
        if respond_code!=200:
            print('\nfailed\n')
        else:
            print('\nsuccessful\n')

        data = respond.read()

        return data

