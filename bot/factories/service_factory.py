from typing import Any, Dict

from bot.repositories import (
    DebateClubRepository,
    DebateGameRepository,
    DebateMotionRepository,
    DebateParticipantRepository,
    DebateRoomResultRepository,
    DebateTeamRepository,
    UserDebateClubRoleRepository,
    UserRepository,
)
from bot.repositories.debate_room_repository import DebateRoomRepository
from bot.services import (
    DebateClubService,
    DebateGameService,
    DebateMotionService,
    DebateParticipantService,
    DebateRoomResultService,
    DebateTeamService,
    UserDebateClubRoleService,
    UserService,
)
from bot.services.debate_room_service import DebateRoomService


class ServiceFactory:
    _repositories: Dict[str, Any] = {}

    @classmethod
    def _get_repo(cls, repo_class: Any) -> Any:
        repo_name: str = repo_class.__name__
        if repo_name not in cls._repositories:
            cls._repositories[repo_name] = repo_class()
        return cls._repositories[repo_name]

    @classmethod
    def create_user_service(cls) -> UserService:
        return UserService(user_repo=cls._get_repo(UserRepository))

    @classmethod
    def create_debate_club_service(cls) -> DebateClubService:
        return DebateClubService(
            club_repo=cls._get_repo(DebateClubRepository),
            user_repo=cls._get_repo(UserRepository),
        )

    @classmethod
    def create_debate_game_service(cls) -> DebateGameService:
        return DebateGameService(
            debate_game_repo=cls._get_repo(DebateGameRepository),
            debate_club_repo=cls._get_repo(DebateClubRepository),
            user_repo=cls._get_repo(UserRepository),
            participant_repo=cls._get_repo(DebateParticipantRepository),
        )

    @classmethod
    def create_debate_motion_service(cls) -> DebateMotionService:
        return DebateMotionService(
            user_repo=cls._get_repo(UserRepository),
            debate_motion_repo=cls._get_repo(DebateMotionRepository),
        )

    @classmethod
    def create_debate_room_service(cls) -> DebateRoomService:
        return DebateRoomService(
            room_repo=cls._get_repo(DebateRoomRepository),
            team_repo=cls._get_repo(DebateTeamRepository),
            motion_repo=cls._get_repo(DebateMotionRepository),
            user_repo=cls._get_repo(UserRepository),
            result_repo=cls._get_repo(DebateRoomResultRepository),
        )

    @classmethod
    def create_debate_participant_service(cls) -> DebateParticipantService:
        return DebateParticipantService(
            participant_repo=cls._get_repo(DebateParticipantRepository),
        )

    @classmethod
    def create_debate_room_result_service(cls) -> DebateRoomResultService:
        return DebateRoomResultService(
            result_repo=cls._get_repo(DebateRoomResultRepository),
        )

    @classmethod
    def create_debate_team_service(cls) -> DebateTeamService:
        return DebateTeamService(
            team_repo=cls._get_repo(DebateTeamRepository),
        )

    @classmethod
    def create_user_debate_club_role_service(cls) -> UserDebateClubRoleService:
        return UserDebateClubRoleService(
            role_repo=cls._get_repo(UserDebateClubRoleRepository),
        )

    @classmethod
    def create_all_services(cls) -> dict[str, Any]:
        return {
            "user_service": cls.create_user_service(),
            "debate_club_service": cls.create_debate_club_service(),
            "debate_game_service": cls.create_debate_game_service(),
            "debate_motion_service": cls.create_debate_motion_service(),
            "debate_room_service": cls.create_debate_room_service(),
            "debate_participant_service": cls.create_debate_participant_service(),
            "debate_room_result_service": cls.create_debate_room_result_service(),
            "debate_team_service": cls.create_debate_team_service(),
            "user_debate_club_role_service": cls.create_user_debate_club_role_service(),
        }

    @classmethod
    def clear_repositories(cls) -> None:
        cls._repositories.clear()
