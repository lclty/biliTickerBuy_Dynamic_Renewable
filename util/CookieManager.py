from loguru import logger
from playwright.sync_api import sync_playwright
from util.KVDatabase import KVDatabase

class CookieManager:
    def __init__(self, config_file_path=None, cookies=None):
        self.db = KVDatabase(config_file_path)
        if cookies is not None:
            self.db.insert("cookie", cookies)
    
    @logger.catch
    def _login_and_save_cookies(
        self, login_url="https://show.bilibili.com/platform/home.html"
    ):
        logger.info("启动浏览器中，第一次启动会比较慢，请使用在浏览器登录")
        
        # 定义浏览器启动优先级：先尝试 Chrome，再尝试 Edge
        BROWSER_PRIORITY = ["chrome", "msedge"]
        browser = None
        
        with sync_playwright() as p:
            # 尝试按优先级启动浏览器
            for browser_channel in BROWSER_PRIORITY:
                try:
                    browser = p.chromium.launch(
                        channel=browser_channel,
                        headless=False,
                        timeout=120000  # 120秒超时
                    )
                    logger.info(f"成功启动 {browser_channel} 浏览器")
                    break  # 成功启动则跳出循环
                except Exception as e:
                    logger.warning(f"无法启动 {browser_channel} 浏览器: {e}")
            
            # 检查是否成功启动了浏览器
            if not browser:
                error_msg = "无法启动任何浏览器！请确保已安装 Chrome 或 Edge 浏览器"
                logger.error(error_msg)
                raise RuntimeError(error_msg)
            
            try:
                page = browser.new_page()
                page.goto(login_url)
                page.click(".nav-header-register")
                logger.info("浏览器启动, 进行登录.")
                
                # 增加登录等待时间和详细日志
                logger.info("等待用户登录...")
                page.wait_for_selector(".user-center-link", timeout=300000, state="attached")  # 5分钟超时
                logger.info("检测到用户已登录")
                
                cookies = page.context.cookies()
                self.db.insert("cookie", cookies)
                logger.info("登录成功, 浏览器退出.")
                return self.db.get("cookie")
            except Exception as e:
                logger.error(f"登录过程中出错: {e}")
                raise
            finally:
                # 确保无论如何都尝试关闭浏览器
                if browser:
                    browser.close()

    def get_cookies(self, force=False):
        if force:
            return self.db.get("cookie")
        if not self.db.contains("cookie"):
            return self._login_and_save_cookies()
        else:
            return self.db.get("cookie")

    def have_cookies(self):
        return self.db.contains("cookie")

    def get_cookies_str(self):
        cookies = self.get_cookies()
        cookies_str = ""
        assert cookies
        for cookie in cookies:
            cookies_str += cookie["name"] + "=" + cookie["value"] + "; "
        return cookies_str

    def get_cookies_value(self, name):
        cookies = self.get_cookies()
        assert cookies
        for cookie in cookies:
            if cookie["name"] == name:
                return cookie["value"]
        return None

    def get_config_value(self, name, default=None):
        if self.db.contains(name):
            return self.db.get(name)
        else:
            return default

    def set_config_value(self, name, value):
        self.db.insert(name, value)

    def get_cookies_str_force(self):
        self._login_and_save_cookies()
        return self.get_cookies_str()