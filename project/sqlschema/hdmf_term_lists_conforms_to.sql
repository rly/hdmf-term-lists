

CREATE TABLE "ElectricalArray" (
	time TEXT, 
	electrode TEXT, 
	"values" FLOAT, 
	PRIMARY KEY (time, electrode, "values")
);

CREATE TABLE "Electrode" (
	name TEXT, 
	impedance FLOAT, 
	PRIMARY KEY (name, impedance)
);

CREATE TABLE "ElectrodeSeries" (
	name TEXT NOT NULL, 
	"values" TEXT NOT NULL, 
	PRIMARY KEY (name, "values")
);

CREATE TABLE "IrregularlySampledElectricalArray" (
	electrode TEXT, 
	"values" FLOAT, 
	time TEXT, 
	PRIMARY KEY (electrode, "values", time)
);

CREATE TABLE "IrregularlySampledTimestampSeries" (
	name TEXT NOT NULL, 
	"values" FLOAT NOT NULL, 
	PRIMARY KEY (name, "values")
);

CREATE TABLE "RegularlySampledElectricalArray" (
	electrode TEXT, 
	"values" FLOAT, 
	time TEXT, 
	PRIMARY KEY (electrode, "values", time)
);

CREATE TABLE "RegularlySampledTimestampSeries" (
	name TEXT NOT NULL, 
	sampling_rate FLOAT NOT NULL, 
	starting_time FLOAT NOT NULL, 
	length INTEGER, 
	"values" FLOAT, 
	PRIMARY KEY (name, sampling_rate, starting_time, length, "values")
);
