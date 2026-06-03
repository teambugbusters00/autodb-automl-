import pytest
from autohf.core.config import AutoHFConfig, PipelineState


def test_config_defaults():
    config = AutoHFConfig()
    assert config.preset == "medium_quality"
    assert config.time_limit == 300
    assert config.max_dataset_rows == 50000
    assert config.router == "auto"


def test_config_from_preset():
    config = AutoHFConfig.from_preset("quick_prototype", time_limit=120)
    assert config.preset == "quick_prototype"
    assert config.time_limit == 120
    assert config.max_dataset_rows == 10000
