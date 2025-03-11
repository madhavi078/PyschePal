from ChatbotWebsite import db, create_app

app = create_app()

with app.app_context():
    db.create_all() 

# Run the app
if __name__ == '__main__':
    app.run()


#set SQLALCHEMY_DATABASE_URI=mysql+pymysql://root:12345678@localhost/users
#set SECRET_KEY=a3d1e94776fa8798d219cd0b4fb7ab76a8d9c038db2adfa5c7c9cd2baf940a3b
#set MAIL_USERNAME=kaarshi03@gmail.com
#set MAIL_PASSWORD=Madhavi@9515