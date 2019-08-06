-- Queries executed on database TrackerTest (C:/______AAAAA_KCFIT/TrackerTest.db)
-- Date and time of execution: 2019-08-06 12:05:41
PRAGMA foreign_keys = 0;
CREATE TABLE sqlitestudio_temp_table AS SELECT * FROM HEALTH;
DROP TABLE HEALTH;
CREATE TABLE HEALTH (HealthId INTEGER PRIMARY KEY NOT NULL DEFAULT (0), Date DATE NOT NULL DEFAULT (''), DayOfWeek TEXT (16) NOT NULL DEFAULT (''), Weight INTEGER NOT NULL DEFAULT (0), BP TEXT (16) NOT NULL DEFAULT (''), Pulse INTEGER NOT NULL DEFAULT (0), Time TIME NOT NULL DEFAULT (''), Notes TEXT (80) NOT NULL DEFAULT (''));
INSERT INTO HEALTH (HealthId, Date, DayOfWeek, Weight, BP, Pulse, Time, Notes) SELECT HealthId, Date, DayOfWeek, Weight, BP, Pulse, Time, Notes FROM sqlitestudio_temp_table;
DROP TABLE sqlitestudio_temp_table;
PRAGMA foreign_keys = 1;

-- Queries executed on database TrackerTest (C:/______AAAAA_KCFIT/TrackerTest.db)
-- Date and time of execution: 2019-08-06 12:07:35
CREATE TABLE RUN (RunId INTEGER PRIMARY KEY NOT NULL DEFAULT (0));

-- Queries executed on database TrackerTest (C:/______AAAAA_KCFIT/TrackerTest.db)
-- Date and time of execution: 2019-08-06 12:11:34
PRAGMA foreign_keys = 0;
CREATE TABLE sqlitestudio_temp_table AS SELECT * FROM RUN;
DROP TABLE RUN;
CREATE TABLE RUN (RunId INTEGER PRIMARY KEY NOT NULL DEFAULT (0), Date DATE NOT NULL DEFAULT (''), DayOfWeek TEXT (16) NOT NULL DEFAULT (''), TimeOfDay TIME NOT NULL DEFAULT (''));
INSERT INTO RUN (RunId) SELECT RunId FROM sqlitestudio_temp_table;
DROP TABLE sqlitestudio_temp_table;
PRAGMA foreign_keys = 1;

-- Queries executed on database TrackerTest (C:/______AAAAA_KCFIT/TrackerTest.db)
-- Date and time of execution: 2019-08-06 12:15:42
PRAGMA foreign_keys = 0;
CREATE TABLE sqlitestudio_temp_table AS SELECT * FROM RUN;
DROP TABLE RUN;
CREATE TABLE RUN (RunId INTEGER PRIMARY KEY NOT NULL DEFAULT (0), Date DATE NOT NULL DEFAULT (''), DayOfWeek TEXT (16) NOT NULL DEFAULT (''), TimeOfDay TIME NOT NULL DEFAULT (''), Weather TEXT (40) NOT NULL DEFAULT (''), Workout TEXT (40) NOT NULL DEFAULT (''));
INSERT INTO RUN (RunId, Date, DayOfWeek, TimeOfDay) SELECT RunId, Date, DayOfWeek, TimeOfDay FROM sqlitestudio_temp_table;
DROP TABLE sqlitestudio_temp_table;
PRAGMA foreign_keys = 1;

-- Queries executed on database TrackerTest (C:/______AAAAA_KCFIT/TrackerTest.db)
-- Date and time of execution: 2019-08-06 12:35:51
PRAGMA foreign_keys = 0;
CREATE TABLE sqlitestudio_temp_table AS SELECT * FROM RUN;
DROP TABLE RUN;
CREATE TABLE RUN (RunId INTEGER PRIMARY KEY NOT NULL DEFAULT (0), Date DATE NOT NULL DEFAULT (''), DayOfWeek TEXT (16) NOT NULL DEFAULT (''), TimeOfDay TIME NOT NULL DEFAULT (''), Weather TEXT (40) NOT NULL DEFAULT (''), Workout TEXT (40) NOT NULL DEFAULT (''), Time TIME NOT NULL DEFAULT (''), Distance NUMERIC (3, 2) NOT NULL DEFAULT (''), Pace NUMERIC (2, 2) NOT NULL DEFAULT (''), Notes TEXT (80) NOT NULL DEFAULT (''));
INSERT INTO RUN (RunId, Date, DayOfWeek, TimeOfDay, Weather, Workout) SELECT RunId, Date, DayOfWeek, TimeOfDay, Weather, Workout FROM sqlitestudio_temp_table;
DROP TABLE sqlitestudio_temp_table;
PRAGMA foreign_keys = 1;

