import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

const PROTECTED = ["/dashboard", "/account", "/orders"]; // add more as needed

export function middleware(req: NextRequest) {
  const session = req.cookies.get("skoga_session")?.value;
  const { pathname, search } = req.nextUrl;
  const isAuth = pathname === "/signin" || pathname === "/signup";
  const wantsProtected = PROTECTED.some((p) => pathname.startsWith(p));

  // send unauthenticated users to signin (preserve target with ?next=)
  if (!session && !isAuth) {
    const url = req.nextUrl.clone();
    url.pathname = "/signin";
    url.searchParams.set("next", pathname + search);
    return NextResponse.redirect(url);
  }

  // logged-in users shouldn't see auth pages
  if (session && isAuth) {
    const url = req.nextUrl.clone();
    url.pathname = "/dashboard";
    return NextResponse.redirect(url);
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/((?!_next/static|_next/image|favicon.ico|public|api).*)"],
};
