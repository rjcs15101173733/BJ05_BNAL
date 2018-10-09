import allure

from Base.base import Base
import Page
class PageLogin(Base):
    # 点击我
    @allure.step('点击我')
    def page_click_me(self):
        self.base_click(Page.me_btn)
    # 点击已有账号，去登录
    @allure.step('点击已有账号')
    def page_click_info(self):
        self.base_click(Page.user)
    # 输入账号
    @allure.step('输入账号')
    def page_input_user(self,username):
        self.base_input(Page.user_name,username)
    # 输入密码
    @allure.step('输入密码')
    def page_input_pwd(self,password):
        self.base_input(Page.user_pwd,password)
    # 点击登录按钮
    @allure.step('点击登录按钮')
    def page_click_login_btn(self):
        self.base_click(Page.login_btn)
    @allure.step('点击设置按钮')
    def page_click_setting(self):
        self.base_click(Page.setting_btn)

    @allure.step('点击滑动>消息推送>修改密码')
    def page_drag_and_drop(self):
        el1 = self.base_find_element(Page.msg_send)
        el2 = self.base_find_element(Page.update_pwd)
        self.base_drag_and_drop(el1,el2)

    @allure.step('点击退出账号')
    def page_click_exit_bt(self):
        self.base_click(Page.exit_btn)

    @allure.step('点击确认退出账号')
    def page_click_exit_ok(self):
        self.base_click(Page.exit_ok)

    def page_login(self,username,password):
        self.page_click_me()
        self.page_click_info()
        self.page_input_user(username)
        self.page_input_pwd(password)
        self.page_click_login_btn()

    def page_login_logout(self):
        # 点击设置
        self.page_click_setting()
        # 滑动屏幕  消息推送滑到修改密码
        self.page_drag_and_drop()
        # 点击退出按钮
        self.page_click_exit_bt()
        # 确认退出
        self.page_click_exit_ok()

    @allure.step('获取nickname信息')
    def page_get_nickname(self):
        return self.base_get_text(Page.me_nickname)