-- Queries executed on database TrackerTest (C:/______AAAAA_KCFIT/TrackerTest.db)
-- Date and time of execution: 2019-08-06 12:37:23
CREATE TABLE WALK (WalkId INTEGER PRIMARY KEY NOT NULL DEFAULT (0));

-- Queries executed on database TrackerTest (C:/______AAAAA_KCFIT/TrackerTest.db)
-- Date and time of execution: 2019-08-06 12:42:07
PRAGMA foreign_keys = 0;
CREATE TABLE sqlitestudio_temp_table AS SELECT * FROM WALK;
DROP TABLE WALK;
CREATE TABLE WALK (WalkId INTEGER PRIMARY KEY NOT NULL DEFAULT (0), Date DATE NOT NULL DEFAULT (0));
INSERT INTO WALK (WalkId) SELECT WalkId FROM sqlitestudio_temp_table;
DROP TABLE sqlitestudio_temp_table;
PRAGMA foreign_keys = 1;

-- Queries executed on database TrackerTest (C:/______AAAAA_KCFIT/TrackerTest.db)
-- Date and time of execution: 2019-08-06 12:50:34
PRAGMA foreign_keys = 0;
CREATE TABLE sqlitestudio_temp_table AS SELECT * FROM WALK;
DROP TABLE WALK;
CREATE TABLE WALK (WalkId INTEGER PRIMARY KEY NOT NULL DEFAULT (0), Date DATE NOT NULL DEFAULT (''), DayOfWeek TEXT (16) NOT NULL DEFAULT (''), Weather TEXT NOT NULL DEFAULT (''), Time TIME NOT NULL DEFAULT (''), Distance DECIMAL (3, 2) NOT NULL DEFAULT (''), Notes TEXT (80) NOT NULL DEFAULT (''));
INSERT INTO WALK (WalkId, Date) SELECT WalkId, Date FROM sqlitestudio_temp_table;
DROP TABLE sqlitestudio_temp_table;
PRAGMA foreign_keys = 1;

-- Queries executed on database TrackerTest (C:/______AAAAA_KCFIT/TrackerTest.db)
-- Date and time of execution: 2019-08-06 12:52:19
PRAGMA foreign_keys = 0;
CREATE TABLE sqlitestudio_temp_table AS SELECT * FROM RUN;
DROP TABLE RUN;
CREATE TABLE RUN (RunId INTEGER PRIMARY KEY NOT NULL DEFAULT (0), Date DATE NOT NULL DEFAULT (''), DayOfWeek TEXT (16) NOT NULL DEFAULT (''), TimeOfDay TIME NOT NULL DEFAULT (''), Weather TEXT (40) NOT NULL DEFAULT (''), Workout TEXT (40) NOT NULL DEFAULT (''), Time TIME NOT NULL DEFAULT (''), Distance DECIMAL (3, 2) NOT NULL DEFAULT (''), Pace DECIMAL (2, 2) NOT NULL DEFAULT (''), Notes TEXT (80) NOT NULL DEFAULT (''));
INSERT INTO RUN (RunId, Date, DayOfWeek, TimeOfDay, Weather, Workout, Time, Distance, Pace, Notes) SELECT RunId, Date, DayOfWeek, TimeOfDay, Weather, Workout, Time, Distance, Pace, Notes FROM sqlitestudio_temp_table;
DROP TABLE sqlitestudio_temp_table;
PRAGMA foreign_keys = 1;

