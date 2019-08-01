import unittest
import vnf_bd as vnf_bd
import yaml
import os
import pyangbind.lib.pybindJSON as pybindJSON

MODEL_NAME = "vnf_bd"
EXAMPLE_DIR = "examples/"


def check_against_model(yaml_path):
    """
    Open a given YAML file and tries to load it into
    model that was generated by pyangbind.
    Fails if the YAML file is not compatible to the
    model.
    """
    with open(yaml_path, "r") as f:
        vnf_bd_data = yaml.load(f)
        vnf_bd_model = pybindJSON.loads_ietf(
            vnf_bd_data, vnf_bd, MODEL_NAME)
        #  print(ped_model.ped.name)  # example how to use model
        return vnf_bd_model


class TestStringMethods(unittest.TestCase):

    def test_example_vnf_bds_against_model(self):
        # collect all example vnf_bd files which should be checked against model
        example_vnf_bds = os.listdir(EXAMPLE_DIR)
        # check each vnf_bd file against the model
        print("Validating: {} VNF-BD files.".format(len(example_vnf_bds)))
        for ep in example_vnf_bds:
            self.assertIsNotNone(
                check_against_model(os.path.join(EXAMPLE_DIR, ep)))
            print("File: '{}' is valid against model '{}'."
                .format(ep, MODEL_NAME))

    def test_example_vnf_bds_dump_json(self):
        example_vnf_bds = os.listdir(EXAMPLE_DIR)
        # check each vnf_bd file against the model
        print("Validating: {} VNF-BD files.".format(len(example_vnf_bds)))
        for ep in example_vnf_bds:
            parsed_vnfbd = check_against_model(os.path.join(EXAMPLE_DIR, ep))
            print(pybindJSON.dumps(parsed_vnfbd))