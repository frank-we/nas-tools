ALTER TABLE "RSS_MOVIES" ADD COLUMN IF NOT EXISTS "SEEDERS" INTEGER DEFAULT 1;
ALTER TABLE "RSS_TVS" ADD COLUMN IF NOT EXISTS "SEEDERS" INTEGER DEFAULT 1;