-- Queries executed on database TrackerTest (C:/______AAAAA_KCFIT/TrackerTest.db)
-- Date and time of execution: 2019-08-06 13:01:55
CREATE TABLE Exercise (ExerciseId INTEGER PRIMARY KEY NOT NULL DEFAULT (0), Date DATE NOT NULL DEFAULT (''), DayOfWeek TEXT (16) NOT NULL DEFAULT (''));

-- Queries executed on database TrackerTest (C:/______AAAAA_KCFIT/TrackerTest.db)
-- Date and time of execution: 2019-08-06 13:02:51
PRAGMA foreign_keys = 0;
CREATE TABLE sqlitestudio_temp_table AS SELECT * FROM Exercise;
DROP TABLE Exercise;
CREATE TABLE EXERCISE (ExerciseId INTEGER PRIMARY KEY NOT NULL DEFAULT (0), Date DATE NOT NULL DEFAULT (''), DayOfWeek TEXT (16) NOT NULL DEFAULT (''));
INSERT INTO EXERCISE (ExerciseId, Date, DayOfWeek) SELECT ExerciseId, Date, DayOfWeek FROM sqlitestudio_temp_table;
DROP TABLE sqlitestudio_temp_table;
PRAGMA foreign_keys = 1;

-- Queries executed on database TrackerTest (C:/______AAAAA_KCFIT/TrackerTest.db)
-- Date and time of execution: 2019-08-06 13:04:56
PRAGMA foreign_keys = 0;
CREATE TABLE sqlitestudio_temp_table AS SELECT * FROM EXERCISE;
DROP TABLE EXERCISE;
CREATE TABLE EXERCISE (ExerciseId INTEGER PRIMARY KEY NOT NULL DEFAULT (0), Date DATE NOT NULL DEFAULT (''), DayOfWeek TEXT (16) NOT NULL DEFAULT (''), Stairs BOOLEAN NOT NULL DEFAULT (0), Mercola BOOLEAN NOT NULL DEFAULT (0));
INSERT INTO EXERCISE (ExerciseId, Date, DayOfWeek) SELECT ExerciseId, Date, DayOfWeek FROM sqlitestudio_temp_table;
DROP TABLE sqlitestudio_temp_table;
PRAGMA foreign_keys = 1;

-- Queries executed on database TrackerTest (C:/______AAAAA_KCFIT/TrackerTest.db)
-- Date and time of execution: 2019-08-06 13:12:32
PRAGMA foreign_keys = 0;
CREATE TABLE sqlitestudio_temp_table AS SELECT * FROM EXERCISE;
DROP TABLE EXERCISE;
CREATE TABLE EXERCISE (ExerciseId INTEGER PRIMARY KEY NOT NULL DEFAULT (0), Date DATE NOT NULL DEFAULT (''), DayOfWeek TEXT (16) NOT NULL DEFAULT (''), Stairs BOOLEAN NOT NULL DEFAULT (0), Mercola BOOLEAN NOT NULL DEFAULT (0), Backwards BOOLEAN NOT NULL DEFAULT (0), Weights BOOLEAN NOT NULL DEFAULT (0), WarmUp BOOLEAN NOT NULL DEFAULT (0), StandUps BOOLEAN NOT NULL DEFAULT (0), SitUps BOOLEAN NOT NULL DEFAULT (0), "Vacuum" BOOLEAN NOT NULL DEFAULT (0), Glutes BOOLEAN NOT NULL DEFAULT (0), Wrist BOOLEAN NOT NULL DEFAULT (0), Notes TEXT (80) NOT NULL DEFAULT (''));
INSERT INTO EXERCISE (ExerciseId, Date, DayOfWeek, Stairs, Mercola) SELECT ExerciseId, Date, DayOfWeek, Stairs, Mercola FROM sqlitestudio_temp_table;
DROP TABLE sqlitestudio_temp_table;
PRAGMA foreign_keys = 1;

-- Queries executed on database TrackerTest (C:/______AAAAA_KCFIT/TrackerTest.db)
-- Date and time of execution: 2019-08-06 13:22:40
CREATE TABLE VO2 (Vo2ID INTEGER PRIMARY KEY NOT NULL DEFAULT (0));

