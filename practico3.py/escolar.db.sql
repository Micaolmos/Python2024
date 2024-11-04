BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `Profesor` (
	`dni`	INTEGER NOT NULL,
	`nombre`	TEXT NOT NULL,
	`apellido`	TEXT NOT NULL,
	`curso`	INTEGER NOT NULL,
	`estado`	TEXT NOT NULL,
	`email`	INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS `Materias` (
	`id_materia`	INTEGER,
	`nombre_materia`	TEXT NOT NULL,
	`curso_materia`	INTEGER NOT NULL,
	`descripcion`	TEXT,
	`horario`	INTEGER NOT NULL,
	PRIMARY KEY(`id_materia`)
);
CREATE TABLE IF NOT EXISTS `Estudiante` (
	`legajo_id`	INTEGER,
	`dni`	TEXT NOT NULL,
	`nombre`	TEXT NOT NULL,
	`edad`	INTEGER NOT NULL,
	`fecha_nacimiento`	INTEGER NOT NULL,
	`curso`	INTEGER NOT NULL,
	`estados`	INTEGER NOT NULL,
	`email`	INTEGER NOT NULL,
	PRIMARY KEY(`legajo_id`)
);
CREATE TABLE IF NOT EXISTS `Calificacion` (
	`id_estudiante`	INTEGER,
	`id_materia`	TEXT NOT NULL,
	`nota`	INTEGER NOT NULL,
	`fecha`	INTEGER NOT NULL,
	FOREIGN KEY(`id_materia`) REFERENCES `materias`(`id`),
	FOREIGN KEY(`id_estudiante`) REFERENCES `estudiantes`(`id`),
	PRIMARY KEY(`id_estudiante`)
);
COMMIT;
