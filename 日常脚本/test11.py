import sys
sys.path.append('../')
from common.common import Common

common = Common()
name = common.update_stream(3785, 1)
print(name)