-- Queries executed on database TrackerTest (C:/______AAAAA_KCFIT/TrackerTest.db)
-- Date and time of execution: 2019-08-06 13:40:10
PRAGMA foreign_keys = 0;
CREATE TABLE sqlitestudio_temp_table AS SELECT * FROM VO2;
DROP TABLE VO2;
CREATE TABLE VO2 (Vo2ID INTEGER PRIMARY KEY NOT NULL DEFAULT (0), Date DATE NOT NULL DEFAULT (''), DayOfWeek TEXT (16) NOT NULL DEFAULT (''), TimeOfDay TIME NOT NULL DEFAULT (''), Minutes INTEGER NOT NULL DEFAULT (0), Seconds INTEGER NOT NULL DEFAULT (0));
INSERT INTO VO2 (Vo2ID) SELECT Vo2ID FROM sqlitestudio_temp_table;
DROP TABLE sqlitestudio_temp_table;
PRAGMA foreign_keys = 1;

-- Queries executed on database TrackerTest (C:/______AAAAA_KCFIT/TrackerTest.db)
-- Date and time of execution: 2019-08-06 13:48:02
PRAGMA foreign_keys = 0;
CREATE TABLE sqlitestudio_temp_table AS SELECT * FROM VO2;
DROP TABLE VO2;
CREATE TABLE VO2 (Vo2ID INTEGER PRIMARY KEY NOT NULL DEFAULT (0), Date DATE NOT NULL DEFAULT (''), DayOfWeek TEXT (16) NOT NULL DEFAULT (''), TimeOfDay TIME NOT NULL DEFAULT (''), Minutes INTEGER NOT NULL DEFAULT (0), Seconds INTEGER NOT NULL DEFAULT (0), Vo2Max TEXT (25) NOT NULL DEFAULT (''), AgeAvg TEXT (25) NOT NULL DEFAULT (''), Score INTEGER NOT NULL DEFAULT (0), Rating TEXT (16) NOT NULL DEFAULT (''), Notes TEXT (80) NOT NULL DEFAULT (''));
INSERT INTO VO2 (Vo2ID, Date, DayOfWeek, TimeOfDay, Minutes, Seconds) SELECT Vo2ID, Date, DayOfWeek, TimeOfDay, Minutes, Seconds FROM sqlitestudio_temp_table;
DROP TABLE sqlitestudio_temp_table;
PRAGMA foreign_keys = 1;

-- Queries executed on database TrackerTest (C:/______AAAAA_KCFIT/TrackerTest.db)
-- Date and time of execution: 2019-08-06 13:57:41
PRAGMA foreign_keys = 0;
CREATE TABLE sqlitestudio_temp_table AS SELECT * FROM VO2;
DROP TABLE VO2;
CREATE TABLE VO2 (Vo2ID INTEGER PRIMARY KEY NOT NULL DEFAULT (0), Date DATE NOT NULL DEFAULT (''), DayOfWeek TEXT (16) NOT NULL DEFAULT (''), TimeOfDay TIME NOT NULL DEFAULT (''), Minutes INTEGER NOT NULL DEFAULT (0), Seconds INTEGER NOT NULL DEFAULT (0), Mets TEXT (25) NOT NULL DEFAULT (''), Vo2Max TEXT (25) NOT NULL DEFAULT (''), AgeAvg TEXT (25) NOT NULL DEFAULT (''), Score INTEGER NOT NULL DEFAULT (0), Rating TEXT (16) NOT NULL DEFAULT (''), Notes TEXT (80) NOT NULL DEFAULT (''));
INSERT INTO VO2 (Vo2ID, Date, DayOfWeek, TimeOfDay, Minutes, Seconds, Vo2Max, AgeAvg, Score, Rating, Notes) SELECT Vo2ID, Date, DayOfWeek, TimeOfDay, Minutes, Seconds, Vo2Max, AgeAvg, Score, Rating, Notes FROM sqlitestudio_temp_table;
DROP TABLE sqlitestudio_temp_table;
PRAGMA foreign_keys = 1;