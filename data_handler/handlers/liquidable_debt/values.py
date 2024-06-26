import os

from enum import Enum

from dotenv import load_dotenv

load_dotenv()

GS_BUCKET_NAME = os.environ.get("GS_BUCKET_NAME", "")
GS_BUCKET_URL = os.environ.get("GS_BUCKET_URL", "")
LOCAL_STORAGE_PATH = "loans/{protocol_name}_data/"
USER_FIELD_NAME = "User"
PROTOCOL_FIELD_NAME = "Protocol"
COLLATERAL_FIELD_NAME = "Collateral"
DEBT_FIELD_NAME = "Debt"
RISK_ADJUSTED_COLLATERAL_USD_FIELD_NAME = "Risk-adjusted collateral (USD)"
DEBT_USD_FIELD_NAME = "Debt (USD)"
HEALTH_FACTOR_FIELD_NAME = "Health factor"
LIQUIDABLE_DEBT_FIELD_NAME = "Liquidable debt"
ALL_NEEDED_FIELDS = (
    USER_FIELD_NAME,
    PROTOCOL_FIELD_NAME,
    COLLATERAL_FIELD_NAME,
    DEBT_FIELD_NAME,
    RISK_ADJUSTED_COLLATERAL_USD_FIELD_NAME,
    DEBT_USD_FIELD_NAME,
    HEALTH_FACTOR_FIELD_NAME,
)
FIELDS_TO_VALIDATE = (
    COLLATERAL_FIELD_NAME,
    DEBT_FIELD_NAME,
    RISK_ADJUSTED_COLLATERAL_USD_FIELD_NAME,
    HEALTH_FACTOR_FIELD_NAME,
    DEBT_USD_FIELD_NAME,
)


class LendingProtocolNames(Enum):
    HASHSTACK_V0: str = 'hashstack_v0'
    HASHSTACK_V1: str = 'hashstack_v1'
    NOSTRA_ALPHA: str = 'nostra_alpha'
    NOSTRA_MAINNET: str = 'nostra_mainnet'
    ZKLEND: str = 'zklend'
