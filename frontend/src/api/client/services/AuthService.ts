/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Signup } from '../models/Signup';
import type { TokenObtainPair } from '../models/TokenObtainPair';
import type { TokenRefresh } from '../models/TokenRefresh';
import type { TokenVerify } from '../models/TokenVerify';
import type { UserMe } from '../models/UserMe';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class AuthService {
    /**
     * Get the authenticated user's profile.
     * @returns UserMe
     * @throws ApiError
     */
    public static authMe(): CancelablePromise<UserMe> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/auth/me',
        });
    }
    /**
     * Refresh JWT token.
     * @param requestBody
     * @returns any No response body
     * @throws ApiError
     */
    public static authRefresh(
        requestBody: TokenRefresh,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/auth/refresh',
            body: requestBody,
            mediaType: 'application/json',
        });
    }
    /**
     * Sign in for all roles (Customer, Staff, Owner, SuperAdmin).
     * @param requestBody
     * @returns any JWT tokens and user info
     * @throws ApiError
     */
    public static authSignin(
        requestBody: TokenObtainPair,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/auth/signin',
            body: requestBody,
            mediaType: 'application/json',
        });
    }
    /**
     * Member signup only (Customers).
     * @param requestBody
     * @returns UserMe User created
     * @throws ApiError
     */
    public static authSignup(
        requestBody: Signup,
    ): CancelablePromise<UserMe> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/auth/signup',
            body: requestBody,
            mediaType: 'application/json',
        });
    }
    /**
     * Verify JWT token.
     * @param requestBody
     * @returns any No response body
     * @throws ApiError
     */
    public static authVerify(
        requestBody: TokenVerify,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/auth/verify',
            body: requestBody,
            mediaType: 'application/json',
        });
    }
}
