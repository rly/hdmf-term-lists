# Auto generated from hdmf_term_lists_conforms_to.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-03-03T15:32:44
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
from linkml_runtime.linkml_model.types import Float, Integer, String

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
class IrregularlySampledTimestampSeriesName(extended_str):
    pass


class RegularlySampledTimestampSeriesName(extended_str):
    pass


class ElectrodeSeriesName(extended_str):
    pass


class TimestampSeries(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HDMF_TERM_LISTS.TimestampSeries
    class_class_curie: ClassVar[str] = "hdmf_term_lists:TimestampSeries"
    class_name: ClassVar[str] = "TimestampSeries"
    class_model_uri: ClassVar[URIRef] = HDMF_TERM_LISTS.TimestampSeries


@dataclass
class IrregularlySampledTimestampSeries(TimestampSeries):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HDMF_TERM_LISTS.IrregularlySampledTimestampSeries
    class_class_curie: ClassVar[str] = "hdmf_term_lists:IrregularlySampledTimestampSeries"
    class_name: ClassVar[str] = "IrregularlySampledTimestampSeries"
    class_model_uri: ClassVar[URIRef] = HDMF_TERM_LISTS.IrregularlySampledTimestampSeries

    name: Union[str, IrregularlySampledTimestampSeriesName] = None
    values: Union[float, List[float]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, IrregularlySampledTimestampSeriesName):
            self.name = IrregularlySampledTimestampSeriesName(self.name)

        if self._is_empty(self.values):
            self.MissingRequiredField("values")
        if not isinstance(self.values, list):
            self.values = [self.values] if self.values is not None else []
        self.values = [v if isinstance(v, float) else float(v) for v in self.values]

        super().__post_init__(**kwargs)


@dataclass
class RegularlySampledTimestampSeries(TimestampSeries):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HDMF_TERM_LISTS.RegularlySampledTimestampSeries
    class_class_curie: ClassVar[str] = "hdmf_term_lists:RegularlySampledTimestampSeries"
    class_name: ClassVar[str] = "RegularlySampledTimestampSeries"
    class_model_uri: ClassVar[URIRef] = HDMF_TERM_LISTS.RegularlySampledTimestampSeries

    name: Union[str, RegularlySampledTimestampSeriesName] = None
    sampling_rate: float = None
    starting_time: float = None
    length: Optional[int] = None
    values: Optional[Union[float, List[float]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, RegularlySampledTimestampSeriesName):
            self.name = RegularlySampledTimestampSeriesName(self.name)

        if self._is_empty(self.sampling_rate):
            self.MissingRequiredField("sampling_rate")
        if not isinstance(self.sampling_rate, float):
            self.sampling_rate = float(self.sampling_rate)

        if self._is_empty(self.starting_time):
            self.MissingRequiredField("starting_time")
        if not isinstance(self.starting_time, float):
            self.starting_time = float(self.starting_time)

        if self.length is not None and not isinstance(self.length, int):
            self.length = int(self.length)

        if not isinstance(self.values, list):
            self.values = [self.values] if self.values is not None else []
        self.values = [v if isinstance(v, float) else float(v) for v in self.values]

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
class ElectrodeSeries(YAMLRoot):
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
class ElectricalArray(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HDMF_TERM_LISTS.ElectricalArray
    class_class_curie: ClassVar[str] = "hdmf_term_lists:ElectricalArray"
    class_name: ClassVar[str] = "ElectricalArray"
    class_model_uri: ClassVar[URIRef] = HDMF_TERM_LISTS.ElectricalArray

    time: Optional[Union[dict, TimestampSeries]] = None
    electrode: Optional[Union[str, ElectrodeSeriesName]] = None
    values: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.time is not None and not isinstance(self.time, TimestampSeries):
            self.time = TimestampSeries()

        if self.electrode is not None and not isinstance(self.electrode, ElectrodeSeriesName):
            self.electrode = ElectrodeSeriesName(self.electrode)

        if self.values is not None and not isinstance(self.values, float):
            self.values = float(self.values)

        super().__post_init__(**kwargs)


@dataclass
class IrregularlySampledElectricalArray(ElectricalArray):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HDMF_TERM_LISTS.IrregularlySampledElectricalArray
    class_class_curie: ClassVar[str] = "hdmf_term_lists:IrregularlySampledElectricalArray"
    class_name: ClassVar[str] = "IrregularlySampledElectricalArray"
    class_model_uri: ClassVar[URIRef] = HDMF_TERM_LISTS.IrregularlySampledElectricalArray

    time: Optional[Union[str, IrregularlySampledTimestampSeriesName]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.time is not None and not isinstance(self.time, IrregularlySampledTimestampSeriesName):
            self.time = IrregularlySampledTimestampSeriesName(self.time)

        super().__post_init__(**kwargs)


@dataclass
class RegularlySampledElectricalArray(ElectricalArray):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HDMF_TERM_LISTS.RegularlySampledElectricalArray
    class_class_curie: ClassVar[str] = "hdmf_term_lists:RegularlySampledElectricalArray"
    class_name: ClassVar[str] = "RegularlySampledElectricalArray"
    class_model_uri: ClassVar[URIRef] = HDMF_TERM_LISTS.RegularlySampledElectricalArray

    time: Optional[Union[str, RegularlySampledTimestampSeriesName]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.time is not None and not isinstance(self.time, RegularlySampledTimestampSeriesName):
            self.time = RegularlySampledTimestampSeriesName(self.time)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.irregularlySampledTimestampSeries__name = Slot(uri=HDMF_TERM_LISTS.name, name="irregularlySampledTimestampSeries__name", curie=HDMF_TERM_LISTS.curie('name'),
                   model_uri=HDMF_TERM_LISTS.irregularlySampledTimestampSeries__name, domain=None, range=URIRef)

slots.irregularlySampledTimestampSeries__values = Slot(uri=HDMF_TERM_LISTS.values, name="irregularlySampledTimestampSeries__values", curie=HDMF_TERM_LISTS.curie('values'),
                   model_uri=HDMF_TERM_LISTS.irregularlySampledTimestampSeries__values, domain=None, range=Union[float, List[float]])

slots.regularlySampledTimestampSeries__name = Slot(uri=HDMF_TERM_LISTS.name, name="regularlySampledTimestampSeries__name", curie=HDMF_TERM_LISTS.curie('name'),
                   model_uri=HDMF_TERM_LISTS.regularlySampledTimestampSeries__name, domain=None, range=URIRef)

slots.regularlySampledTimestampSeries__sampling_rate = Slot(uri=HDMF_TERM_LISTS.sampling_rate, name="regularlySampledTimestampSeries__sampling_rate", curie=HDMF_TERM_LISTS.curie('sampling_rate'),
                   model_uri=HDMF_TERM_LISTS.regularlySampledTimestampSeries__sampling_rate, domain=None, range=float)

slots.regularlySampledTimestampSeries__starting_time = Slot(uri=HDMF_TERM_LISTS.starting_time, name="regularlySampledTimestampSeries__starting_time", curie=HDMF_TERM_LISTS.curie('starting_time'),
                   model_uri=HDMF_TERM_LISTS.regularlySampledTimestampSeries__starting_time, domain=None, range=float)

slots.regularlySampledTimestampSeries__length = Slot(uri=HDMF_TERM_LISTS.length, name="regularlySampledTimestampSeries__length", curie=HDMF_TERM_LISTS.curie('length'),
                   model_uri=HDMF_TERM_LISTS.regularlySampledTimestampSeries__length, domain=None, range=Optional[int])

slots.regularlySampledTimestampSeries__values = Slot(uri=HDMF_TERM_LISTS.values, name="regularlySampledTimestampSeries__values", curie=HDMF_TERM_LISTS.curie('values'),
                   model_uri=HDMF_TERM_LISTS.regularlySampledTimestampSeries__values, domain=None, range=Optional[Union[float, List[float]]])

slots.electrode__name = Slot(uri=HDMF_TERM_LISTS.name, name="electrode__name", curie=HDMF_TERM_LISTS.curie('name'),
                   model_uri=HDMF_TERM_LISTS.electrode__name, domain=None, range=Optional[str])

slots.electrode__impedance = Slot(uri=HDMF_TERM_LISTS.impedance, name="electrode__impedance", curie=HDMF_TERM_LISTS.curie('impedance'),
                   model_uri=HDMF_TERM_LISTS.electrode__impedance, domain=None, range=Optional[float])

slots.electrodeSeries__name = Slot(uri=HDMF_TERM_LISTS.name, name="electrodeSeries__name", curie=HDMF_TERM_LISTS.curie('name'),
                   model_uri=HDMF_TERM_LISTS.electrodeSeries__name, domain=None, range=URIRef)

slots.electrodeSeries__values = Slot(uri=HDMF_TERM_LISTS.values, name="electrodeSeries__values", curie=HDMF_TERM_LISTS.curie('values'),
                   model_uri=HDMF_TERM_LISTS.electrodeSeries__values, domain=None, range=Union[Union[dict, Electrode], List[Union[dict, Electrode]]])

slots.electricalArray__time = Slot(uri=HDMF_TERM_LISTS.time, name="electricalArray__time", curie=HDMF_TERM_LISTS.curie('time'),
                   model_uri=HDMF_TERM_LISTS.electricalArray__time, domain=None, range=Optional[Union[dict, TimestampSeries]])

slots.electricalArray__electrode = Slot(uri=HDMF_TERM_LISTS.electrode, name="electricalArray__electrode", curie=HDMF_TERM_LISTS.curie('electrode'),
                   model_uri=HDMF_TERM_LISTS.electricalArray__electrode, domain=None, range=Optional[Union[str, ElectrodeSeriesName]])

slots.electricalArray__values = Slot(uri=HDMF_TERM_LISTS.values, name="electricalArray__values", curie=HDMF_TERM_LISTS.curie('values'),
                   model_uri=HDMF_TERM_LISTS.electricalArray__values, domain=None, range=Optional[float])

slots.IrregularlySampledElectricalArray_time = Slot(uri=HDMF_TERM_LISTS.time, name="IrregularlySampledElectricalArray_time", curie=HDMF_TERM_LISTS.curie('time'),
                   model_uri=HDMF_TERM_LISTS.IrregularlySampledElectricalArray_time, domain=IrregularlySampledElectricalArray, range=Optional[Union[str, IrregularlySampledTimestampSeriesName]])

slots.RegularlySampledElectricalArray_time = Slot(uri=HDMF_TERM_LISTS.time, name="RegularlySampledElectricalArray_time", curie=HDMF_TERM_LISTS.curie('time'),
                   model_uri=HDMF_TERM_LISTS.RegularlySampledElectricalArray_time, domain=RegularlySampledElectricalArray, range=Optional[Union[str, RegularlySampledTimestampSeriesName]])