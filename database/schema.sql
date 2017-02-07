/*
 *  Create `sensors` table.
 */
CREATE TABLE IF NOT EXISTS sensors (
    id            INTEGER  PRIMARY KEY,
    sensor_name   TEXT     NOT NULL,
    sensor_value  TEXT     NOT NULL,
    sensor_time   DATETIME NOT NULL
);
