from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class NotificationValidationValues:
    telegram_id_pattern: str = r"^\d{9,10}$"
    telegram_id_min_length: int = 9
    telegram_id_max_length: int = 10
    health_ratio_level_min_value: float = 0
    health_ratio_level_max_value: float = 10
    unique_fields: tuple[str, ...] = (
        "email",
        "telegram_id",
    )
    validation_fields: tuple[str, ...] = (
        "email",
        "wallet_id",
        "telegram_id",
        "ip_address",
    )


@dataclass(frozen=True)
class CreateSubscriptionValues:
    create_subscription_success_message: str = "Subscription created successfully"
    create_subscription_exception_message: str = "Please provide all needed data"
    create_subscription_description_message: str = (
        "Creates a new subscription to notifications"
    )


class ProtocolIDs(Enum):
    HASHSTACK: str = "Hashstack"
    NOSTRA: str = "Nostra"
    ZKLEND: str = "zkLend"