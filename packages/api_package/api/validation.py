from marshmallow import Schema, fields
from marshmallow import ValidationError

import typing as t
import json


class InvalidInputError(Exception):
    """Invalid model input."""


class DataRequestSchema(Schema):
    form_id = fields.Integer()
    views = fields.Integer()
    submissions = fields.Integer()
    feat_01 = fields.Float()
    feat_02 = fields.Float()
    feat_03 = fields.Float()
    feat_04 = fields.Float()
    feat_05 = fields.Float()
    feat_06 = fields.Float()
    feat_07 = fields.Float()
    feat_08 = fields.Float()
    feat_09 = fields.Float()
    feat_10 = fields.Float()
    feat_11 = fields.Float()
    feat_12 = fields.Float()
    feat_13 = fields.Float()
    feat_14 = fields.Float()
    feat_15 = fields.Float()
    feat_16 = fields.Float()
    feat_17 = fields.Float()
    feat_18 = fields.Float()
    feat_19 = fields.Float()
    feat_20 = fields.Float()
    feat_21 = fields.Float()
    feat_22 = fields.Float()
    feat_23 = fields.Float()
    feat_24 = fields.Float()
    feat_25 = fields.Float()
    feat_26 = fields.Float()
    feat_27 = fields.Float()
    feat_28 = fields.Float()
    feat_29 = fields.Float()
    feat_30 = fields.Float()
    feat_31 = fields.Float()
    feat_32 = fields.Float()
    feat_33 = fields.Float()
    feat_34 = fields.Float()
    feat_35 = fields.Float()
    feat_36 = fields.Float()
    feat_37 = fields.Float()
    feat_38 = fields.Float()
    feat_39 = fields.Float()
    feat_40 = fields.Float()
    feat_41 = fields.Float()
    feat_42 = fields.Float()
    feat_43 = fields.Float()
    feat_44 = fields.Float()
    feat_45 = fields.Float()
    feat_46 = fields.Float()
    feat_47 = fields.Float()


def _filter_error_rows(errors: dict, validated_input: t.List[dict]) -> t.List[dict]:
    """Remove input data rows with errors."""

    indexes = errors.keys()
    # delete them in reverse order so that you
    # don't throw off the subsequent indexes.
    for index in sorted(indexes, reverse=True):
        if index == "_schema":
            continue
        del validated_input[index]

    return validated_input


def validate_inputs(input_data):
    """Check prediction inputs against schema."""

    # set many=True to allow passing in a list
    schema = DataRequestSchema(strict=True, many=True)

    if isinstance(input_data, str):
        input_data = json.loads(input_data)
    # # convert syntax error field names (beginning with numbers)
    # for dict in input_data:
    #     for key, value in SYNTAX_ERROR_FIELD_MAP.items():
    #         dict[value] = dict[key]
    #         del dict[key]

    errors = None
    try:
        schema.load(input_data)
    except ValidationError as exc:
        errors = exc.messages

    # # convert syntax error field names back
    # # this is a hack - never name your data
    # # fields with numbers as the first letter.
    # for dict in input_data:
    #     for key, value in SYNTAX_ERROR_FIELD_MAP.items():
    #         dict[key] = dict[value]
    #         del dict[value]

    if errors:

        print(errors)
        validated_input = _filter_error_rows(errors=errors, validated_input=input_data)
    else:
        validated_input = input_data

    return validated_input, errors
