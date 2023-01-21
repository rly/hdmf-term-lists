from hdmf_term_lists.datamodel.hdmf_term_lists import NWBFile, Subject, SubjectSex, SubjectSpecies
from linkml_runtime.dumpers import json_dumper
import unittest

class TestNWBFile(unittest.TestCase):

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

        json_out = json_dumper.dumps(subject)
        self.assertEqual(json_out,
"""{
  "subject_id": "MySubject001",
  "sex": "FEMALE",
  "species": "HOMO_SAPIENS",
  "@type": "Subject"
}"""     )
