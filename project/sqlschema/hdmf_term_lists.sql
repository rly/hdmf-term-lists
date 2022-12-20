

CREATE TABLE "ElectricalArray" (
	axis0 TEXT NOT NULL, 
	axis1 TEXT NOT NULL, 
	"values" FLOAT NOT NULL, 
	PRIMARY KEY (axis0, axis1, "values")
);

CREATE TABLE "Electrode" (
	impedance FLOAT, 
	PRIMARY KEY (impedance)
);

CREATE TABLE "ElectrodeSeries" (
	name TEXT NOT NULL, 
	data_type TEXT, 
	"values" TEXT NOT NULL, 
	PRIMARY KEY (name, data_type, "values")
);

CREATE TABLE "OneDimensionalSeries" (
	name TEXT NOT NULL, 
	data_type TEXT, 
	"values" TEXT NOT NULL, 
	PRIMARY KEY (name, data_type, "values")
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
