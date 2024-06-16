# coding: utf-8

"""
    comfyui
    No description provided (generated by Openapi JSON Schema Generator https://github.com/openapi-json-schema-tools/openapi-json-schema-generator)  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from comfy.api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema

from comfy.api.paths.view.get.parameters.parameter_0 import schema
from comfy.api.paths.view.get.parameters.parameter_1 import schema as schema_3
from comfy.api.paths.view.get.parameters.parameter_2 import schema as schema_2


class Properties(typing.TypedDict):
    filename: typing.Type[schema.Schema]
    subfolder: typing.Type[schema_2.Schema]
    type: typing.Type[schema_3.Schema]

class QueryParametersRequiredDictInput(typing.TypedDict):
    filename: str

class QueryParametersOptionalDictInput(typing.TypedDict, total=False):
    subfolder: str
    type: typing.Literal["output", "input", "temp"]


class QueryParametersDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "filename",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "subfolder",
        "type",
    })
    
    def __new__(
        cls,
        *,
        filename: str,
        subfolder: typing.Union[
            str,
            schemas.Unset
        ] = schemas.unset,
        type: typing.Union[
            typing.Literal[
                "output",
                "input",
                "temp"
            ],
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
    ):
        arg_: typing.Dict[str, typing.Any] = {
            "filename": filename,
        }
        for key_, val in (
            ("subfolder", subfolder),
            ("type", type),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key_] = val
        used_arg_ = typing.cast(QueryParametersDictInput, arg_)
        return QueryParameters.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> QueryParametersDict:
        return QueryParameters.validate(arg, configuration=configuration)
    
    @property
    def filename(self) -> str:
        return typing.cast(
            str,
            self.__getitem__("filename")
        )
    
    @property
    def subfolder(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("subfolder", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )
    
    @property
    def type(self) -> typing.Union[typing.Literal["output", "input", "temp"], schemas.Unset]:
        val = self.get("type", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            typing.Literal["output", "input", "temp"],
            val
        )


class QueryParametersDictInput(QueryParametersRequiredDictInput, QueryParametersOptionalDictInput):
    pass


@dataclasses.dataclass(frozen=True)
class QueryParameters(
    schemas.Schema[QueryParametersDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "filename",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: QueryParametersDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> QueryParametersDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

