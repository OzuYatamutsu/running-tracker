PRAGMA foreign_keys=off;

CREATE TABLE vitals_migration (
    entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME NOT NULL DEFAULT (DATETIME('now')),
    weight_lb NUMERIC NOT NULL,
    bp_systolic NUMERIC NOT NULL,
    bp_diastolic NUMERIC NOT NULL,
    heart_bpm UNSIGNED INTEGER NOT NULL,
    notes TEXT(1024) NOT NULL DEFAULT ''
);

INSERT INTO vitals_migration SELECT * FROM vitals;
DROP TABLE vitals;

ALTER TABLE vitals_migration RENAME TO vitals;
CREATE INDEX vitals_timestamp_idx ON vitals (timestamp);

CREATE TABLE activity_migration (
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

INSERT INTO activity_migration SELECT * FROM activity;
DROP TABLE activity;

ALTER TABLE activity_migration RENAME TO activity;
CREATE INDEX activity_timestamp_idx ON activity (timestamp);

DROP TABLE vo2;

PRAGMA foreign_keys=on;
COMMIT;

