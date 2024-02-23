from flask import Flask

def create_app(config_name='dev'):
  app = Flask(__name__)
  #current_config = AppConfig[config_name]
  #print(current_config)
  #app.config['SQLALCHEMY_DATABASE_URI']=current_config.SQLALCHEMY_DATABASE_URI
  #app.config.from_object(current_config)

  #db.init_app(app)
  #migrate=Migrate(app,db,render_as_batch=True)
  return app
