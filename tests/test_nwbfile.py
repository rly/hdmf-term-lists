from hdmf_term_lists.datamodel.nwb_electrical_array import \
  (NWBFile, Subject, SubjectSex, SubjectSpecies, ElectricalArray, IrregularlySampledTimestampSeries,
   Electrode, ElectrodeSeries)
from linkml_runtime.dumpers import json_dumper
import numpy as np
import unittest


class TestNWBFile(unittest.TestCase):

    def test_irreg_timestamp_series(self):
        time_series = IrregularlySampledTimestampSeries(
            name="time",
            values=np.array([0.0, 1.0]),
        )
        self.assertEqual(time_series.name, "time")
        np.testing.assert_equal(time_series.values, np.array([0.0, 1.0]))

    def test_electrical_array(self):
        time_series = IrregularlySampledTimestampSeries(
          name="time",
          values=np.array([0.0, 1.0]),
        )
        elec1 = Electrode(
            name="elec1",
            impedance=0.1,
        )
        elec2 = Electrode(
            name="elec2",
            impedance=0.2,
        )
        electrode_series = ElectrodeSeries(
            name="electrode_series",
            values=[elec1, elec2],
        )
        electrical_array = ElectricalArray(
          time=time_series,
          electrode=electrode_series,
          values=np.array([[0.1, 0.2], [0.3, 0.4]]),
        )
        self.assertEqual(electrical_array.time, time_series)
        self.assertEqual(electrical_array.electrode, electrode_series)
        np.testing.assert_equal(electrical_array.values, np.array([[0.1, 0.2], [0.3, 0.4]]))



    def test_subject(self):
        subject = Subject(
            subject_id="MySubject001",
            sex="FEMALE",
            species="HOMO_SAPIENS"
        )
        assert subject.subject_id == "MySubject001"
        # self.assertEqual(subject.sex, SubjectSex.FEMALE)  # will be allowed soon
        self.assertEqual(subject.sex, SubjectSex(SubjectSex.FEMALE))
        self.assertEqual(subject.species, SubjectSpecies(SubjectSpecies.HOMO_SAPIENS))

        # expected = {
        #     'subject_id': 'MySubject001',
        #     'sex': (SubjectSex.FEMALE),
        #     'species': SubjectSpecies(SubjectSpecies.HOMO_SAPIENS)
        # }
        # self.assertEqual(subject.dict(), expected)

#         json_out = json_dumper.dumps(subject)
#         self.assertEqual(json_out,
# """{
#   "subject_id": "MySubject001",
#   "sex": "FEMALE",
#   "species": "HOMO_SAPIENS",
#   "@type": "Subject"
# }"""     )
