"use client";

import * as React from "react";
import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";
import { Button } from "@/components/ui/button";

function useAuthed(): boolean {
  const [ok, setOk] = React.useState(false);
  React.useEffect(() => {
    const token =
      typeof window !== "undefined" ? localStorage.getItem("access") : null;
    setOk(!!token);
  }, []);
  return ok;
}

function NavLink({
  href,
  children,
}: React.PropsWithChildren<{ href: string }>) {
  const pathname = usePathname();
  const active =
    pathname === href || (href !== "/" && pathname?.startsWith(href));
  return (
    <Link
      href={href}
      className={`text-sm font-medium hover:opacity-80 ${
        active ? "text-foreground" : "text-muted-foreground"
      }`}
    >
      {children}
    </Link>
  );
}

export default function TopNav() {
  const authed = useAuthed();
  const router = useRouter();

  function signOut() {
    try {
      localStorage.removeItem("access");
      document.cookie = "skoga_session=; Max-Age=0; Path=/; SameSite=Lax";
      router.replace("/");
    } catch {
      router.replace("/");
    }
  }

  return (
    <header className="sticky top-0 z-40 w-full border-b bg-background/80 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container mx-auto flex h-14 items-center justify-between gap-4 px-4">
        <div className="flex items-center gap-6">
          <Link href="/" className="text-lg font-semibold">
            Skoga
          </Link>
          <nav className="hidden items-center gap-5 sm:flex">
            <NavLink href="/">Catalog</NavLink>
            <NavLink href="/about">About</NavLink>
            <NavLink href="/contact">Contact</NavLink>
          </nav>
        </div>

        <div className="flex items-center gap-2">
          {!authed ? (
            <>
              <Link href="/signin">
                {/* ghost → transparent with subtle hover; size=sm → h-8 px-3 */}
                <Button className="h-8 px-3 bg-transparent hover:bg-muted">
                  Sign in
                </Button>
              </Link>
              <Link href="/signup">
                {/* size=sm → h-8 px-3 */}
                <Button className="h-8 px-3">Sign up</Button>
              </Link>
            </>
          ) : (
            <div className="flex items-center gap-2">
              <Link href="/dashboard">
                {/* outline → border; size=sm → h-8 px-3 */}
                <Button className="h-8 px-3 border">Account</Button>
              </Link>
              <Button
                className="h-8 px-3 bg-transparent hover:bg-muted"
                onClick={signOut}
              >
                Sign out
              </Button>
            </div>
          )}
        </div>
      </div>
    </header>
  );
}
