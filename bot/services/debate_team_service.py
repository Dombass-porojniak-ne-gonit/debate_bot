from bot.repositories import DebateTeamRepository


class DebateTeamService:
    def __init__(self, team_repo: DebateTeamRepository) -> None:
        self.team_repo = team_repo


# TODO: create teams for room, assign positions, update rankings
