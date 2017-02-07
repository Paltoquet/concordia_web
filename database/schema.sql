/*
 *  Create `sensors` table.
 */
CREATE TABLE IF NOT EXISTS sensors (
    id            INTEGER  PRIMARY KEY,
    sensor_name   TEXT     NOT NULL,
    sensor_value  TEXT     NOT NULL,
    sensor_time   DATETIME NOT NULL
);

/*
 *  Create `config` table.
 */
CREATE TABLE IF NOT EXISTS config (
    config_key   TEXT PRIMARY KEY,
    config_value TEXT
);

INSERT INTO config (config_key, config_value)
SELECT * FROM (
/*  Default configuration */
    SELECT 'lightStartTime',  '14:00'    UNION
    SELECT 'lightDuration',   '20'       UNION
    SELECT 'thermoTempStart', '22'       UNION
    SELECT 'thermoTempEnd',   '25'
/* / Default configuration */
)
WHERE NOT EXISTS (SELECT * FROM config)