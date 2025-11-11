from bot.repositories import UserDebateClubRoleRepository


class UserDebateClubRoleService:
    def __init__(self, role_repo: UserDebateClubRoleRepository) -> None:
        self.role_repo = role_repo


# TODO: assign role, update role, get club members, check permissions
