# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

PACKAGE_NAME = "fn_tenable_io_assets"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'tenable_io_assets''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("tenable_io_assets")
    def _tenable_io_assets_function(self, event, *args, **kwargs):
        """Function: Function for multiple operations:
- Gets Asset data from Tenable.io.
- Invoke Tenable.io Vulnerability scan for the Asset(s)."""
        try:

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'tenable_io_assets' running in workflow '{0}'".format(wf_instance_id))

            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            artifact_id = kwargs.get("artifact_id")  # number
            tio_operation_type = kwargs.get("tio_operation_type")  # text
            tio_operation_param1 = kwargs.get("tio_operation_param1")  # text
            tio_operation_param2 = kwargs.get("tio_operation_param2")  # text

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("artifact_id: %s", artifact_id)
            log.info("tio_operation_type: %s", tio_operation_type)
            log.info("tio_operation_param1: %s", tio_operation_param1)
            log.info("tio_operation_param2: %s", tio_operation_param2)

            ##############################################
            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE #
            ##############################################

            yield StatusMessage("Finished 'tenable_io_assets' that was running in workflow '{0}'".format(wf_instance_id))

            results = {
                "content": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
