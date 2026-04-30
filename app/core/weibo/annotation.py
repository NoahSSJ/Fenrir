from typing import Annotated
from store import *

RedisClient = Annotated[RedisConfig, 'RedisConfig instance']
MinIOClient = Annotated[MinIOConfig, 'MinIOConfig instance']
