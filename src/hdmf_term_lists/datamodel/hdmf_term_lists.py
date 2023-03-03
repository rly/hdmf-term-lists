# Auto generated from hdmf_term_lists.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-03-03T15:32:13
# Schema: hdmf-term-lists
#
# id: https://w3id.org/hdmf-dev/hdmf-term-lists
# description: Example LinkML schema to demonstrate storage of term lists.
# license: MIT

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Float, String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
NCBITAXON = CurieNamespace('NCBITaxon', 'http://purl.obolibrary.org/obo/NCBITaxon_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
HDMF_TERM_LISTS = CurieNamespace('hdmf_term_lists', 'https://w3id.org/hdmf-dev/hdmf-term-lists/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OBO = CurieNamespace('obo', 'http://purl.obolibrary.org/obo/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = HDMF_TERM_LISTS


# Types

# Class references
class OneDimensionalSeriesName(extended_str):
    pass


class TimestampSeriesName(OneDimensionalSeriesName):
    pass


class ElectrodeSeriesName(OneDimensionalSeriesName):
    pass


Any = Any

@dataclass
class OneDimensionalSeries(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HDMF_TERM_LISTS.OneDimensionalSeries
    class_class_curie: ClassVar[str] = "hdmf_term_lists:OneDimensionalSeries"
    class_name: ClassVar[str] = "OneDimensionalSeries"
    class_model_uri: ClassVar[URIRef] = HDMF_TERM_LISTS.OneDimensionalSeries

    name: Union[str, OneDimensionalSeriesName] = None
    values: Union[Union[dict, Any], List[Union[dict, Any]]] = None
    data_type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, OneDimensionalSeriesName):
            self.name = OneDimensionalSeriesName(self.name)

        if self.data_type is not None and not isinstance(self.data_type, str):
            self.data_type = str(self.data_type)

        super().__post_init__(**kwargs)


@dataclass
class TwoDimensionalArray(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HDMF_TERM_LISTS.TwoDimensionalArray
    class_class_curie: ClassVar[str] = "hdmf_term_lists:TwoDimensionalArray"
    class_name: ClassVar[str] = "TwoDimensionalArray"
    class_model_uri: ClassVar[URIRef] = HDMF_TERM_LISTS.TwoDimensionalArray

    axis0: Union[dict, OneDimensionalSeries] = None
    axis1: Union[dict, OneDimensionalSeries] = None
    values: Union[Union[dict, Any], List[Union[dict, Any]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.axis0):
            self.MissingRequiredField("axis0")
        if not isinstance(self.axis0, OneDimensionalSeries):
            self.axis0 = OneDimensionalSeries(**as_dict(self.axis0))

        if self._is_empty(self.axis1):
            self.MissingRequiredField("axis1")
        if not isinstance(self.axis1, OneDimensionalSeries):
            self.axis1 = OneDimensionalSeries(**as_dict(self.axis1))

        super().__post_init__(**kwargs)


@dataclass
class TimestampSeries(OneDimensionalSeries):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HDMF_TERM_LISTS.TimestampSeries
    class_class_curie: ClassVar[str] = "hdmf_term_lists:TimestampSeries"
    class_name: ClassVar[str] = "TimestampSeries"
    class_model_uri: ClassVar[URIRef] = HDMF_TERM_LISTS.TimestampSeries

    name: Union[str, TimestampSeriesName] = None
    values: Union[float, List[float]] = None
    data_type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, TimestampSeriesName):
            self.name = TimestampSeriesName(self.name)

        if self._is_empty(self.values):
            self.MissingRequiredField("values")
        if not isinstance(self.values, list):
            self.values = [self.values] if self.values is not None else []
        self.values = [v if isinstance(v, float) else float(v) for v in self.values]

        if self.data_type is not None and not isinstance(self.data_type, str):
            self.data_type = str(self.data_type)

        super().__post_init__(**kwargs)


@dataclass
class Electrode(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HDMF_TERM_LISTS.Electrode
    class_class_curie: ClassVar[str] = "hdmf_term_lists:Electrode"
    class_name: ClassVar[str] = "Electrode"
    class_model_uri: ClassVar[URIRef] = HDMF_TERM_LISTS.Electrode

    name: Optional[str] = None
    impedance: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.impedance is not None and not isinstance(self.impedance, float):
            self.impedance = float(self.impedance)

        super().__post_init__(**kwargs)


@dataclass
class ElectrodeSeries(OneDimensionalSeries):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HDMF_TERM_LISTS.ElectrodeSeries
    class_class_curie: ClassVar[str] = "hdmf_term_lists:ElectrodeSeries"
    class_name: ClassVar[str] = "ElectrodeSeries"
    class_model_uri: ClassVar[URIRef] = HDMF_TERM_LISTS.ElectrodeSeries

    name: Union[str, ElectrodeSeriesName] = None
    values: Union[Union[dict, Electrode], List[Union[dict, Electrode]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ElectrodeSeriesName):
            self.name = ElectrodeSeriesName(self.name)

        if self._is_empty(self.values):
            self.MissingRequiredField("values")
        if not isinstance(self.values, list):
            self.values = [self.values] if self.values is not None else []
        self.values = [v if isinstance(v, Electrode) else Electrode(**as_dict(v)) for v in self.values]

        super().__post_init__(**kwargs)


@dataclass
class ElectricalArray(TwoDimensionalArray):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HDMF_TERM_LISTS.ElectricalArray
    class_class_curie: ClassVar[str] = "hdmf_term_lists:ElectricalArray"
    class_name: ClassVar[str] = "ElectricalArray"
    class_model_uri: ClassVar[URIRef] = HDMF_TERM_LISTS.ElectricalArray

    axis0: Union[dict, TimestampSeries] = None
    axis1: Union[dict, ElectrodeSeries] = None
    values: Union[float, List[float]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.axis0):
            self.MissingRequiredField("axis0")
        if not isinstance(self.axis0, TimestampSeries):
            self.axis0 = TimestampSeries(**as_dict(self.axis0))

        if self._is_empty(self.axis1):
            self.MissingRequiredField("axis1")
        if not isinstance(self.axis1, ElectrodeSeries):
            self.axis1 = ElectrodeSeries(**as_dict(self.axis1))

        if self._is_empty(self.values):
            self.MissingRequiredField("values")
        if not isinstance(self.values, list):
            self.values = [self.values] if self.values is not None else []
        self.values = [v if isinstance(v, float) else float(v) for v in self.values]

        super().__post_init__(**kwargs)


@dataclass
class Subject(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HDMF_TERM_LISTS.Subject
    class_class_curie: ClassVar[str] = "hdmf_term_lists:Subject"
    class_name: ClassVar[str] = "Subject"
    class_model_uri: ClassVar[URIRef] = HDMF_TERM_LISTS.Subject

    subject_id: Optional[str] = None
    sex: Optional[Union[str, "SubjectSex"]] = None
    species: Optional[Union[str, "SubjectSpecies"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject_id is not None and not isinstance(self.subject_id, str):
            self.subject_id = str(self.subject_id)

        if self.sex is not None and not isinstance(self.sex, SubjectSex):
            self.sex = SubjectSex(self.sex)

        if self.species is not None and not isinstance(self.species, SubjectSpecies):
            self.species = SubjectSpecies(self.species)

        super().__post_init__(**kwargs)


@dataclass
class NWBFile(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HDMF_TERM_LISTS.NWBFile
    class_class_curie: ClassVar[str] = "hdmf_term_lists:NWBFile"
    class_name: ClassVar[str] = "NWBFile"
    class_model_uri: ClassVar[URIRef] = HDMF_TERM_LISTS.NWBFile

    raw_ephys: Optional[Union[dict, ElectricalArray]] = None
    subject: Optional[Union[dict, Subject]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.raw_ephys is not None and not isinstance(self.raw_ephys, ElectricalArray):
            self.raw_ephys = ElectricalArray(**as_dict(self.raw_ephys))

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**as_dict(self.subject))

        super().__post_init__(**kwargs)


# Enumerations
class SubjectSex(EnumDefinitionImpl):

    MALE = PermissibleValue(text="MALE")
    FEMALE = PermissibleValue(text="FEMALE")

    _defn = EnumDefinition(
        name="SubjectSex",
    )

class SubjectSpecies(EnumDefinitionImpl):

    HOMO_SAPIENS = PermissibleValue(text="HOMO_SAPIENS",
                                               meaning=NCBITAXON["9606"])
    MUS_MUSCULUS = PermissibleValue(text="MUS_MUSCULUS",
                                               meaning=NCBITAXON["10090"])

    _defn = EnumDefinition(
        name="SubjectSpecies",
    )

# Slots
class slots:
    pass

slots.oneDimensionalSeries__name = Slot(uri=HDMF_TERM_LISTS.name, name="oneDimensionalSeries__name", curie=HDMF_TERM_LISTS.curie('name'),
                   model_uri=HDMF_TERM_LISTS.oneDimensionalSeries__name, domain=None, range=URIRef)

slots.oneDimensionalSeries__data_type = Slot(uri=HDMF_TERM_LISTS.data_type, name="oneDimensionalSeries__data_type", curie=HDMF_TERM_LISTS.curie('data_type'),
                   model_uri=HDMF_TERM_LISTS.oneDimensionalSeries__data_type, domain=None, range=Optional[str])

slots.oneDimensionalSeries__values = Slot(uri=HDMF_TERM_LISTS.values, name="oneDimensionalSeries__values", curie=HDMF_TERM_LISTS.curie('values'),
                   model_uri=HDMF_TERM_LISTS.oneDimensionalSeries__values, domain=None, range=Union[Union[dict, Any], List[Union[dict, Any]]])

slots.twoDimensionalArray__axis0 = Slot(uri=HDMF_TERM_LISTS.axis0, name="twoDimensionalArray__axis0", curie=HDMF_TERM_LISTS.curie('axis0'),
                   model_uri=HDMF_TERM_LISTS.twoDimensionalArray__axis0, domain=None, range=Union[dict, OneDimensionalSeries])

slots.twoDimensionalArray__axis1 = Slot(uri=HDMF_TERM_LISTS.axis1, name="twoDimensionalArray__axis1", curie=HDMF_TERM_LISTS.curie('axis1'),
                   model_uri=HDMF_TERM_LISTS.twoDimensionalArray__axis1, domain=None, range=Union[dict, OneDimensionalSeries])

slots.twoDimensionalArray__values = Slot(uri=HDMF_TERM_LISTS.values, name="twoDimensionalArray__values", curie=HDMF_TERM_LISTS.curie('values'),
                   model_uri=HDMF_TERM_LISTS.twoDimensionalArray__values, domain=None, range=Union[Union[dict, Any], List[Union[dict, Any]]])

slots.electrode__name = Slot(uri=HDMF_TERM_LISTS.name, name="electrode__name", curie=HDMF_TERM_LISTS.curie('name'),
                   model_uri=HDMF_TERM_LISTS.electrode__name, domain=None, range=Optional[str])

slots.electrode__impedance = Slot(uri=HDMF_TERM_LISTS.impedance, name="electrode__impedance", curie=HDMF_TERM_LISTS.curie('impedance'),
                   model_uri=HDMF_TERM_LISTS.electrode__impedance, domain=None, range=Optional[float])

slots.subject__subject_id = Slot(uri=HDMF_TERM_LISTS.subject_id, name="subject__subject_id", curie=HDMF_TERM_LISTS.curie('subject_id'),
                   model_uri=HDMF_TERM_LISTS.subject__subject_id, domain=None, range=Optional[str])

slots.subject__sex = Slot(uri=HDMF_TERM_LISTS.sex, name="subject__sex", curie=HDMF_TERM_LISTS.curie('sex'),
                   model_uri=HDMF_TERM_LISTS.subject__sex, domain=None, range=Optional[Union[str, "SubjectSex"]])

slots.subject__species = Slot(uri=HDMF_TERM_LISTS.species, name="subject__species", curie=HDMF_TERM_LISTS.curie('species'),
                   model_uri=HDMF_TERM_LISTS.subject__species, domain=None, range=Optional[Union[str, "SubjectSpecies"]])

slots.nWBFile__raw_ephys = Slot(uri=HDMF_TERM_LISTS.raw_ephys, name="nWBFile__raw_ephys", curie=HDMF_TERM_LISTS.curie('raw_ephys'),
                   model_uri=HDMF_TERM_LISTS.nWBFile__raw_ephys, domain=None, range=Optional[Union[dict, ElectricalArray]])

slots.nWBFile__subject = Slot(uri=HDMF_TERM_LISTS.subject, name="nWBFile__subject", curie=HDMF_TERM_LISTS.curie('subject'),
                   model_uri=HDMF_TERM_LISTS.nWBFile__subject, domain=None, range=Optional[Union[dict, Subject]])

slots.TimestampSeries_data_type = Slot(uri=HDMF_TERM_LISTS.data_type, name="TimestampSeries_data_type", curie=HDMF_TERM_LISTS.curie('data_type'),
                   model_uri=HDMF_TERM_LISTS.TimestampSeries_data_type, domain=TimestampSeries, range=Optional[str])

slots.TimestampSeries_values = Slot(uri=HDMF_TERM_LISTS.values, name="TimestampSeries_values", curie=HDMF_TERM_LISTS.curie('values'),
                   model_uri=HDMF_TERM_LISTS.TimestampSeries_values, domain=TimestampSeries, range=Union[float, List[float]])

slots.ElectrodeSeries_values = Slot(uri=HDMF_TERM_LISTS.values, name="ElectrodeSeries_values", curie=HDMF_TERM_LISTS.curie('values'),
                   model_uri=HDMF_TERM_LISTS.ElectrodeSeries_values, domain=ElectrodeSeries, range=Union[Union[dict, Electrode], List[Union[dict, Electrode]]])

slots.ElectricalArray_axis0 = Slot(uri=HDMF_TERM_LISTS.axis0, name="ElectricalArray_axis0", curie=HDMF_TERM_LISTS.curie('axis0'),
                   model_uri=HDMF_TERM_LISTS.ElectricalArray_axis0, domain=ElectricalArray, range=Union[dict, TimestampSeries])

slots.ElectricalArray_axis1 = Slot(uri=HDMF_TERM_LISTS.axis1, name="ElectricalArray_axis1", curie=HDMF_TERM_LISTS.curie('axis1'),
                   model_uri=HDMF_TERM_LISTS.ElectricalArray_axis1, domain=ElectricalArray, range=Union[dict, ElectrodeSeries])

slots.ElectricalArray_values = Slot(uri=HDMF_TERM_LISTS.values, name="ElectricalArray_values", curie=HDMF_TERM_LISTS.curie('values'),
                   model_uri=HDMF_TERM_LISTS.ElectricalArray_values, domain=ElectricalArray, range=Union[float, List[float]])