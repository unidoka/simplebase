-- +goose Up
-- +goose StatementBegin
CREATE SCHEMA IF NOT EXISTS auth AUTHORIZATION root;
SET search_path TO auth;

CREATE TABLE "users" (
    id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name varchar(255) NOT NULL, 
    email varchar(255) NOT NULL, 
    password varchar(255) NOT NULL, 
    created_at timestamptz DEFAULT now(),
    updated_at timestamptz DEFAULT now()
);

ALTER TABLE "users" OWNER TO root;

SET search_path TO public;
-- +goose StatementEnd

-- +goose Down
-- +goose StatementBegin
DROP TABLE IF EXISTS auth."users"
-- +goose StatementEnd
