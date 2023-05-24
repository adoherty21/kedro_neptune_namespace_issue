from kedro.pipeline import Pipeline, node, pipeline

from ..nodes.common_node_01_raw import read_raw_data


def create_raw_pipeline() -> Pipeline:
    nodes = [
        node(
            # use partial to pass the string dataset
            # update wrapper to avoid warnings and to improve logging
            func=read_raw_data,
            inputs=["params:raw.column_name"],# "neptune_run"],
            outputs=f"data_raw",
        )
    ]

    return pipeline(nodes, tags="to_raw")
