"use client";

import React, { useState, useEffect } from "react";
import Tasks from "./tasks/page";
import Login from "./login/page";

export default function Home() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [checkingAuth, setCheckingAuth] = useState(true);

  useEffect(() => {
    const checkAuth = () => {
      try {
        const user = localStorage.getItem("user");
        const expiresAt = localStorage.getItem("expiresAt");
        const isValidUser =
          user && expiresAt && new Date().getTime() < parseInt(expiresAt);

        setIsLoggedIn(!!isValidUser);
      } catch (error) {
        console.error("Error checking authentication:", error);
        setIsLoggedIn(false);
      } finally {
        setCheckingAuth(false);
      }
    };

    checkAuth();
  }, []);

  if (checkingAuth) {
    return <p className="text-center mt-10">Checking authentication...</p>;
  }

  return isLoggedIn ? <Tasks /> : <Login />;
}
