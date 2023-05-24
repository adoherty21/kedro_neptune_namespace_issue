from kedro.pipeline import Pipeline, pipeline

# common pipeline import
from ...common.pipelines.common_pipeline_01_raw import create_raw_pipeline


def create_pipeline() -> Pipeline:

    raw_pipeline = create_raw_pipeline()

    return pipeline(
        raw_pipeline,
        namespace="namespace_1",
    )
