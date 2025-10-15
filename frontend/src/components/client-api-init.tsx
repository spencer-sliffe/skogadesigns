"use client";

import { useEffect } from "react";
import { OpenAPI } from "@api/client/core/OpenAPI";

export default function ClientApiInit() {
  useEffect(() => {
    // Set base URL (falls back to localhost)
    OpenAPI.BASE = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";

    // Set auth token dynamically on client
    OpenAPI.TOKEN = async () => {
      if (typeof window === "undefined") return undefined;
      return localStorage.getItem("access") ?? undefined;
    };
  }, []);

  return null;
}
