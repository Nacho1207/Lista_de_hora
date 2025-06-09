document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger');
    const navLinksContainer = document.querySelector('.nav-links-container');


    function toggleMenu() {
        hamburger.classList.toggle('active');
        navLinksContainer.classList.toggle('active');

    }


    if (hamburger && navLinksContainer) {
        hamburger.addEventListener('click', toggleMenu);
    }


    document.addEventListener('click', function(event) {
        const isClickInsideNav = hamburger.contains(event.target) || navLinksContainer.contains(event.target);
        const isMenuOpen = navLinksContainer.classList.contains('active');

        if (!isClickInsideNav && isMenuOpen) {
            toggleMenu();
        }
    });


    const navLinks = navLinksContainer.querySelectorAll('a');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {

            if (navLinksContainer.classList.contains('active') && window.innerWidth <= 768) {
                toggleMenu();
            }
        });
    });
});