CREATE TABLE IF NOT EXISTS projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    start_date DATE,
    end_date DATE
);

-- Check if the 'budget' column already exists before altering
SET @column_exists = (
    SELECT COUNT(*)
    FROM information_schema.columns
    WHERE table_schema = DATABASE() AND table_name = 'projects' AND column_name = 'budget'
);

-- Add column only if it does not exist
SET @alter_stmt = IF(@column_exists = 0, 'ALTER TABLE projects ADD COLUMN budget DECIMAL(10,2)', 'SELECT "Column already exists"');
PREPARE stmt FROM @alter_stmt;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;