from dotenv import load_dotenv
import os

# Config class to store all the configuration variables


class Config:
    DEBUG = False
    SECRET_KEY = os.environ.get("SECRET_KEY")
    # contain mysql database url with user and password
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/users' #mysql
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'  #Alternative database if mysql not working
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")



#set SQLALCHEMY_DATABASE_URI=mysql+pymysql://root:12345678@localhost/users
#set SECRET_KEY=a3d1e94776fa8798d219cd0b4fb7ab76a8d9c038db2adfa5c7c9cd2baf940a3b
#set MAIL_USERNAME=tejmani913@gmail.com
#set MAIL_PASSWORD=ManiMadhavi@9515
