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
    "networkfabric externalnetwork update-admin-state",
)
class UpdateAdminState(AAZCommand):
    """Update the admin state of the provided External Network resource.

    :example: Update admin state of External Network
        az networkfabric externalnetwork update-admin-state --resource-group "example-rg" --l3domain "example-l3domain" --resource-name "example-externalNetwork" --state "Enable"
    """

    _aaz_info = {
        "version": "2023-02-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.managednetworkfabric/l3isolationdomains/{}/externalnetworks/{}/updateadministrativestate", "2023-02-01-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, None)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_name = AAZStrArg(
            options=["--resource-name"],
            help="Name of the ExternalNetwork.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.l3_isolation_domain_name = AAZStrArg(
            options=["--l3domain", "--l3-isolation-domain-name"],
            help="Name of the L3IsolationDomain",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            help="Name of the resource group",
            required=True,
        )

        # define Arg Group "Body"

        _args_schema = cls._args_schema
        _args_schema.resource_ids = AAZListArg(
            options=["--resource-ids"],
            arg_group="Body",
            help="Network Fabrics or Network Rack resource Id.",
        )
        _args_schema.state = AAZStrArg(
            options=["--state"],
            arg_group="Body",
            help="Administrative state.",
            enum={"Disable": "Disable", "Enable": "Enable"},
        )

        resource_ids = cls._args_schema.resource_ids
        resource_ids.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.ExternalNetworksUpdateAdministrativeState(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    class ExternalNetworksUpdateAdministrativeState(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}/externalNetworks/{externalNetworkName}/updateAdministrativeState",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "externalNetworkName", self.ctx.args.resource_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "l3IsolationDomainName", self.ctx.args.l3_isolation_domain_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-02-01-preview",
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
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("resourceIds", AAZListType, ".resource_ids")
            _builder.set_prop("state", AAZStrType, ".state")

            resource_ids = _builder.get(".resourceIds")
            if resource_ids is not None:
                resource_ids.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200(self, session):
            pass


class _UpdateAdminStateHelper:
    """Helper class for UpdateAdminState"""


__all__ = ["UpdateAdminState"]