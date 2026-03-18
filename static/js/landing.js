/*
Author: Sadik Mohamud
Project: InstrWear
File: static/js/landing.js
Purpose: Mobile nav, tabs, and GSAP animations for landing page only.
*/

document.addEventListener("DOMContentLoaded", function () {
    const menuToggle = document.getElementById("menuToggle");
    const siteNav = document.getElementById("siteNav");
    const tabs = document.querySelectorAll(".iw-tab");
    const shopperSteps = document.getElementById("shopper-steps");
    const merchantSteps = document.getElementById("merchant-steps");

    if (menuToggle && siteNav) {
        menuToggle.addEventListener("click", function () {
            const isOpen = siteNav.classList.toggle("open");
            menuToggle.setAttribute("aria-expanded", String(isOpen));
        });

        siteNav.querySelectorAll("a").forEach((link) => {
            link.addEventListener("click", function () {
                siteNav.classList.remove("open");
                menuToggle.setAttribute("aria-expanded", "false");
            });
        });
    }

    tabs.forEach((tab) => {
        tab.addEventListener("click", function () {
            const selectedTab = tab.dataset.tab;

            tabs.forEach((item) => {
                item.classList.remove("active");
                item.setAttribute("aria-selected", "false");
            });

            tab.classList.add("active");
            tab.setAttribute("aria-selected", "true");

            if (selectedTab === "shopper") {
                shopperSteps.classList.add("active");
                merchantSteps.classList.remove("active");
            } else {
                merchantSteps.classList.add("active");
                shopperSteps.classList.remove("active");
            }
        });
    });

    if (window.gsap) {
        gsap.from(".gsap-title", {
            y: 40,
            opacity: 0,
            duration: 0.8,
            stagger: 0.12,
            ease: "power3.out"
        });

        gsap.from(".gsap-fade-up", {
            y: 28,
            opacity: 0,
            duration: 0.8,
            stagger: 0.15,
            ease: "power3.out",
            delay: 0.25
        });

        gsap.from(".gsap-shape", {
            scale: 0.8,
            rotation: -8,
            opacity: 0,
            duration: 1,
            stagger: 0.12,
            ease: "back.out(1.4)",
            delay: 0.2
        });

        gsap.to(".gsap-float", {
            y: -14,
            duration: 1.8,
            repeat: -1,
            yoyo: true,
            stagger: 0.2,
            ease: "sine.inOut"
        });
    }
});