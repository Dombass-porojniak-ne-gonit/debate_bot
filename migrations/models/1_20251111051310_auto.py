from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "debate_club" ALTER COLUMN "telegram_id" TYPE BIGINT USING "telegram_id"::BIGINT;
        ALTER TABLE "debate_game" ADD "telegram_group_message_id" BIGINT NOT NULL UNIQUE;
        ALTER TABLE "users" DROP COLUMN "is_deactivated";
        COMMENT ON COLUMN "user_debate_club_role"."role" IS 'MEMBER: 1
JUDGE: 2
ADMIN: 3
OWNER: 4';
        CREATE UNIQUE INDEX IF NOT EXISTS "uid_debate_club_telegra_f17a23" ON "debate_club" ("telegram_id");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP INDEX IF EXISTS "uid_debate_game_telegra_546686";
        ALTER TABLE "debate_club" DROP CONSTRAINT IF EXISTS "debate_club_telegram_id_key";
        DROP INDEX IF EXISTS "uid_debate_club_telegra_f17a23";
        ALTER TABLE "users" ADD "is_deactivated" BOOL NOT NULL DEFAULT False;
        ALTER TABLE "debate_club" ALTER COLUMN "telegram_id" TYPE INT USING "telegram_id"::INT;
        ALTER TABLE "debate_game" DROP COLUMN "telegram_group_message_id";
        COMMENT ON COLUMN "user_debate_club_role"."role" IS 'MEMBER: 1
MODERATOR: 2
ADMIN: 3
OWNER: 4';"""


MODELS_STATE = (
    "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"
    "AUgXAss="
)
