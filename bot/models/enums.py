from enum import IntEnum, StrEnum


class DebateTeamPosition(IntEnum):
    G1 = 1
    G2 = 2
    O1 = 3
    O2 = 4


class GameStatus(StrEnum):
    REGISTRATION = "REGISTRATION"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class AttendanceStatus(IntEnum):
    REGISTERED = 1
    CONFIRMED = 2
    ATTENDED = 3
    WITHDRAWN = 4


class ClubRole(IntEnum):
    MEMBER = 1  # Can play as player/wing/viewer judge assignment only by admin or owner
    JUDGE = 2  # Can assign himself to rooms as judge
    ADMIN = 3  # Manage bot
    OWNER = 4  # Manage admins


class ParticipantRole(IntEnum):
    DEBATER = 1
    JUDGE = 2
    WING = 3
    VIEWER = 4
    WAIT = 5
