import pytest
from rayforge.core.forge_engine import Forge

forge = Forge()

def test_pull_model():
    model_info = forge.pull("distilbert-base-uncased-finetuned-sst-2-english", source="huggingface")
    assert model_info["source"] == "huggingface"
    assert "task" in model_info

def test_run_inference():
    model_info = forge.pull("distilbert-base-uncased-finetuned-sst-2-english", source="huggingface")
    output = forge.run(model_info, "I love this!")
    assert isinstance(output, str) or isinstance(output, dict)
    assert len(str(output)) > 0

def test_invalid_model():
    with pytest.raises(Exception):
        forge.pull("non-existent-model-id-xyz", source="huggingface")
