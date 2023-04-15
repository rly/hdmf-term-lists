from __future__ import annotations
from datetime import datetime, date
from enum import Enum
import numpy as np
from typing import List, Dict, Optional, Any, Union, Literal
from pydantic import BaseModel as BaseModel, Field
from linkml_runtime.linkml_model import Decimal

metamodel_version = "None"
version = "None"

class WeakRefShimBaseModel(BaseModel):
   __slots__ = '__weakref__'

class ConfiguredBaseModel(WeakRefShimBaseModel,
                validate_assignment = True,
                validate_all = True,
                underscore_attrs_are_private = True,
                extra = 'forbid',
                arbitrary_types_allowed = True):
    pass


class SubjectSex(str, Enum):

    MALE = "MALE"
    FEMALE = "FEMALE"



class SubjectSpecies(str, Enum):

    HOMO_SAPIENS = "HOMO_SAPIENS"
    MUS_MUSCULUS = "MUS_MUSCULUS"



class TimestampSeries(ConfiguredBaseModel):

    None



class IrregularlySampledTimestampSeries(TimestampSeries):

    name: Optional[str] = Field(None)
    values: np.ndarray = Field(None)



class RegularlySampledTimestampSeries(TimestampSeries):

    name: Optional[str] = Field(None)
    sampling_rate: float = Field(None)
    starting_time: float = Field(None)
    length: Optional[int] = Field(None)
    values: Optional[List[float]] = Field(default_factory=list)



class Electrode(ConfiguredBaseModel):

    name: Optional[str] = Field(None)
    impedance: Optional[float] = Field(None)



class ElectrodeSeries(ConfiguredBaseModel):

    name: Optional[str] = Field(None)
    values: List[Electrode] = Field(default_factory=list)



class ElectricalArray(ConfiguredBaseModel):

    time: TimestampSeries = Field(None)
    electrode: ElectrodeSeries = Field(None)
    values: np.ndarray = Field(None)



class IrregularlySampledElectricalArray(ElectricalArray):

    time: IrregularlySampledTimestampSeries = Field(None)
    electrode: ElectrodeSeries = Field(None)
    values: List[float] = Field(default_factory=list)



class RegularlySampledElectricalArray(ElectricalArray):

    time: Optional[RegularlySampledTimestampSeries] = Field(None)
    electrode: ElectrodeSeries = Field(None)
    values: List[float] = Field(default_factory=list)



class Subject(ConfiguredBaseModel):

    subject_id: Optional[str] = Field(None)
    sex: Optional[SubjectSex] = Field(None)
    species: Optional[SubjectSpecies] = Field(None)



class NWBFile(ConfiguredBaseModel):

    raw_ephys: Optional[IrregularlySampledElectricalArray] = Field(None)
    subject: Optional[Subject] = Field(None)




# Update forward refs
# see https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
TimestampSeries.update_forward_refs()
IrregularlySampledTimestampSeries.update_forward_refs()
RegularlySampledTimestampSeries.update_forward_refs()
Electrode.update_forward_refs()
ElectrodeSeries.update_forward_refs()
ElectricalArray.update_forward_refs()
IrregularlySampledElectricalArray.update_forward_refs()
RegularlySampledElectricalArray.update_forward_refs()
Subject.update_forward_refs()
NWBFile.update_forward_refs()

