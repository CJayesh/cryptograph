from enum import Enum

class DurationSelectionEnum(Enum):
    PREDEFINED = 1
    CUSTOM = 2

class DurationTypeEnum(Enum):
    HOUR = 1
    DAY = 2
    WEEK = 3
    MONTH = 4
    YEAR = 5