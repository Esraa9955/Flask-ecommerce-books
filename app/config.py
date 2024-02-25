class Config:
  @staticmethod
  def init_app():
    pass


class DevelopmentConfig(Config):
  DEBUG=True
  SQLALCHEMY_DATABASE_URI='sqlite:///Project.db'


class ProductionConfig(Config):
  DEBUG=False
  SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12345@localhost:5432/flask'



config_options ={
  "dev":DevelopmentConfig,
  "prd":ProductionConfig
}