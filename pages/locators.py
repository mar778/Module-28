from selenium.webdriver.common.by import By


class AuthLocators:
    phone_tab = (By.ID, 't-btn-tab-phone')
    mail_tab = (By.ID, 't-btn-tab-mail')
    login_tab = (By.ID, 't-btn-tab-login')
    ls_tab = (By.ID, 't-btn-tab-ls')
    tab_no_active = (By.CSS_SELECTOR, "rt-tab.rt-tab--small")
    tab_value = (By.XPATH, "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]")
    tab_active = (By.CSS_SELECTOR, ".rt-tab.rt-tab--small.rt-tab--active")
    name_field = (By.ID, 'username')
    password_field = (By.ID, 'password')
    error_phone = (By.XPATH, "//span[contains(text(),'Введите номер телефона')]")
    error_mail = (By.XPATH, "//span[contains(text(),'Введите адрес, указанный при регистрации')]")
    error_login = (By.XPATH, "//span[contains(text(),'Введите логин, указанный при регистрации')]")
    error_ls = (By.XPATH, "//span[contains(text(),'Введите номер вашего лицевого счета')]")
    forgot_password = (By.ID, "forgot_password")
    btn_login = (By.ID, "kc-login")
    registration = (By.ID, "kc-register")
    customer_support = (By.XPATH, "//div[contains(text(),'Поддержка')]")
    name_support = (By.XPATH, "//input[@id='full-name']")
    phone_support = (By.XPATH, "//label[contains(text(),'Номер телефона без +7')]")
    close_customer_support = (By.XPATH, "//div[@id='widget_closeChat']")
    eye_icon = (By.XPATH, "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[2]/*[1]")
    terms_of_use = (By.XPATH, "//span[contains(text(),'Пользовательским соглашением')]")
    error_message = (By.ID, "form-error-message")
    auth = (By.XPATH, "//h1[contains(text(),'Авторизация')]")
    lk = (By.XPATH, "//body/div[@id='app']/main[1]/div[1]/div[2]/div[3]/h3[1]")
    tab = (By.XPATH, "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]")
    lk_logo = (By.XPATH, "//h2[contains(text(),'Личный кабинет')]")

class RegistrationLocators:
    reg = (By.XPATH, "//h1[contains(text(),'Регистрация')]")
    first_name_field = (By.NAME, "firstName")
    last_name_field = (By.NAME, "lastName")
    region_field = (By.XPATH, "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/input[1]")
    address_field = (By.ID, "address")
    password_reg_field = (By.ID, "password")
    password_confirm_field = (By.ID, "password-confirm")
    btn_reg = (By.NAME, "register")
    error_firts_name = (By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")
    error_last_name = (By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")

class PassRecoveryLocators:
    pass_recovery = (By.XPATH, "//h1[contains(text(),'Восстановление пароля')]")
    back = (By.ID, "reset-back")
    phone_tab = (By.ID, 't-btn-tab-phone')
    mail_tab = (By.ID, 't-btn-tab-mail')
    login_tab = (By.ID, 't-btn-tab-login')
    ls_tab = (By.ID, 't-btn-tab-ls')
    btn_continue = (By.ID, "reset")
    captcha = (By.CSS_SELECTOR, ".reset-form__captcha")
