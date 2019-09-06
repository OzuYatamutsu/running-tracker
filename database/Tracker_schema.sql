PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: activity
DROP TABLE IF EXISTS activity;

/*
One activity record per day inserted after vitals record.
Table fields default to an empty string ('').
Fields:
activity_id: integer primary key autoincrement
vitals_id: primary key of vitals table - Foreign Key here
activity type: primary key of activity_types table - Foreign Key here 
distance_mi: numeric or '' - distance in miles
duration_min: integer or ''
duration_sec: integer or ''
pace_mi: numeric or '' - pace per mile
steps_per_min: integer or '' - cadence value for run or walk activity
feels_like_temp_f: integer or '' - heat index at time of activity - usually several degrees hotter than outside temperature
weights: "Y" or '' - usual schedule is 3x per week 
core: "Y" or '' - daily schedule - situps, bridge, vacuum
wrist: "Y" or '' - daily schedule - squeeze blood pressure grips - 100x
stairs: "Y" or '' - daily schedule - up and down one story or more - at least 10x
breathe: "Y" or '' - daily schedule - Airlife Incentive Spirometer - at least 5 x
standups: "Y" or '' - daily schedule - get up and down from a sitting position on the floor without assistance
backwards: "Y" or '' - daily schedule - walk backwards to sharpen the senses and improve coordination
notes: additional daily info or ''
*/

CREATE TABLE "activity" (
	"activity_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"linked_to_vitals_id"	INTEGER NOT NULL DEFAULT '' UNIQUE,
	"activity_type"	TEXT NOT NULL DEFAULT '',
	"distance_mi"	NUMERIC NOT NULL DEFAULT '',
	"duration_min"	INTEGER NOT NULL DEFAULT '',
	"duration_sec"	INTEGER NOT NULL DEFAULT '',
	"pace_mi"	NUMERIC NOT NULL DEFAULT '',
	"steps_per_min"	INTEGER NOT NULL DEFAULT '',
	"feels_like_temp_f"	INTEGER NOT NULL DEFAULT '',
	"weights"	TEXT NOT NULL DEFAULT '',
	"core"	TEXT NOT NULL DEFAULT '',
	"wrist"	TEXT NOT NULL DEFAULT '',
	"stairs"	TEXT NOT NULL DEFAULT '',
	"breathe"	TEXT NOT NULL DEFAULT '',
	"standups"	TEXT NOT NULL DEFAULT '',
	"backwards"	TEXT NOT NULL DEFAULT (''),
	"notes"	TEXT NOT NULL DEFAULT '',
	FOREIGN KEY("linked_to_vitals_id") REFERENCES "vitals"("vitals_id") ON DELETE RESTRICT ON UPDATE CASCADE,
	FOREIGN KEY("activity_type") REFERENCES "activity_types"("name") ON DELETE RESTRICT ON UPDATE RESTRICT
);


-- Table: activity_types
DROP TABLE IF EXISTS activity_types;

/*
Fields: name: primary key - possible values: run, long-run, cooper, walk, cross-training
*/

CREATE TABLE activity_types (
    name TEXT NOT NULL
            DEFAULT ''
            UNIQUE,
    PRIMARY KEY (
        name
    )
);


-- Table: vitals
DROP TABLE IF EXISTS vitals;

/*
One vitals record per day inserted before activity record.
Table fields default to an empty string ('').
Fields:
vitals_id: integer primary key autoincrement
measured_on: date vitals record created
weight_lb: integer or ''
bp_systolic: integer or ''
bp_diastolic: integer or ''
heart_bpm: integer or '' - pulse rate measured along with blood pressure
bp_time: time of day blood pressure measured or ''
week_day: day of week vitals record created
notes: additional daily vitals info or ''      
*/

CREATE TABLE vitals (
    vitals_id    INTEGER NOT NULL
                         PRIMARY KEY AUTOINCREMENT
                         UNIQUE,
    measured_on  TEXT    NOT NULL
                         DEFAULT ('') 
                         UNIQUE,
    weight_lb    INTEGER NOT NULL
                         DEFAULT '',
    bp_systolic  INTEGER NOT NULL
                         DEFAULT '',
    bp_diastolic INTEGER NOT NULL
                         DEFAULT '',
    heart_bpm    INTEGER NOT NULL
                         DEFAULT '',
    bp_time      TEXT    NOT NULL
                         DEFAULT (''),
    week_day     TEXT    NOT NULL
                         DEFAULT (''),
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
