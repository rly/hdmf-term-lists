

CREATE TABLE "ElectricalArray" (
	axis0 TEXT NOT NULL, 
	axis1 TEXT NOT NULL, 
	"values" FLOAT NOT NULL, 
	PRIMARY KEY (axis0, axis1, "values")
);

CREATE TABLE "Electrode" (
	name TEXT, 
	impedance FLOAT, 
	PRIMARY KEY (name, impedance)
);

CREATE TABLE "ElectrodeSeries" (
	name TEXT NOT NULL, 
	data_type TEXT, 
	"values" TEXT NOT NULL, 
	PRIMARY KEY (name, data_type, "values")
);

CREATE TABLE "NWBFile" (
	raw_ephys TEXT, 
	subject TEXT, 
	PRIMARY KEY (raw_ephys, subject)
);

CREATE TABLE "OneDimensionalSeries" (
	name TEXT NOT NULL, 
	data_type TEXT, 
	"values" TEXT NOT NULL, 
	PRIMARY KEY (name, data_type, "values")
);

CREATE TABLE "Subject" (
	subject_id TEXT, 
	sex VARCHAR(6), 
	species VARCHAR(12), 
	PRIMARY KEY (subject_id, sex, species)
);

CREATE TABLE "TimestampSeries" (
	name TEXT NOT NULL, 
	data_type TEXT, 
	"values" FLOAT NOT NULL, 
	PRIMARY KEY (name, data_type, "values")
);

CREATE TABLE "TwoDimensionalArray" (
	axis0 TEXT NOT NULL, 
	axis1 TEXT NOT NULL, 
	"values" TEXT NOT NULL, 
	PRIMARY KEY (axis0, axis1, "values")
);
