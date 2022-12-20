# Auto generated from hdmf_term_lists.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-12-20T12:56:23
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


@dataclass
class OneDimensionalSeries(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HDMF_TERM_LISTS.OneDimensionalSeries
    class_class_curie: ClassVar[str] = "hdmf_term_lists:OneDimensionalSeries"
    class_name: ClassVar[str] = "OneDimensionalSeries"
    class_model_uri: ClassVar[URIRef] = HDMF_TERM_LISTS.OneDimensionalSeries

    name: Union[str, OneDimensionalSeriesName] = None
    values: Union[str, List[str]] = None
    data_type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, OneDimensionalSeriesName):
            self.name = OneDimensionalSeriesName(self.name)

        if self._is_empty(self.values):
            self.MissingRequiredField("values")
        if not isinstance(self.values, list):
            self.values = [self.values] if self.values is not None else []
        self.values = [v if isinstance(v, str) else str(v) for v in self.values]

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

    axis0: Union[str, OneDimensionalSeriesName] = None
    axis1: Union[str, OneDimensionalSeriesName] = None
    values: Union[str, List[str]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.axis0):
            self.MissingRequiredField("axis0")
        if not isinstance(self.axis0, OneDimensionalSeriesName):
            self.axis0 = OneDimensionalSeriesName(self.axis0)

        if self._is_empty(self.axis1):
            self.MissingRequiredField("axis1")
        if not isinstance(self.axis1, OneDimensionalSeriesName):
            self.axis1 = OneDimensionalSeriesName(self.axis1)

        if self._is_empty(self.values):
            self.MissingRequiredField("values")
        if not isinstance(self.values, list):
            self.values = [self.values] if self.values is not None else []
        self.values = [v if isinstance(v, str) else str(v) for v in self.values]

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

    impedance: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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

    axis0: Union[str, TimestampSeriesName] = None
    axis1: Union[str, ElectrodeSeriesName] = None
    values: Union[float, List[float]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.axis0):
            self.MissingRequiredField("axis0")
        if not isinstance(self.axis0, TimestampSeriesName):
            self.axis0 = TimestampSeriesName(self.axis0)

        if self._is_empty(self.axis1):
            self.MissingRequiredField("axis1")
        if not isinstance(self.axis1, ElectrodeSeriesName):
            self.axis1 = ElectrodeSeriesName(self.axis1)

        if self._is_empty(self.values):
            self.MissingRequiredField("values")
        if not isinstance(self.values, list):
            self.values = [self.values] if self.values is not None else []
        self.values = [v if isinstance(v, float) else float(v) for v in self.values]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.oneDimensionalSeries__name = Slot(uri=HDMF_TERM_LISTS.name, name="oneDimensionalSeries__name", curie=HDMF_TERM_LISTS.curie('name'),
                   model_uri=HDMF_TERM_LISTS.oneDimensionalSeries__name, domain=None, range=URIRef)

slots.oneDimensionalSeries__data_type = Slot(uri=HDMF_TERM_LISTS.data_type, name="oneDimensionalSeries__data_type", curie=HDMF_TERM_LISTS.curie('data_type'),
                   model_uri=HDMF_TERM_LISTS.oneDimensionalSeries__data_type, domain=None, range=Optional[str])

slots.oneDimensionalSeries__values = Slot(uri=HDMF_TERM_LISTS.values, name="oneDimensionalSeries__values", curie=HDMF_TERM_LISTS.curie('values'),
                   model_uri=HDMF_TERM_LISTS.oneDimensionalSeries__values, domain=None, range=Union[str, List[str]])

slots.twoDimensionalArray__axis0 = Slot(uri=HDMF_TERM_LISTS.axis0, name="twoDimensionalArray__axis0", curie=HDMF_TERM_LISTS.curie('axis0'),
                   model_uri=HDMF_TERM_LISTS.twoDimensionalArray__axis0, domain=None, range=Union[str, OneDimensionalSeriesName])

slots.twoDimensionalArray__axis1 = Slot(uri=HDMF_TERM_LISTS.axis1, name="twoDimensionalArray__axis1", curie=HDMF_TERM_LISTS.curie('axis1'),
                   model_uri=HDMF_TERM_LISTS.twoDimensionalArray__axis1, domain=None, range=Union[str, OneDimensionalSeriesName])

slots.twoDimensionalArray__values = Slot(uri=HDMF_TERM_LISTS.values, name="twoDimensionalArray__values", curie=HDMF_TERM_LISTS.curie('values'),
                   model_uri=HDMF_TERM_LISTS.twoDimensionalArray__values, domain=None, range=Union[str, List[str]])

slots.electrode__impedance = Slot(uri=HDMF_TERM_LISTS.impedance, name="electrode__impedance", curie=HDMF_TERM_LISTS.curie('impedance'),
                   model_uri=HDMF_TERM_LISTS.electrode__impedance, domain=None, range=Optional[float])

slots.TimestampSeries_data_type = Slot(uri=HDMF_TERM_LISTS.data_type, name="TimestampSeries_data_type", curie=HDMF_TERM_LISTS.curie('data_type'),
                   model_uri=HDMF_TERM_LISTS.TimestampSeries_data_type, domain=TimestampSeries, range=Optional[str])

slots.TimestampSeries_values = Slot(uri=HDMF_TERM_LISTS.values, name="TimestampSeries_values", curie=HDMF_TERM_LISTS.curie('values'),
                   model_uri=HDMF_TERM_LISTS.TimestampSeries_values, domain=TimestampSeries, range=Union[float, List[float]])

slots.ElectrodeSeries_values = Slot(uri=HDMF_TERM_LISTS.values, name="ElectrodeSeries_values", curie=HDMF_TERM_LISTS.curie('values'),
                   model_uri=HDMF_TERM_LISTS.ElectrodeSeries_values, domain=ElectrodeSeries, range=Union[Union[dict, Electrode], List[Union[dict, Electrode]]])

slots.ElectricalArray_axis0 = Slot(uri=HDMF_TERM_LISTS.axis0, name="ElectricalArray_axis0", curie=HDMF_TERM_LISTS.curie('axis0'),
                   model_uri=HDMF_TERM_LISTS.ElectricalArray_axis0, domain=ElectricalArray, range=Union[str, TimestampSeriesName])

slots.ElectricalArray_axis1 = Slot(uri=HDMF_TERM_LISTS.axis1, name="ElectricalArray_axis1", curie=HDMF_TERM_LISTS.curie('axis1'),
                   model_uri=HDMF_TERM_LISTS.ElectricalArray_axis1, domain=ElectricalArray, range=Union[str, ElectrodeSeriesName])

slots.ElectricalArray_values = Slot(uri=HDMF_TERM_LISTS.values, name="ElectricalArray_values", curie=HDMF_TERM_LISTS.curie('values'),
                   model_uri=HDMF_TERM_LISTS.ElectricalArray_values, domain=ElectricalArray, range=Union[float, List[float]])