/*
Author: Sadik Mohamud
Project: InstrWear
File: static/js/add-product.js
Purpose: Handle custom image upload interaction on merchant add product page.
*/

document.addEventListener("DOMContentLoaded", function () {
    const uploadTrigger = document.getElementById("uploadTrigger");
    const fileInput = document.getElementById("id_image");
    const uploadText = document.getElementById("uploadText");

    if (uploadTrigger && fileInput) {
        uploadTrigger.addEventListener("click", function () {
            fileInput.click();
        });

        uploadTrigger.addEventListener("keydown", function (event) {
            if (event.key === "Enter" || event.key === " ") {
                event.preventDefault();
                fileInput.click();
            }
        });

        fileInput.addEventListener("change", function () {
            if (fileInput.files.length > 0) {
                uploadText.textContent = fileInput.files[0].name;
            } else {
                uploadText.textContent = "CLICK TO UPLOAD IMAGE";
            }
        });
    }
});