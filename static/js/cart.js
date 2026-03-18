/*
Author: Sadik Mohamud
Project: InstrWear
File: static/js/cart.js
Purpose: GSAP cart feedback animation when an item has just been added or updated.
*/

document.addEventListener("DOMContentLoaded", function () {
    const successMessage = document.querySelector(".js-cart-added-message");
    const highlightedItem = document.querySelector(".js-cart-added-item");

    if (window.gsap && successMessage) {
        gsap.from(successMessage, {
            y: -24,
            opacity: 0,
            duration: 0.65,
            ease: "power3.out"
        });

        if (highlightedItem) {
            gsap.fromTo(
                highlightedItem,
                {
                    scale: 0.97,
                    y: 12,
                    boxShadow: "0 0 0 0 #000000"
                },
                {
                    scale: 1,
                    y: 0,
                    duration: 0.75,
                    ease: "back.out(1.4)"
                }
            );
        }
    }
});