from bot.repositories import DebateMotionRepository, UserRepository


class DebateMotionService:
    def __init__(
        self, user_repo: UserRepository, debate_motion_repo: DebateMotionRepository
    ) -> None:
        self.debate_motion_repo = debate_motion_repo
        self.user_repo = user_repo


# TODO: create motion, get by user, get random motion (need to discuss logic of it), get user motions, get user played motions
