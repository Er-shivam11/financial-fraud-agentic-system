from typing import TypedDict, Optional


class BankingState(TypedDict):

    question: str

    sql: Optional[str]

    result: Optional[list]

    answer: Optional[str]

    history: Optional[list]