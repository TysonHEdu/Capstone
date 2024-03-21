// Function to add hover effect to the login button
function addHoverEffect() {
    const loginButton = document.querySelector('button[type="submit"]');
    if (loginButton) {
        loginButton.addEventListener('mouseenter', () => {
            loginButton.style.transform = 'translateY(-5px)'; // Move button 5px up
        });

        loginButton.addEventListener('mouseleave', () => {
            loginButton.style.transform = 'translateY(0)'; // Reset button position
        });
    }
}