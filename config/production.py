from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\x96\xa1\xd0\xdf\xf27\xda\x8d\xc2\xe2\xd3\x94#\x93\xadm'

