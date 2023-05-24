from copy import deepcopy
from typing import Any, Dict, Optional

from kedro.framework.context import KedroContext
from kedro.framework.hooks import hook_impl
from kedro.io import DataCatalog
from kedro.pipeline.node import Node

# we wish to dynamically generate the outputs for a node to make it dynamic


class ProjectHooks:
    def __init__(self):
        self.params = None
        # self.raw_download_node_outputs = None

    @hook_impl
    def after_context_created(
        self,
        context: KedroContext,
    ) -> None:
        self.params = deepcopy(context.params)
        # print(f"PRINTED PARAMS: {self.params}")

    # @hook_impl
    # def before_pipeline_run(
    #         self,
    #         context: KedroContext,
    # ) -> None:

    @hook_impl
    def before_node_run(  # pylint: disable=too-many-arguments
        self,
        node: Node,
        catalog: DataCatalog,
        inputs: Dict[str, Any],
        is_async: bool,
        session_id: str,
    ) -> Optional[Dict[str, Any]]:
        pass
        # the following hook can be used to set the output datasets as
        # the parameters to enable dynamically selecting outputs based on inputs
        # print(self.params)

        # if "raw_download_node" in node.name:
        #     namespace = node.name.split(".")[0]
        #     datasets = self.params[namespace]["raw_datasets"]
        #     output_datasets = [namespace + "." + data for data in datasets]
        #     node._outputs = output_datasets
        #     self.raw_download_node_outputs = output_datasets

        # if "intermediate_node" in node.name:
        #     # node.inputs = self.raw_download_node_outputs
        #     print(f"INTERMEDIATE NODE {node._inputs}")
        #     # then loop through each of the outputs and apply the name changes and
        #     # datatype assignemnts in the intermediate file
        #     # consider only defining columns that are not float
        #     - considering the bulk of our data are floats
        #     #node._outputs = output_datasets
