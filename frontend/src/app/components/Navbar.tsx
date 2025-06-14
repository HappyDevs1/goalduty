"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { Goal } from "lucide-react";
import { useRouter } from "next/navigation";

export const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [isLoggedIn, setIsLoggedIn] = useState<any>(false);
  const router = useRouter();

  const checkLoginStatus = () => {
    try {
      const user = localStorage.getItem("user");
    const expiresAt = localStorage.getItem("expiresAt");

    const isValidUser = user && expiresAt && new Date().getTime() < parseInt(expiresAt);
    setIsLoggedIn(isValidUser);
    } catch (error) {
      console.error("Error checking login status:", error);
      setIsLoggedIn(false);
    }
  }

  useEffect(() => {
    checkLoginStatus();
  }, []);

  return (
    <nav className="bg-white shadow-md p-4">
      <div className="container mx-auto flex justify-between items-center">
        {/* Logo */}
        <div className="flex gap-2 items-center">
        <Goal size={28} color="blue" />
        <p className="font-semibold text-xl">Goalduty</p>
        </div>

        {/* Hamburger Menu Button (Mobile) */}
        <button
          className="md:hidden flex flex-col justify-between w-8 h-6"
          onClick={() => setIsOpen(!isOpen)}
        >
          <span
            className={`block w-8 h-1 bg-black rounded transition-all duration-300 ${
              isOpen ? "rotate-45 translate-y-2" : ""
            }`}
          ></span>
          <span
            className={`block w-8 h-1 bg-black rounded transition-all duration-300 ${
              isOpen ? "opacity-0" : ""
            }`}
          ></span>
          <span
            className={`block w-8 h-1 bg-black rounded transition-all duration-300 ${
              isOpen ? "-rotate-45 -translate-y-2" : ""
            }`}
          ></span>
        </button>

        {/* Desktop Navigation */}
        <ul className="hidden md:flex space-x-6 items-center">
          {
            isLoggedIn && (
              <>
              <li>
            <Link href="/" className="hover:text-blue-600">
              Tasks
            </Link>
          </li>
              <li>
            <Link href="/journal" className="hover:text-blue-600">
              Journal
            </Link>
          </li>
          <li>
            <Link href="/feedback" className="hover:text-blue-600">
              Feedback
            </Link>
          </li>
          <li>
            <Link href="/chat" className="hover:text-blue-600">
              Chat
            </Link>
          </li>
          <li>
            <button className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700" onClick={() => router.push("/login")}>
              Login
            </button>
          </li>
              </>
            )
          }
        </ul>
      </div>

      {/* Mobile Menu */}
      {isOpen && (
        <ul className="md:hidden absolute top-16 left-0 w-full bg-white shadow-md flex flex-col items-center space-y-4 p-4">
          {
            isLoggedIn && (
              <>
              <li>
            <Link href="/" className="hover:text-blue-600" onClick={() => setIsOpen(false)}>
              Tasks
            </Link>
          </li>
              <li>
            <Link href="/journal" className="hover:text-blue-600" onClick={() => setIsOpen(false)}>
              Journal
            </Link>
          </li>
          <li>
            <Link href="/feedback" className="hover:text-blue-600" onClick={() => setIsOpen(false)}>
              Feedback
            </Link>
          </li>
          <li>
            <Link href="/chat" className="hover:text-blue-600" onClick={() => setIsOpen(false)}>
              Chat
            </Link>
          </li>
              </>
            )
          }
          <li>
            <button className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700" onClick={() => router.push("/login")}>
              Login
            </button>
          </li>
        </ul>
      )}
    </nav>
  );
};
