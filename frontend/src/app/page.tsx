"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { loginUser } from "./services/user";

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const router = useRouter();

  const handleLogin = async () => {
    setError("");

    const res = await loginUser({ email, password });

    if (!res) {
      setError("Login failed");
      return;
    }

    const user: any = res.data;

    // Store in localStorage with expiry
    const expiresAt = new Date().getTime() + 30 * 60 * 1000; // 30 minutes
    localStorage.setItem("user", user);
    localStorage.setItem("expiresAt", expiresAt.toString());

    router.push("/tasks");
  };

  return (
    <div className="h-screen flex flex-col justify-center items-center">
      <div className="w-80 bg-white p-6 rounded shadow space-y-4">
        <h2 className="text-xl font-bold">Login</h2>
        <input
          className="w-full border p-2 rounded"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          type="password"
          className="w-full border p-2 rounded"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        {error && <p className="text-red-500 text-sm">{error}</p>}
        <button
          className="w-full bg-blue-500 text-white py-2 rounded"
          onClick={handleLogin}
        >
          Login
        </button>
      </div>
    </div>
  );
}
