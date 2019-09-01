--
-- File generated with SQLiteStudio v3.2.1 on Sun Sep 1 16:19:19 2019
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: activity
DROP TABLE IF EXISTS activity;

CREATE TABLE activity (
    activity_id         INTEGER NOT NULL
                                PRIMARY KEY AUTOINCREMENT
                                UNIQUE,
    linked_to_vitals_id INTEGER NOT NULL
                                DEFAULT ''
                                UNIQUE,
    activity_type       TEXT    NOT NULL
                                DEFAULT '',
    distance_mi         NUMERIC NOT NULL
                                DEFAULT '',
    duration_min        INTEGER NOT NULL
                                DEFAULT '',
    duration_sec        INTEGER NOT NULL
                                DEFAULT '',
    feels_like_temp_f   INTEGER NOT NULL
                                DEFAULT '',
    steps_per_min       INTEGER NOT NULL
                                DEFAULT '',
    weights             INTEGER NOT NULL
                                DEFAULT '',
    core                INTEGER NOT NULL
                                DEFAULT '',
    wrist               INTEGER NOT NULL
                                DEFAULT '',
    stairs              INTEGER NOT NULL
                                DEFAULT '',
    squats              INTEGER NOT NULL
                                DEFAULT '',
    breathe             INTEGER NOT NULL
                                DEFAULT '',
    standups            INTEGER NOT NULL
                                DEFAULT '',
    notes               TEXT    NOT NULL
                                DEFAULT '',
    FOREIGN KEY (
        linked_to_vitals_id
    )
    REFERENCES vitals (vitals_id) ON DELETE RESTRICT
                                  ON UPDATE CASCADE,
    FOREIGN KEY (
        activity_type
    )
    REFERENCES activity_types (name) ON DELETE RESTRICT
                                     ON UPDATE RESTRICT
);


-- Table: activity_types
DROP TABLE IF EXISTS activity_types;

CREATE TABLE activity_types (
    name TEXT NOT NULL
            DEFAULT ''
            UNIQUE,
    PRIMARY KEY (
        name
    )
);

INSERT INTO activity_types (
                               name
                           )
                           VALUES (
                               'run'
                           );

INSERT INTO activity_types (
                               name
                           )
                           VALUES (
                               'long-run'
                           );

INSERT INTO activity_types (
                               name
                           )
                           VALUES (
                               'walk'
                           );

INSERT INTO activity_types (
                               name
                           )
                           VALUES (
                               'cross-training'
                           );

INSERT INTO activity_types (
                               name
                           )
                           VALUES (
                               'cooper'
                           );


-- Table: vitals
DROP TABLE IF EXISTS vitals;

CREATE TABLE vitals (
    vitals_id    INTEGER NOT NULL
                         PRIMARY KEY AUTOINCREMENT
                         UNIQUE,
    measured_on  TEXT    NOT NULL
                         DEFAULT '(DATE(''now''))'
                         UNIQUE,
    weight_lb    INTEGER NOT NULL
                         DEFAULT '',
    bp_systolic  INTEGER NOT NULL
                         DEFAULT '',
    bp_diastolic INTEGER NOT NULL
                         DEFAULT '',
    heart_bpm    INTEGER NOT NULL
                         DEFAULT '',
    notes        TEXT    NOT NULL
                         DEFAULT ''
);


-- Index: vitals_measured_on_idx
DROP INDEX IF EXISTS vitals_measured_on_idx;

CREATE UNIQUE INDEX vitals_measured_on_idx ON vitals (
    "measured_on"
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
