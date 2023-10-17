import os
from pw_config import ConfigDev, ConfigProd, ConfigLocal

match os.environ.get('FLASK_CONFIG_TYPE'):
    case 'dev':
        config = ConfigDev()
        print('- pw_models/config: Development')
    case 'prod':
        config = ConfigProd()
        print('- pw_models/config: Production')
    case _:
        config = ConfigLocal()
        print('- pw_models/config: Local')
    