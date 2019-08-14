CREATE TABLE vitals (
    entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME NOT NULL DEFAULT (DATETIME('now')),
    weight_lb NUMERIC NOT NULL,
    bp_systolic NUMERIC NOT NULL,
    bp_diastolic NUMERIC NOT NULL,
    heart_bpm UNSIGNED INTEGER NOT NULL,
    notes TEXT(1024) NOT NULL DEFAULT ''
);

CREATE INDEX vitals_timestamp_idx ON vitals (timestamp);

CREATE TABLE activity_types (
    name TEXT PRIMARY KEY NOT NULL
);

-- Seed activity types into table
INSERT INTO activity_types (name) VALUES
    ('run'),
    ('walk'),
    ('cross-training');

CREATE TABLE activity (
    entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vitals_id INTEGER NOT NULL,
    activity_type TEXT NOT NULL,
    distance_mi NUMERIC NOT NULL,
    duration_min UNSIGNED INTEGER NOT NULL,
    duration_sec UNSIGNED INTEGER NOT NULL,
    temp_f NUMERIC,
    notes TEXT(1024) NOT NULL DEFAULT '',

    FOREIGN KEY (activity_type) REFERENCES activity_types(name)
        ON UPDATE RESTRICT
        ON DELETE RESTRICT,

    FOREIGN KEY (vitals_id) REFERENCES vitals(entry_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE INDEX activity_timestamp_idx ON activity (timestamp);

COMMIT;
