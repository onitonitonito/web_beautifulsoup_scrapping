"""
# to make stdout environment cp494 [WINDOWS-7] to utf-8
#
"""
print(__doc__)

import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf8')
