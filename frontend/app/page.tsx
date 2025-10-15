export default function Home() {
  const token = typeof window !== "undefined" ? localStorage.getItem("access") : null;
  return (
    <main className="flex min-h-screen items-center justify-center flex-col space-y-4">
      <h1 className="text-3xl font-bold">Welcome to Skoga Designs</h1>
      {token ? (
        <p className="text-green-600">Authenticated ✅</p>
      ) : (
        <p className="text-red-600">You are not signed in</p>
      )}
    </main>
  );
}
