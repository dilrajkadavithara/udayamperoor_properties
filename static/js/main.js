// static/js/main.js
document.addEventListener('DOMContentLoaded', () => {
    // Existing Mobile Menu Toggle
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');

    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });
    }

    // NEW: Search Form Toggle for Mobile (using original button ID)
    const toggleSearchButtonMobile = document.getElementById('toggle-search-button');
    const searchFormContainer = document.getElementById('search-form-container'); // This container is used by both mobile and desktop toggles

    if (toggleSearchButtonMobile && searchFormContainer) {
        toggleSearchButtonMobile.addEventListener('click', () => {
            searchFormContainer.classList.toggle('hidden'); // Toggles visibility of the form
            // Optional: Change button text based on state
            if (searchFormContainer.classList.contains('hidden')) {
                toggleSearchButtonMobile.textContent = 'Show Search Filters';
            } else {
                toggleSearchButtonMobile.textContent = 'Hide Search Filters';
            }
        });
    }

    // NEW: Search Form Toggle for Desktop
    const toggleSearchButtonDesktop = document.getElementById('toggle-search-button-desktop');

    if (toggleSearchButtonDesktop && searchFormContainer) {
        toggleSearchButtonDesktop.addEventListener('click', () => {
            searchFormContainer.classList.toggle('hidden'); // Toggles visibility of the form
            // Optional: Change button text based on state
            if (searchFormContainer.classList.contains('hidden')) {
                toggleSearchButtonDesktop.textContent = 'Show Search Filters';
            } else {
                toggleSearchButtonDesktop.textContent = 'Hide Search Filters';
            }
        });
    }
});