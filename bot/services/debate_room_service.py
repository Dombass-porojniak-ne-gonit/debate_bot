from bot.repositories import (
    DebateMotionRepository,
    DebateRoomRepository,
    DebateRoomResultRepository,
    DebateTeamRepository,
    UserRepository,
)


class DebateRoomService:
    def __init__(
        self,
        room_repo: DebateRoomRepository,
        team_repo: DebateTeamRepository,
        motion_repo: DebateMotionRepository,
        user_repo: UserRepository,
        result_repo: DebateRoomResultRepository,
    ) -> None:
        self.room_repo = room_repo
        self.team_repo = team_repo
        self.motion_repo = motion_repo
        self.user_repo = user_repo
        self.result_repo = result_repo


# TODO: create room (one added automatically on game creation, but owner/admin of group can add more)
