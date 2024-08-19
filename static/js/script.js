


document.addEventListener('DOMContentLoaded', function() {
    const themeStylesheet = document.getElementById('theme-stylesheet');
    const themeToggle = document.getElementById('theme-toggle');

    // Load theme preference from localStorage
    const darkMode = localStorage.getItem('dark_mode') === 'true';
    themeStylesheet.setAttribute('href', darkMode ? '/static/css/styles-darkmode.css' : '/static/css/styles.css');
    themeToggle.classList.toggle('fa-toggle-on', darkMode);
    themeToggle.classList.toggle('fa-toggle-off', !darkMode);

    themeToggle.addEventListener('click', function() {
        const isDarkMode = themeStylesheet.getAttribute('href').includes('styles-darkmode.css');
        const newTheme = isDarkMode ? '/static/css/styles.css' : '/static/css/styles-darkmode.css';

        // Update localStorage
        localStorage.setItem('dark_mode', !isDarkMode);

        // Update the stylesheet link
        themeStylesheet.setAttribute('href', newTheme);

        // Toggle the icon class
        this.classList.toggle('fa-toggle-on', !isDarkMode);
        this.classList.toggle('fa-toggle-off', isDarkMode);
    });
});





document.addEventListener('DOMContentLoaded', function() {
    const messageLogo = document.querySelector('.fa-regular.fa-message');

    // Check if there are new messages from localStorage
    const hasNewMessages = localStorage.getItem('hasNewMessages') === 'true';

    if (messageLogo) {
        if (hasNewMessages) {
            messageLogo.classList.add('fa-new-message');
        } else {
            messageLogo.classList.remove('fa-new-message');
        }
    }

    // Clear the notification state after checking
    localStorage.removeItem('hasNewMessages');
});






document.addEventListener('DOMContentLoaded', function() {
    const messageForm = document.getElementById('message-form');
    const messageInput = document.getElementById('message-input');
    const messageList = document.getElementById('message-list');
    const recipientId = document.getElementById('recipient-id').value;

    messageForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const messageContent = messageInput.value;

        fetch('/send_message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token() }}'  // If using CSRF protection
            },
            body: JSON.stringify({
                recipient_id: recipientId,
                message: messageContent
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                console.error(data.error);
            } else {
                const newMessage = document.createElement('li');
                newMessage.className='message-right'
                newMessage.innerHTML = `${data.content}<br><small style="font-size: 0.2em;">Sent at: ${data.timestamp}</small>`;
                messageList.appendChild(newMessage);
                messageInput.value = '';
            }
        })
        .catch(error => console.error('Error:', error));
    });
});


document.addEventListener('DOMContentLoaded', function() {
    const chatContainer = document.getElementById('chat-container');

    function scrollToBottom() {
        if (chatContainer) {
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }
    }

    // Scroll to bottom when the page loads
    scrollToBottom();

    // Optionally, scroll to bottom when a new message is added
    const observer = new MutationObserver(scrollToBottom);
    observer.observe(chatContainer, { childList: true, subtree: true });
});


// for image navigation in homepage

document.addEventListener('DOMContentLoaded', function() {
    // Select all gallery containers
    const galleryContainers = document.querySelectorAll('.gallery-container');
    
    galleryContainers.forEach(container => {
        const images = container.dataset.images.split(',').map(filename => `/static/uploads/${filename}`);
        let currentIndex = 0;

        const galleryImage = container.querySelector('#gallery-image');
        const prevButton = container.querySelector('.prev-button');
        const nextButton = container.querySelector('.next-button');

        function updateImage() {
            galleryImage.src = images[currentIndex];
        }

        prevButton.addEventListener('click', function() {
            currentIndex = (currentIndex === 0) ? images.length - 1 : currentIndex - 1;
            updateImage();
        });

        nextButton.addEventListener('click', function() {
            currentIndex = (currentIndex === images.length - 1) ? 0 : currentIndex + 1;
            updateImage();
        });

        // Initialize with the first image
        updateImage();
    });
});


document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.card');

    cards.forEach(card => {
        card.addEventListener('click', function(event) {
            const target = event.target;

            // Prevent navigation if clicking on the navigation buttons
            if (target.closest('.prev-button') || target.closest('.next-button') || target.tagName === 'BUTTON') {
                event.stopPropagation();
                return;
            }

            // Otherwise, navigate to the post's page
            window.location.href = this.dataset.href;
        });
    });
});




//search funtion - not working now 

document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search-input');
    const mainContent = document.querySelector('.main-content');

    if (!mainContent) {
        console.error('Error: mainContent is null');
        return;
    }

    searchInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault(); // Prevent the default Enter key action (e.g., form submission)
            const keyword = searchInput.value;

            fetch(`/search?keyword=${encodeURIComponent(keyword)}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok.');
                    }
                    return response.json();
                })
                .then(data => {
                    if (data.html) {
                        mainContent.innerHTML = data.html;
                    } else {
                        console.error('Error: No HTML returned in response');
                    }
                })
                .catch(error => console.error('Error:', error));
        }
    });
});




document.getElementById('open-modal').addEventListener('click', function() {
    document.getElementById('myModal').style.display = 'block';
});

document.getElementById('close-modal').addEventListener('click', function() {
    document.getElementById('myModal').style.display = 'none';
});

window.onclick = function(event) {
    if (event.target === document.getElementById('myModal')) {
        document.getElementById('myModal').style.display = 'none';
    }
};
