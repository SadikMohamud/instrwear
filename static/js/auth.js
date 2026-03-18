/*
Author: Sadik Mohamud
Project: InstrWear
File: static/js/auth.js
Purpose: Role switcher and password confirmation validation for auth pages.
*/

document.addEventListener("DOMContentLoaded", function () {
    const roleButtons = document.querySelectorAll(".iw-role-option");
    const roleInput = document.getElementById("roleInput");

    if (roleButtons.length && roleInput) {
        roleButtons.forEach((button) => {
            button.addEventListener("click", function () {
                const selectedRole = button.dataset.role;

                roleButtons.forEach((item) => item.classList.remove("active"));
                button.classList.add("active");
                roleInput.value = selectedRole;
            });
        });
    }

    const shopperForm = document.getElementById("shopperRegisterForm");
    if (shopperForm) {
        shopperForm.addEventListener("submit", function (event) {
            const password = document.getElementById("shopper_password").value;
            const confirmPassword = document.getElementById("shopper_confirm_password").value;

            if (password !== confirmPassword) {
                event.preventDefault();
                alert("Passwords do not match.");
            }
        });
    }

    const merchantForm = document.getElementById("merchantRegisterForm");
    if (merchantForm) {
        merchantForm.addEventListener("submit", function (event) {
            const password = document.getElementById("merchant_password").value;
            const confirmPassword = document.getElementById("merchant_password_confirm").value;

            if (password !== confirmPassword) {
                event.preventDefault();
                alert("Passwords do not match.");
            }
        });
    }
});