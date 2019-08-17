PRAGMA foreign_keys=off;

CREATE TABLE vitals_migration (
    entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
    measured_on DATE NOT NULL DEFAULT (DATE('now')),
    weight_lb NUMERIC NOT NULL,
    bp_systolic NUMERIC NOT NULL,
    bp_diastolic NUMERIC NOT NULL,
    heart_bpm UNSIGNED INTEGER NOT NULL,
    notes TEXT(1024) NOT NULL DEFAULT ''
);

INSERT INTO vitals_migration SELECT * FROM vitals;
DROP TABLE vitals;

ALTER TABLE vitals_migration RENAME TO vitals;
CREATE INDEX vitals_measured_on_idx ON vitals (measured_on);

INSERT INTO activity_types (name) VALUES
    ('run-intervals'),
    ('cross-training'),
    ('cooper');

CREATE TABLE activity_migration (
    entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
    linked_to_vitals_entry INTEGER NOT NULL,
    activity_type TEXT NOT NULL,
    distance_mi NUMERIC NOT NULL,
    duration_min UNSIGNED INTEGER NOT NULL,
    duration_sec UNSIGNED INTEGER NOT NULL,
    feels_like_temp_f NUMERIC,
    steps_per_min NUMERIC,
    notes TEXT(1024) NOT NULL DEFAULT '',

    FOREIGN KEY (activity_type) REFERENCES activity_types(name)
        ON UPDATE RESTRICT
        ON DELETE RESTRICT,

    FOREIGN KEY (linked_to_vitals_entry) REFERENCES vitals(entry_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

INSERT INTO activity_migration SELECT * FROM activity;
DROP TABLE activity;

ALTER TABLE activity_migration RENAME TO activity;

DROP TABLE vo2;

PRAGMA foreign_keys=on;
COMMIT;
