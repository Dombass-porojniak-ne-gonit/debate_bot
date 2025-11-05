from bot.repositories import (
    DebateMotionRepository,
    ResultRepository,
    RoomRepository,
    TeamRepository,
    UserRepository,
)


class RoomService:
    def __init__(
        self,
        room_repo: RoomRepository,
        team_repo: TeamRepository,
        motion_repo: DebateMotionRepository,
        user_repo: UserRepository,
        result_repo: ResultRepository,
    ) -> None:
        self.room_repo = room_repo
        self.team_repo = team_repo
        self.motion_repo = motion_repo
        self.user_repo = user_repo
        self.result_repo = result_repo


# TODO: create room (one added automatically on game creation, but owner/admin of group can add more)
