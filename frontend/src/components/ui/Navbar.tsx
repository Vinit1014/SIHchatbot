import React, { useState } from "react";

export default function NavbarComp() {
    const [isMenuOpen, setIsMenuOpen] = useState(false);

    // Array of menu items with label and href (link)
    const menuItems = [
        { label: "Projects", href: "#projects" },
        { label: "Tech", href: "#tech" },
        { label: "Contact", href: "#contact" },
    ];
    
    return (
        <nav className="w-full px-4 py-4 shadow-md sticky top-0 z-50">
        <div className="container mx-auto flex justify-between items-center">
            {/* Brand Name */}
            
            {/* <div className="text-xl font-bold ml-2">
            <a href="#">

            AI
            </a>
            </div> */}

            {/* Menu Toggle Button for Mobile */}
            <button
            onClick={() => setIsMenuOpen(!isMenuOpen)}
            className="sm:hidden text-neutral-200 focus:outline-none"
            >
            {isMenuOpen ? (
                <svg
                className="w-6 h-6"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
                >
                <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="M6 18L18 6M6 6l12 12"
                ></path>
                </svg>
            ) : (
                <svg
                className="w-6 h-6"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
                >
                <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="M4 6h16M4 12h16M4 18h16"
                ></path>
                </svg>
            )}
            </button>

            {/* Desktop Menu Items */}
            <div className="hidden sm:flex gap-6 items-center">
            {/* {menuItems.map((item, index) => (
                <a
                key={index}
                href={item.href}
                className="text-neutral-200 hover:text-white text-xl"
                >
                {item.label}
                </a>
            ))} */}
            </div>
        </div>

        {/* Mobile Menu */}
        {isMenuOpen && (
            <div className="sm:hidden mt-2 flex flex-col gap-4">
            {menuItems.map((item, index) => (
                <a
                key={index}
                href={item.href}
                className="text-neutral-200 hover:text-white text-lg"
                >
                {item.label}
                </a>
            ))}
            </div>
        )}
        </nav>
    );
}
