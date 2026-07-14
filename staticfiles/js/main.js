function toggleMenu() {
document.getElementById("navMenu").classList.toggle("show");
}

// Register Page Validation

// Register Page Validation

document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");

    if (form) {

        form.addEventListener("submit", function (e) {

            let password =
                document.getElementById("password").value;

            let confirm =
                document.getElementById("confirm_password").value;

            let errorBox =
                document.getElementById("password-error");

            if (password !== confirm) {

                e.preventDefault();

                if(errorBox){
                    errorBox.innerText =
                    "Passwords do not match";
                    errorBox.style.display = "block";
                }

                return false;
            }

            if(errorBox){
                errorBox.style.display = "none";
            }

        });

    }

});

// Auto Close Mobile Menu

document.querySelectorAll("#navMenu a").forEach(link => {

link.addEventListener("click", () => {

    document.getElementById("navMenu")
        .classList.remove("show");

});

});

// Close menu when clicking outside

document.addEventListener("click", function(event){

    const menu = document.getElementById("navMenu");
    const toggle = document.querySelector(".menu-toggle");

    if(
        !menu.contains(event.target) &&
        !toggle.contains(event.target)
    ){
        menu.classList.remove("show");
    }

});

// Donate Amount Validation

const donateForm =
document.querySelector(".donate-card form");

if(donateForm){

    donateForm.addEventListener(
        "submit",
        function(e){

            const amount =
            document.getElementById("amount").value;

            if(amount < 10){

                e.preventDefault();

                alert(
                "Minimum donation amount is ₹10"
                );
            }

        }
    );

}

// contact page

document.addEventListener("DOMContentLoaded", () => {

const cards = document.querySelectorAll(
    ".info-card, .contact-form-card"
);

const observer = new IntersectionObserver((entries) => {

    entries.forEach(entry => {

        if(entry.isIntersecting){

            entry.target.style.opacity = "1";
            entry.target.style.transform = "translateY(0)";

        }

    });

});

cards.forEach(card => {

    card.style.opacity = "0";
    card.style.transform = "translateY(40px)";
    card.style.transition = "all .8s ease";

    observer.observe(card);

});

});


// Developer Card

document.addEventListener("DOMContentLoaded", function () {

    const developerBtn = document.getElementById("developerBtn");
    const developerCard = document.getElementById("developerCard");

    if (developerBtn && developerCard) {

        developerBtn.addEventListener("click", function () {

            if (developerCard.style.display === "block") {
                developerCard.style.display = "none";
            } else {
                developerCard.style.display = "block";
            }

        });

    }

});

function closeCard() {
    document.getElementById("developerCard").style.display = "none";
}

