class Config:
    SECRET_KEY = 'hard to guess string'
    JWT_SECRET_KEY = 'your_jwt_secret_key'
    SESSION_PROTECTION = 'strong'
    SQLALCHEMY_DATABASE_URI = 'mysql://web:web@db/data_dt'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MQTT_BROKER_URL = 'mqtt5'
    MQTT_BROKER_PORT = 1883
    MQTT_USERNAME = 'web'
    MQTT_PASSWORD = 'web'
    MQTT_KEEPALIVE = 5

    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=465
    MAIL_USERNAME='yijunguo473@gmail.com'
    MAIL_PASSWORD='yqyjiraegxflepcu'
    MAIL_USE_SSL=True
    MAIL_USE_TLS=False
    MAIL_DEFAULT_SENDER=('admin', 'yijunguo473@gmail.com')
    MAIL_MAX_EMAILS=10,
    
    # yqyj irae gxfl epcu