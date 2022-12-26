# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "billing-benefits savings-plan-order-aliases create",
)
class Create(AAZCommand):
    """Create a savings plan. Learn more about permissions needed at https://go.microsoft.com/fwlink/?linkid=2215851

    :example: Create a Shared scope savings plan
        az billing-benefits savings-plan-order-aliases create --order-alias-name "cliTest" --applied-scope-type Shared --billing-plan P1M --billing-scope-id /subscriptions/30000000-aaaa-bbbb-cccc-200000000004 --commitment "{amount:10.0,currency-code:USD,grain:Hourly}" --display-name "cliTest" --term P1Y --sku Compute_Savings_Plan

    :example: Create a Single scope savings plan
        az billing-benefits savings-plan-order-aliases create --order-alias-name "cliTest" --applied-scope-type Single --applied-scope-prop "{subscription-id:/subscriptions/30000000-aaaa-bbbb-cccc-200000000004}" --billing-plan P1M --billing-scope-id /subscriptions/30000000-aaaa-bbbb-cccc-200000000004 --commitment "{amount:10.0,currency-code:USD,grain:Hourly}" --display-name "cliTest" --term P1Y --sku Compute_Savings_Plan

    :example: Create a Single Resource group scope savings plan
        az billing-benefits savings-plan-order-aliases create --order-alias-name "cliTest" --applied-scope-type Single --applied-scope-prop "{subscription-id:/subscriptions/30000000-aaaa-bbbb-cccc-200000000004/resourceGroups/rgName}" --billing-plan P1M --billing-scope-id /subscriptions/30000000-aaaa-bbbb-cccc-200000000004 --commitment "{amount:10.0,currency-code:USD,grain:Hourly}" --display-name "cliTest" --term P1Y --sku Compute_Savings_Plan

    :example: Create a ManagementGroup savings plan
        az billing-benefits savings-plan-order-aliases create --order-alias-name "cliTest" --applied-scope-type ManagementGroup --applied-scope-prop "{tenantId:10000000-aaaa-bbbb-cccc-20000000006,managementGroupId:/providers/Microsoft.Management/managementGroups/TestRg}" --billing-plan P1M --billing-scope-id /subscriptions/30000000-aaaa-bbbb-cccc-200000000004 --commitment "{amount:10.0,currency-code:USD,grain:Hourly}" --display-name "cliTest" --term P1Y --sku Compute_Savings_Plan
    """

    _aaz_info = {
        "version": "2022-11-01",
        "resources": [
            ["mgmt-plane", "/providers/microsoft.billingbenefits/savingsplanorderaliases/{}", "2022-11-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.order_alias_name = AAZStrArg(
            options=["--order-alias-name"],
            help="Name of the savings plan order alias",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9_\-\.]+$",
            ),
        )

        # define Arg Group "Body"

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.applied_scope_prop = AAZObjectArg(
            options=["--applied-scope-prop"],
            arg_group="Properties",
            help="Properties specific to applied scope type. Not required if not applicable.",
        )
        _args_schema.applied_scope_type = AAZStrArg(
            options=["--applied-scope-type"],
            arg_group="Properties",
            help="Type of the Applied Scope.",
            enum={"ManagementGroup": "ManagementGroup", "Shared": "Shared", "Single": "Single"},
        )
        _args_schema.billing_plan = AAZStrArg(
            options=["--billing-plan"],
            arg_group="Properties",
            help="Represents the billing plan in ISO 8601 format. Required only for monthly billing plans.",
            enum={"P1M": "P1M"},
        )
        _args_schema.billing_scope_id = AAZStrArg(
            options=["--billing-scope-id"],
            arg_group="Properties",
            help="Subscription that will be charged for purchasing the benefit",
        )
        _args_schema.commitment = AAZObjectArg(
            options=["--commitment"],
            arg_group="Properties",
            help="Commitment towards the benefit.",
        )
        _args_schema.display_name = AAZStrArg(
            options=["--display-name"],
            arg_group="Properties",
            help="Display name",
        )
        _args_schema.term = AAZStrArg(
            options=["--term"],
            arg_group="Properties",
            help="Represent benefit term in ISO 8601 format.",
            enum={"P1Y": "P1Y", "P3Y": "P3Y", "P5Y": "P5Y"},
        )

        applied_scope_prop = cls._args_schema.applied_scope_prop
        applied_scope_prop.display_name = AAZStrArg(
            options=["display-name"],
            help="Display name",
        )
        applied_scope_prop.management_group_id = AAZStrArg(
            options=["management-group-id"],
            help="Fully-qualified identifier of the management group where the benefit must be applied.",
        )
        applied_scope_prop.resource_group_id = AAZStrArg(
            options=["resource-group-id"],
            help="Fully-qualified identifier of the resource group.",
        )
        applied_scope_prop.subscription_id = AAZStrArg(
            options=["subscription-id"],
            help="Fully-qualified identifier of the subscription.",
        )
        applied_scope_prop.tenant_id = AAZStrArg(
            options=["tenant-id"],
            help="Tenant ID where the benefit is applied.",
        )

        commitment = cls._args_schema.commitment
        commitment.amount = AAZFloatArg(
            options=["amount"],
        )
        commitment.currency_code = AAZStrArg(
            options=["currency-code"],
            help="The ISO 4217 3-letter currency code for the currency used by this purchase record.",
        )
        commitment.grain = AAZStrArg(
            options=["grain"],
            help="Commitment grain.",
            enum={"Hourly": "Hourly"},
        )

        # define Arg Group "Sku"

        _args_schema = cls._args_schema
        _args_schema.sku = AAZStrArg(
            options=["--sku"],
            arg_group="Sku",
            help="Name of the SKU to be applied",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.SavingsPlanOrderAliasCreate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class SavingsPlanOrderAliasCreate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/providers/Microsoft.BillingBenefits/savingsPlanOrderAliases/{savingsPlanOrderAliasName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "savingsPlanOrderAliasName", self.ctx.args.order_alias_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-11-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("sku", AAZObjectType, ".", typ_kwargs={"flags": {"required": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("appliedScopeProperties", AAZObjectType, ".applied_scope_prop")
                properties.set_prop("appliedScopeType", AAZStrType, ".applied_scope_type")
                properties.set_prop("billingPlan", AAZStrType, ".billing_plan")
                properties.set_prop("billingScopeId", AAZStrType, ".billing_scope_id")
                properties.set_prop("commitment", AAZObjectType, ".commitment")
                properties.set_prop("displayName", AAZStrType, ".display_name")
                properties.set_prop("term", AAZStrType, ".term")

            applied_scope_properties = _builder.get(".properties.appliedScopeProperties")
            if applied_scope_properties is not None:
                applied_scope_properties.set_prop("displayName", AAZStrType, ".display_name")
                applied_scope_properties.set_prop("managementGroupId", AAZStrType, ".management_group_id")
                applied_scope_properties.set_prop("resourceGroupId", AAZStrType, ".resource_group_id")
                applied_scope_properties.set_prop("subscriptionId", AAZStrType, ".subscription_id")
                applied_scope_properties.set_prop("tenantId", AAZStrType, ".tenant_id")

            commitment = _builder.get(".properties.commitment")
            if commitment is not None:
                commitment.set_prop("amount", AAZFloatType, ".amount")
                commitment.set_prop("currencyCode", AAZStrType, ".currency_code")
                commitment.set_prop("grain", AAZStrType, ".grain")

            sku = _builder.get(".sku")
            if sku is not None:
                sku.set_prop("name", AAZStrType, ".sku")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.kind = AAZStrType()
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.sku = AAZObjectType(
                flags={"required": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.applied_scope_properties = AAZObjectType(
                serialized_name="appliedScopeProperties",
            )
            properties.applied_scope_type = AAZStrType(
                serialized_name="appliedScopeType",
            )
            properties.billing_plan = AAZStrType(
                serialized_name="billingPlan",
            )
            properties.billing_scope_id = AAZStrType(
                serialized_name="billingScopeId",
            )
            properties.commitment = AAZObjectType()
            properties.display_name = AAZStrType(
                serialized_name="displayName",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.savings_plan_order_id = AAZStrType(
                serialized_name="savingsPlanOrderId",
                flags={"read_only": True},
            )
            properties.term = AAZStrType()

            applied_scope_properties = cls._schema_on_200_201.properties.applied_scope_properties
            applied_scope_properties.display_name = AAZStrType(
                serialized_name="displayName",
            )
            applied_scope_properties.management_group_id = AAZStrType(
                serialized_name="managementGroupId",
            )
            applied_scope_properties.resource_group_id = AAZStrType(
                serialized_name="resourceGroupId",
            )
            applied_scope_properties.subscription_id = AAZStrType(
                serialized_name="subscriptionId",
            )
            applied_scope_properties.tenant_id = AAZStrType(
                serialized_name="tenantId",
            )

            commitment = cls._schema_on_200_201.properties.commitment
            commitment.amount = AAZFloatType()
            commitment.currency_code = AAZStrType(
                serialized_name="currencyCode",
            )
            commitment.grain = AAZStrType()

            sku = cls._schema_on_200_201.sku
            sku.name = AAZStrType()

            system_data = cls._schema_on_200_201.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]