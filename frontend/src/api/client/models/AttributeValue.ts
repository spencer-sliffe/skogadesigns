/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
/**
 * Enforces per-field read/write ACL based on request.user and request.tenant.
 * Looks for rules in this order:
 * 1) Serializer.FIELD_ACL
 * 2) Model.FIELD_ACL (if serializer.Meta.model defines it)
 * 3) Default: read=public, write=auth
 */
export type AttributeValue = {
    readonly id: number;
    attribute: number;
    readonly attribute_name: string;
    value: string;
    slug: string;
    readonly created_at: string;
    readonly updated_at: string;
};

