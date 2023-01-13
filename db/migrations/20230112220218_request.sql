-- migrate:up
CREATE SCHEMA IF NOT EXISTS serv_app; 
CREATE TABLE IF NOT EXISTS serv_app.scores(
    id BIGSERIAL,
    input_requests JSONB NOT NULL,
    output_response JSONB NOT NULL,
    score DECIMAL NOT NULL,
    create_at TIMESTAMP NOT NULL DEFAULT NOW(),
    update_at TIMESTAMP,
    delete_at TIMESTAMP,
    CONSTRAINT scores_id_pkey PRIMARY KEY (id)
);

CREATE INDEX scores_index ON serv_app.scores (score);

-- migrate:down
DROP TABLE IF EXISTS serv_app.scores;
DROP INDEX scores_index;
DROP SCHEMA IF EXISTS serv_app;
