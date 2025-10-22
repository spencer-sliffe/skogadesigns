/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Attribute } from '../models/Attribute';
import type { AttributeValue } from '../models/AttributeValue';
import type { Category } from '../models/Category';
import type { PatchedAttribute } from '../models/PatchedAttribute';
import type { PatchedAttributeValue } from '../models/PatchedAttributeValue';
import type { PatchedCategory } from '../models/PatchedCategory';
import type { PatchedProduct } from '../models/PatchedProduct';
import type { PatchedProductAttribute } from '../models/PatchedProductAttribute';
import type { PatchedProductImage } from '../models/PatchedProductImage';
import type { PatchedVariant } from '../models/PatchedVariant';
import type { Product } from '../models/Product';
import type { ProductAttribute } from '../models/ProductAttribute';
import type { ProductImage } from '../models/ProductImage';
import type { Variant } from '../models/Variant';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class CatalogService {
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @returns AttributeValue
     * @throws ApiError
     */
    public static catalogAttributeValuesList(): CancelablePromise<Array<AttributeValue>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/catalog/attribute-values',
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param requestBody
     * @returns AttributeValue
     * @throws ApiError
     */
    public static catalogAttributeValuesCreate(
        requestBody: AttributeValue,
    ): CancelablePromise<AttributeValue> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/catalog/attribute-values',
            body: requestBody,
            mediaType: 'application/json',
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param id A unique integer value identifying this attribute value.
     * @returns AttributeValue
     * @throws ApiError
     */
    public static catalogAttributeValuesRetrieve(
        id: number,
    ): CancelablePromise<AttributeValue> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/catalog/attribute-values/{id}',
            path: {
                'id': id,
            },
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param id A unique integer value identifying this attribute value.
     * @param requestBody
     * @returns AttributeValue
     * @throws ApiError
     */
    public static catalogAttributeValuesUpdate(
        id: number,
        requestBody: AttributeValue,
    ): CancelablePromise<AttributeValue> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/catalog/attribute-values/{id}',
            path: {
                'id': id,
            },
            body: requestBody,
            mediaType: 'application/json',
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param id A unique integer value identifying this attribute value.
     * @param requestBody
     * @returns AttributeValue
     * @throws ApiError
     */
    public static catalogAttributeValuesPartialUpdate(
        id: number,
        requestBody?: PatchedAttributeValue,
    ): CancelablePromise<AttributeValue> {
        return __request(OpenAPI, {
            method: 'PATCH',
            url: '/api/catalog/attribute-values/{id}',
            path: {
                'id': id,
            },
            body: requestBody,
            mediaType: 'application/json',
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param id A unique integer value identifying this attribute value.
     * @returns void
     * @throws ApiError
     */
    public static catalogAttributeValuesDestroy(
        id: number,
    ): CancelablePromise<void> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/catalog/attribute-values/{id}',
            path: {
                'id': id,
            },
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @returns Attribute
     * @throws ApiError
     */
    public static catalogAttributesList(): CancelablePromise<Array<Attribute>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/catalog/attributes',
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param requestBody
     * @returns Attribute
     * @throws ApiError
     */
    public static catalogAttributesCreate(
        requestBody: Attribute,
    ): CancelablePromise<Attribute> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/catalog/attributes',
            body: requestBody,
            mediaType: 'application/json',
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param id A unique integer value identifying this attribute.
     * @returns Attribute
     * @throws ApiError
     */
    public static catalogAttributesRetrieve(
        id: number,
    ): CancelablePromise<Attribute> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/catalog/attributes/{id}',
            path: {
                'id': id,
            },
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param id A unique integer value identifying this attribute.
     * @param requestBody
     * @returns Attribute
     * @throws ApiError
     */
    public static catalogAttributesUpdate(
        id: number,
        requestBody: Attribute,
    ): CancelablePromise<Attribute> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/catalog/attributes/{id}',
            path: {
                'id': id,
            },
            body: requestBody,
            mediaType: 'application/json',
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param id A unique integer value identifying this attribute.
     * @param requestBody
     * @returns Attribute
     * @throws ApiError
     */
    public static catalogAttributesPartialUpdate(
        id: number,
        requestBody?: PatchedAttribute,
    ): CancelablePromise<Attribute> {
        return __request(OpenAPI, {
            method: 'PATCH',
            url: '/api/catalog/attributes/{id}',
            path: {
                'id': id,
            },
            body: requestBody,
            mediaType: 'application/json',
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param id A unique integer value identifying this attribute.
     * @returns void
     * @throws ApiError
     */
    public static catalogAttributesDestroy(
        id: number,
    ): CancelablePromise<void> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/catalog/attributes/{id}',
            path: {
                'id': id,
            },
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @returns Category
     * @throws ApiError
     */
    public static catalogCategoriesList(): CancelablePromise<Array<Category>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/catalog/categories',
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param requestBody
     * @returns Category
     * @throws ApiError
     */
    public static catalogCategoriesCreate(
        requestBody: Category,
    ): CancelablePromise<Category> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/catalog/categories',
            body: requestBody,
            mediaType: 'application/json',
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param id A unique integer value identifying this category.
     * @returns Category
     * @throws ApiError
     */
    public static catalogCategoriesRetrieve(
        id: number,
    ): CancelablePromise<Category> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/catalog/categories/{id}',
            path: {
                'id': id,
            },
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param id A unique integer value identifying this category.
     * @param requestBody
     * @returns Category
     * @throws ApiError
     */
    public static catalogCategoriesUpdate(
        id: number,
        requestBody: Category,
    ): CancelablePromise<Category> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/catalog/categories/{id}',
            path: {
                'id': id,
            },
            body: requestBody,
            mediaType: 'application/json',
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param id A unique integer value identifying this category.
     * @param requestBody
     * @returns Category
     * @throws ApiError
     */
    public static catalogCategoriesPartialUpdate(
        id: number,
        requestBody?: PatchedCategory,
    ): CancelablePromise<Category> {
        return __request(OpenAPI, {
            method: 'PATCH',
            url: '/api/catalog/categories/{id}',
            path: {
                'id': id,
            },
            body: requestBody,
            mediaType: 'application/json',
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param id A unique integer value identifying this category.
     * @returns void
     * @throws ApiError
     */
    public static catalogCategoriesDestroy(
        id: number,
    ): CancelablePromise<void> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/catalog/categories/{id}',
            path: {
                'id': id,
            },
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @returns ProductImage
     * @throws ApiError
     */
    public static catalogImagesList(): CancelablePromise<Array<ProductImage>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/catalog/images',
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param requestBody
     * @returns ProductImage
     * @throws ApiError
     */
    public static catalogImagesCreate(
        requestBody: ProductImage,
    ): CancelablePromise<ProductImage> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/catalog/images',
            body: requestBody,
            mediaType: 'application/json',
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param id A unique integer value identifying this product image.
     * @returns ProductImage
     * @throws ApiError
     */
    public static catalogImagesRetrieve(
        id: number,
    ): CancelablePromise<ProductImage> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/catalog/images/{id}',
            path: {
                'id': id,
            },
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param id A unique integer value identifying this product image.
     * @param requestBody
     * @returns ProductImage
     * @throws ApiError
     */
    public static catalogImagesUpdate(
        id: number,
        requestBody: ProductImage,
    ): CancelablePromise<ProductImage> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/catalog/images/{id}',
            path: {
                'id': id,
            },
            body: requestBody,
            mediaType: 'application/json',
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param id A unique integer value identifying this product image.
     * @param requestBody
     * @returns ProductImage
     * @throws ApiError
     */
    public static catalogImagesPartialUpdate(
        id: number,
        requestBody?: PatchedProductImage,
    ): CancelablePromise<ProductImage> {
        return __request(OpenAPI, {
            method: 'PATCH',
            url: '/api/catalog/images/{id}',
            path: {
                'id': id,
            },
            body: requestBody,
            mediaType: 'application/json',
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param id A unique integer value identifying this product image.
     * @returns void
     * @throws ApiError
     */
    public static catalogImagesDestroy(
        id: number,
    ): CancelablePromise<void> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/catalog/images/{id}',
            path: {
                'id': id,
            },
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @returns ProductAttribute
     * @throws ApiError
     */
    public static catalogProductAttributesList(): CancelablePromise<Array<ProductAttribute>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/catalog/product-attributes',
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param requestBody
     * @returns ProductAttribute
     * @throws ApiError
     */
    public static catalogProductAttributesCreate(
        requestBody: ProductAttribute,
    ): CancelablePromise<ProductAttribute> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/catalog/product-attributes',
            body: requestBody,
            mediaType: 'application/json',
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param id A unique integer value identifying this product attribute.
     * @returns ProductAttribute
     * @throws ApiError
     */
    public static catalogProductAttributesRetrieve(
        id: number,
    ): CancelablePromise<ProductAttribute> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/catalog/product-attributes/{id}',
            path: {
                'id': id,
            },
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param id A unique integer value identifying this product attribute.
     * @param requestBody
     * @returns ProductAttribute
     * @throws ApiError
     */
    public static catalogProductAttributesUpdate(
        id: number,
        requestBody: ProductAttribute,
    ): CancelablePromise<ProductAttribute> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/catalog/product-attributes/{id}',
            path: {
                'id': id,
            },
            body: requestBody,
            mediaType: 'application/json',
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param id A unique integer value identifying this product attribute.
     * @param requestBody
     * @returns ProductAttribute
     * @throws ApiError
     */
    public static catalogProductAttributesPartialUpdate(
        id: number,
        requestBody?: PatchedProductAttribute,
    ): CancelablePromise<ProductAttribute> {
        return __request(OpenAPI, {
            method: 'PATCH',
            url: '/api/catalog/product-attributes/{id}',
            path: {
                'id': id,
            },
            body: requestBody,
            mediaType: 'application/json',
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param id A unique integer value identifying this product attribute.
     * @returns void
     * @throws ApiError
     */
    public static catalogProductAttributesDestroy(
        id: number,
    ): CancelablePromise<void> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/catalog/product-attributes/{id}',
            path: {
                'id': id,
            },
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @returns Product
     * @throws ApiError
     */
    public static catalogProductsList(): CancelablePromise<Array<Product>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/catalog/products',
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param requestBody
     * @returns Product
     * @throws ApiError
     */
    public static catalogProductsCreate(
        requestBody: Product,
    ): CancelablePromise<Product> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/catalog/products',
            body: requestBody,
            mediaType: 'application/json',
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param id A unique integer value identifying this product.
     * @returns Product
     * @throws ApiError
     */
    public static catalogProductsRetrieve(
        id: number,
    ): CancelablePromise<Product> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/catalog/products/{id}',
            path: {
                'id': id,
            },
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param id A unique integer value identifying this product.
     * @param requestBody
     * @returns Product
     * @throws ApiError
     */
    public static catalogProductsUpdate(
        id: number,
        requestBody: Product,
    ): CancelablePromise<Product> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/catalog/products/{id}',
            path: {
                'id': id,
            },
            body: requestBody,
            mediaType: 'application/json',
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param id A unique integer value identifying this product.
     * @param requestBody
     * @returns Product
     * @throws ApiError
     */
    public static catalogProductsPartialUpdate(
        id: number,
        requestBody?: PatchedProduct,
    ): CancelablePromise<Product> {
        return __request(OpenAPI, {
            method: 'PATCH',
            url: '/api/catalog/products/{id}',
            path: {
                'id': id,
            },
            body: requestBody,
            mediaType: 'application/json',
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param id A unique integer value identifying this product.
     * @returns void
     * @throws ApiError
     */
    public static catalogProductsDestroy(
        id: number,
    ): CancelablePromise<void> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/catalog/products/{id}',
            path: {
                'id': id,
            },
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @returns Variant
     * @throws ApiError
     */
    public static catalogVariantsList(): CancelablePromise<Array<Variant>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/catalog/variants',
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param requestBody
     * @returns Variant
     * @throws ApiError
     */
    public static catalogVariantsCreate(
        requestBody: Variant,
    ): CancelablePromise<Variant> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/catalog/variants',
            body: requestBody,
            mediaType: 'application/json',
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param id A unique integer value identifying this variant.
     * @returns Variant
     * @throws ApiError
     */
    public static catalogVariantsRetrieve(
        id: number,
    ): CancelablePromise<Variant> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/catalog/variants/{id}',
            path: {
                'id': id,
            },
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param id A unique integer value identifying this variant.
     * @param requestBody
     * @returns Variant
     * @throws ApiError
     */
    public static catalogVariantsUpdate(
        id: number,
        requestBody: Variant,
    ): CancelablePromise<Variant> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/catalog/variants/{id}',
            path: {
                'id': id,
            },
            body: requestBody,
            mediaType: 'application/json',
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param id A unique integer value identifying this variant.
     * @param requestBody
     * @returns Variant
     * @throws ApiError
     */
    public static catalogVariantsPartialUpdate(
        id: number,
        requestBody?: PatchedVariant,
    ): CancelablePromise<Variant> {
        return __request(OpenAPI, {
            method: 'PATCH',
            url: '/api/catalog/variants/{id}',
            path: {
                'id': id,
            },
            body: requestBody,
            mediaType: 'application/json',
        });
    }
    /**
     * Convenience base class: ModelViewSet + tenant scoping.
     * Override `tenant_path` per view if the FK is indirect.
     * @param id A unique integer value identifying this variant.
     * @returns void
     * @throws ApiError
     */
    public static catalogVariantsDestroy(
        id: number,
    ): CancelablePromise<void> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/catalog/variants/{id}',
            path: {
                'id': id,
            },
        });
    }
}
