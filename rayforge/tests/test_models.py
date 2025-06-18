import pytest
from rayforge.models.wrapper import wrap_model

def test_hf_text_classification_wrapper():
    model_info = {
        "id": "distilbert-base-uncased-finetuned-sst-2-english",
        "source": "huggingface",
        "task": "text-classification"
    }

    wrapper = wrap_model(model_info)
    output = wrapper("This is a great product.")
    assert isinstance(output, str) or isinstance(output, dict)

def test_missing_model_task():
    model_info = {
        "id": "distilbert-base-uncased",
        "source": "huggingface",
        "task": None
    }

    with pytest.raises(ValueError):
        wrap_model(model_info)
