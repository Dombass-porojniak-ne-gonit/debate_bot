from bot.repositories import DebateRoomResultRepository


class DebateRoomResultService:
    def __init__(self, result_repo: DebateRoomResultRepository) -> None:
        self.result_repo = result_repo


# TODO: submit result, get results by room, validate result submission
