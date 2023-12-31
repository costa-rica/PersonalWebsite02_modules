import os
import json
from dotenv import load_dotenv

load_dotenv()
print("- reading dd07modules/pw_config/config.py")
print(f"- FLASK_CONFIG_TYPE: {os.environ.get('FLASK_CONFIG_TYPE')}")
print(f"- FLASK_DEBUG: {os.environ.get('FLASK_DEBUG')}")

match os.environ.get('FLASK_CONFIG_TYPE'):
    case 'dev' :
        with open(os.path.join(os.environ.get('CONFIG_PATH_SERVER'), os.environ.get('CONFIG_FILE_NAME'))) as env_file:
            env_dict = json.load(env_file)
        with open(os.path.join(os.environ.get('CONFIG_PATH_SERVER'), os.environ.get('CONFIG_FILE_NAME_SUPPORT'))) as env_support_file:
            env_support_dict = json.load(env_support_file)
    case 'prod' :
        with open(os.path.join(os.environ.get('CONFIG_PATH_SERVER'), os.environ.get('CONFIG_FILE_NAME'))) as env_file:
            env_dict = json.load(env_file)
        with open(os.path.join(os.environ.get('CONFIG_PATH_SERVER'), os.environ.get('CONFIG_FILE_NAME_SUPPORT'))) as env_support_file:
            env_support_dict = json.load(env_support_file)
    case _:
        with open(os.path.join(os.environ.get('CONFIG_PATH_LOCAL'), os.environ.get('CONFIG_FILE_NAME'))) as env_file:
            env_dict = json.load(env_file)
        with open(os.path.join(os.environ.get('CONFIG_PATH_LOCAL'), os.environ.get('CONFIG_FILE_NAME_SUPPORT'))) as env_support_file:
            env_support_dict = json.load(env_support_file)

class ConfigBasic():

    def __init__(self):
        self.SECRET_KEY = env_dict.get('SECRET_KEY')
        self.DB_LOCAL_ROOT = os.environ.get('DB_LOCAL_ROOT')
        self.DB_DEV_ROOT = os.environ.get('DB_DEV_ROOT')
        self.DB_PROD_ROOT = os.environ.get('DB_PROD_ROOT')
        
        #Email stuff
        # self.MAIL_SERVER = env_dict.get('MAIL_SERVER_MSOFFICE')
        # self.MAIL_PORT = env_dict.get('MAIL_PORT')
        self.MAIL_USE_TLS = True
        # self.MAIL_USERNAME = env_dict.get('MAIL_EMAIL')
        # self.MAIL_PASSWORD = env_dict.get('MAIL_PASSWORD')
        self.ACCEPTED_EMAILS = env_dict.get('ACCEPTED_EMAILS')

        #web Guest
        self.GUEST_EMAIL = env_dict.get('GUEST_EMAIL')
        self.GUEST_PASSWORD = env_dict.get('GUEST_PASSWORD')

        #API
        self.API_URL = os.environ.get("API_URL")

        #Admin stuff
        self.ADMIN_EMAILS = env_dict.get('ADMIN_EMAILS')
        self.REGISTRATION_KEY =env_dict.get('REGISTRATION_KEY')
        self.BLS_API_URL = env_dict.get('BLS_API_URL')

        #Captcha
        self.SITE_KEY_CAPTCHA = env_support_dict.get('SITE_KEY_CAPTCHA')
        self.SECRET_KEY_CAPTCHA = env_support_dict.get('SECRET_KEY_CAPTCHA')
        self.VERIFY_URL_CAPTCHA = 'https://www.google.com/recaptcha/api/siteverify'

        #Support
        self.MAIL_SERVER = env_support_dict.get('MAIL_SERVER_MSOFFICE_SUPPORT')
        self.MAIL_PORT = env_support_dict.get('MAIL_PORT_SUPPORT')
        self.MAIL_USE_TLS_SUPPORT = True#<----- what is this?
        self.MAIL_USERNAME = env_support_dict.get('MAIL_EMAIL_SUPPORT')
        self.MAIL_PASSWORD = env_support_dict.get('MAIL_PASSWORD_SUPPORT')
        self.MAIL_NICK_GMAIL = env_support_dict.get('MAIL_NICK_GMAIL')


class ConfigLocal(ConfigBasic):
    
    def __init__(self):
        super().__init__()
        self.PROJECT_ROOT = os.environ.get('PROJECT_LOCAL_ROOT')
        # Database
        self.DB_ROOT = self.DB_LOCAL_ROOT
        self.SQL_URI_USERS = f"sqlite:///{self.DB_LOCAL_ROOT}{os.environ.get('DB_NAME_BLOGPOST')}"
        # # other directories
        self.DIR_DB_AUXILIARY = os.path.join(self.DB_LOCAL_ROOT,"auxiliary")
        self.DIR_DB_AUX_FILES_WEBSITE = os.path.join(self.DIR_DB_AUXILIARY,"files_website")
        self.DIR_DB_AUX_BLOG = os.path.join(self.DIR_DB_AUXILIARY,"blog")
        self.DIR_DB_AUX_BLOG_POSTS = os.path.join(self.DIR_DB_AUXILIARY,"blog","posts")
        self.DIR_DB_AUX_BLOG_ICONS = os.path.join(self.DIR_DB_AUXILIARY,"blog","blog_icons")

    DEBUG = True

class ConfigDev(ConfigBasic):

    def __init__(self):
        super().__init__()
        self.PROJECT_ROOT = os.environ.get('PROJECT_DEV_ROOT')
        # Database
        self.DB_ROOT = self.DB_DEV_ROOT
        self.SQL_URI_USERS = f"sqlite:///{self.DB_DEV_ROOT}{os.environ.get('DB_NAME_BLOGPOST')}"
        # # other directories
        self.DIR_DB_AUXILIARY = os.path.join(self.DB_DEV_ROOT,"auxiliary")
        self.DIR_DB_AUX_FILES_WEBSITE = os.path.join(self.DIR_DB_AUXILIARY,"files_website")
        self.DIR_DB_AUX_BLOG = os.path.join(self.DIR_DB_AUXILIARY,"blog")
        self.DIR_DB_AUX_BLOG_POSTS = os.path.join(self.DIR_DB_AUXILIARY,"blog","posts")
        self.DIR_DB_AUX_BLOG_ICONS = os.path.join(self.DIR_DB_AUXILIARY,"blog","blog_icons")

    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True

class ConfigProd(ConfigBasic):
        
    def __init__(self):
        super().__init__()
        self.PROJECT_ROOT = os.environ.get('PROJECT_PROD_ROOT')
        # Database
        self.DB_ROOT = self.DB_PROD_ROOT
        self.SQL_URI_USERS = f"sqlite:///{self.DB_PROD_ROOT}{os.environ.get('DB_NAME_BLOGPOST')}"
        # # other directories
        self.DIR_DB_AUXILIARY = os.path.join(self.DB_PROD_ROOT,"auxiliary")
        self.DIR_DB_AUX_FILES_WEBSITE = os.path.join(self.DIR_DB_AUXILIARY,"files_website")
        self.DIR_DB_AUX_BLOG = os.path.join(self.DIR_DB_AUXILIARY,"blog")
        self.DIR_DB_AUX_BLOG_POSTS = os.path.join(self.DIR_DB_AUXILIARY,"blog","posts")
        self.DIR_DB_AUX_BLOG_ICONS = os.path.join(self.DIR_DB_AUXILIARY,"blog","blog_icons")

    DEBUG = False
    TESTING = False
    PROPAGATE_EXCEPTIONS = True
