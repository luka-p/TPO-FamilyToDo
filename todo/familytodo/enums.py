''' NOT IN USE ANY MORE '''
from enum import Enum

''' Importance enum '''
class Importance(Enum):
    HIGH = 'High'
    MEDIUM = 'Medium'
    LOW = 'Low'

''' tuple for task importance choice '''
IMPORTANCE = (
    ('HIGH', 'High'),
    ('MEDIUM', 'Medium'),
    ('LOW', 'Low'))
