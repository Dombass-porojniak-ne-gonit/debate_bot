from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "debate_club" (
    "id" UUID NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "telegram_id" INT NOT NULL,
    "telegram_link" VARCHAR(255) NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "description" TEXT,
    "total_games" INT NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS "users" (
    "id" UUID NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "telegram_id" BIGINT NOT NULL UNIQUE,
    "is_deactivated" BOOL NOT NULL DEFAULT False,
    "first_name" VARCHAR(255),
    "last_name" VARCHAR(255),
    "username" VARCHAR(255),
    "phone_number" VARCHAR(20),
    "language" VARCHAR(10) NOT NULL DEFAULT 'ua',
    "total_debate_games" INT NOT NULL DEFAULT 0,
    "average_speaker_points" DOUBLE PRECISION
);
CREATE TABLE IF NOT EXISTS "debate_game" (
    "id" UUID NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "name" VARCHAR(255) NOT NULL,
    "description" TEXT,
    "status" VARCHAR(20) NOT NULL DEFAULT 'REGISTRATION',
    "date" DATE NOT NULL,
    "time" TIMETZ,
    "registration_deadline" TIMESTAMPTZ,
    "is_online" BOOL NOT NULL DEFAULT False,
    "location" VARCHAR(500),
    "meeting_link" VARCHAR(500),
    "created_by_id" UUID NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE,
    "debate_club_id" UUID NOT NULL REFERENCES "debate_club" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "debate_game"."status" IS 'REGISTRATION: REGISTRATION\nCOMPLETED: COMPLETED\nCANCELLED: CANCELLED';
CREATE TABLE IF NOT EXISTS "debate_motions" (
    "id" UUID NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "infoslide" VARCHAR(255),
    "text" TEXT NOT NULL,
    "created_by_id" UUID NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "debate_room" (
    "id" UUID NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "adjudicator_id" UUID REFERENCES "users" ("id") ON DELETE CASCADE,
    "game_id" UUID NOT NULL REFERENCES "debate_game" ("id") ON DELETE CASCADE,
    "motion_id" UUID REFERENCES "debate_motions" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "debate_team" (
    "id" UUID NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "position" SMALLINT,
    "rank" INT,
    "room_id" UUID NOT NULL REFERENCES "debate_room" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "debate_team"."position" IS 'G1: 1\nG2: 2\nO1: 3\nO2: 4';
CREATE TABLE IF NOT EXISTS "debate_participant" (
    "id" UUID NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "role" SMALLINT NOT NULL DEFAULT 1,
    "speaker_points" INT,
    "game_id" UUID NOT NULL REFERENCES "debate_game" ("id") ON DELETE CASCADE,
    "team_id" UUID REFERENCES "debate_team" ("id") ON DELETE CASCADE,
    "user_id" UUID NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE,
    CONSTRAINT "uid_debate_part_user_id_1023a7" UNIQUE ("user_id", "game_id")
);
COMMENT ON COLUMN "debate_participant"."role" IS 'DEBATER: 1\nJUDGE: 2\nWING: 3\nVIEWER: 4\nWAIT: 5';
CREATE TABLE IF NOT EXISTS "debate_room_result" (
    "id" UUID NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "feedback" TEXT,
    "room_id" UUID NOT NULL REFERENCES "debate_room" ("id") ON DELETE CASCADE,
    "submitted_id" UUID NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE,
    "winning_team_id" UUID REFERENCES "debate_team" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "user_debate_club_role" (
    "id" UUID NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "role" SMALLINT NOT NULL DEFAULT 1,
    "debate_club_id" UUID NOT NULL REFERENCES "debate_club" ("id") ON DELETE CASCADE,
    "user_id" UUID NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE,
    CONSTRAINT "uid_user_debate_user_id_c275d9" UNIQUE ("user_id", "debate_club_id")
);
COMMENT ON COLUMN "user_debate_club_role"."role" IS 'MEMBER: 1\nMODERATOR: 2\nADMIN: 3\nOWNER: 4';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "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"
    "sIHY2oY8oFPMQ1P+9PLz/zwW+z0="
)
