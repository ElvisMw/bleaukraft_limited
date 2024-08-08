
        document.querySelectorAll('.hero-image').forEach(function(image) {
            image.addEventListener('mouseenter', function() {
                image.classList.add('folded');
            });
            image.addEventListener('mouseleave', function() {
                image.classList.remove('folded');
            });
        });

        // Function to animate the buttons on hover and track clicks
document.querySelectorAll('.sticky a').forEach(button => {

    // Animation on hover
    button.addEventListener('mouseenter', function() {
        this.style.transform = 'scale(1.1)';
        this.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.2)';
    });

    button.addEventListener('mouseleave', function() {
        this.style.transform = 'scale(1)';
        this.style.boxShadow = 'none';
    });

    // Tracking clicks
    button.addEventListener('click', function() {
        const action = this.querySelector('p').innerText; // Get the text of the clicked button (e.g., "Email Us")

        // Log the action to the console (you can replace this with actual tracking code)
        console.log(`Button clicked: ${action}`);

        // Example: Send data to Google Analytics (replace with your actual tracking code)
        if (typeof gtag === 'function') {
            gtag('event', 'contact_click', {
                'event_category': 'Contact Buttons',
                'event_label': action,
                'value': 1
            });
        }
    });
});
