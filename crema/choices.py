from enum import Enum


class EventType(Enum):
    # PSCORE
    USER = "USER"
    LOAN_APPLICATION = "LOAN_APPLICATION"
    DOCUMENT = "DOCUMENT"
    LOAN = "LOAN"
    USER_INFO_REQUEST = "USER_INFO_REQUEST"
    EMPLOYMENT = "EMPLOYMENT"
    DEBIT_INSTRUCTION = "DEBIT_INSTRUCTION"
    ADDRESS = "ADDRESS"
    BANK_ACCOUNT = "BANK_ACCOUNT"
    INCOME_VERIFICATION = "INCOME_VERIFICATION"

    #AMS
    ASSESSMENT = "ASSESSMENT"

    #USER_ACTIVITY
    USER_ACTIVITY = "USER_ACTIVITY"


class EventPartition(Enum):
    # PSCORE
    USER = 64
    LOAN_APPLICATION = 64
    DOCUMENT = 64
    LOAN = 64
    USER_INFO_REQUEST = 64
    EMPLOYMENT = 64
    DEBIT_INSTRUCTION = 64
    ADDRESS = 64
    BANK_ACCOUNT = 64
    INCOME_VERIFICATION = 64

    #AMS
    ASSESSMENT = 64

    #USER_ACTIVITY
    USER_ACTIVITY = 256
