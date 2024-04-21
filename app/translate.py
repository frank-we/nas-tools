from app.utils import RequestUtils, ExceptionUtils
from app.utils.commons import singleton
from config import Config
import log


@singleton
class Translate:
    _domain = None
    _token = None

    def __init__(self):
        self.init_config()

    def init_config(self):
        translate = Config().get_config('translate')
        if translate:
            self._domain = translate.get("domain")
            self._token = translate.get("token")

    def get_tranlation(self,
                       text,
                       source_lang,
                       target_lang="ZH",
                       domain='',
                       token=''):
        _domain = self._domain
        _token = self._token
        if domain:
            _domain = domain
            _token = token
        if not self._domain or not self._token:
            log.error("【Translate】未配置DeepLX API！")
            return False, "未配置翻译服务"
        success = False
        ret_msg = ""
        if (_domain):
            data = {
                "source_lang": source_lang,
                "target_lang": target_lang,
                "text": text
            }

            try:
                res = RequestUtils(
                    headers={
                        "Authorization": "Bearer %s" % _token,
                        'Content-Type': 'application/json'
                    }).post(url=_domain, json=data)

                if not res or res.status_code != 200:
                    log.error("【Translate】调用DeepLX API失败！")
                    ret_msg = "调用DeepLX API失败"
                else:
                    if (res.text):
                        ret_msg = res.json().get("data")
                        log.info("【Translate】'%s' 翻译为 '%s'" % (text, ret_msg))
                        success = True
            except Exception as e:
                ExceptionUtils.exception_traceback(e)
                log.error("【Translate】连接翻译服务出错：" + str(e))
                ret_msg = "连接翻译服务出错：%s" % str(e)
        if success:
            return True, ret_msg
        else:
            return False, ret_msg

    def text_tranlation(self, domain, token):
        return self.get_tranlation(source_lang='EN',
                                   target_lang="ZH",
                                   text='hello world',
                                   domain=domain,
                                   token=token)
