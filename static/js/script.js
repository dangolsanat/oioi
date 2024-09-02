const toggle = document.getElementById("theme-toggle");
const msg = document.getElementById("chat-container");



document.addEventListener("DOMContentLoaded", function() {
    toggle.addEventListener("click", function() {
        const cards = document.getElementsByClassName("card")
        if (toggle.classList.contains("fa-toggle-on")) {
            for (let i = 0; i < cards.length; i++) {
                cards[i].classList.add("light");
            };
        }else {
            for (let i = 0; i < cards.length; i++) {
                cards[i].classList.remove("light");
         };
    }
    }
    );

    toggle.addEventListener("click", function() {
        const msg_left = document.getElementsByClassName("message-left");
        const msg_right = document.getElementsByClassName("message-right");
     
        if (toggle.classList.contains("fa-toggle-on")) {
            for (let i = 0; i < msg_left.length; i++) {
                msg_left[i].classList.add("light");
            };
            for (let i = 0; i < msg_right.length; i++) {
                msg_right[i].classList.add("light");
            };
    
        }else {
            for (let i = 0; i < msg_left.length; i++) {
                msg_left[i].classList.remove("light"); 
            };
            for (let i = 0; i < msg_right.length; i++) {
                msg_right[i].classList.remove("light"); 
            };
        }
    });




    const main = document.getElementsByClassName("main");
    const container = document.getElementById("container");
    const nav = document.getElementById("nav");
    const body = document.body;
    const user_logo = document.getElementById("user-logo");
    const msg_logo = document.getElementById("message-logo");
    const logout = document.getElementById("logout-logo");
    const house_logo = document.getElementById("house-logo");
    const user_cont = document.getElementById("user-content");
    const username = document.getElementById("username");
    const password = document.getElementById("password");


     // Toggle theme on click
    toggle.addEventListener("click", function() {
 

        // Toggle theme icon
        toggle.classList.toggle("fa-toggle-on");
        toggle.classList.toggle("fa-toggle-off");

        // Toggle theme classes
        container.classList.toggle("light");
        nav.classList.toggle("navlight");
        body.classList.toggle("dark");
 
        // Toggle icon colors
        user_logo.classList.toggle("fa-light");
        msg_logo.classList.toggle("fa-light");
        logout.classList.toggle("fa-light");
        house_logo.classList.toggle("fa-light");

        // Toggle card classes
        user_cont.classList.toggle("light");
        username.classList.toggle("form-light");
        password.classList.toggle("form-light");
 
    });


    
});

 











document.addEventListener('DOMContentLoaded', function() {
});


window.onload = function() {
    document.querySelectorAll('.gallery-container img, .user-info img').forEach(function(img) {
        img.style.display = 'block';
    });
};

document.addEventListener('DOMContentLoaded', function() {
    const images = document.querySelectorAll('.gallery-image, .circular-image');

    images.forEach(image => {
        const img = new Image();
        img.src = image.src;
        img.onload = () => {
            image.style.visibility = 'visible';
        };
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
                newMessage.className='message-right';
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

    // // Optionally, scroll to bottom when a new message is added
    // const observer = new MutationObserver(scrollToBottom);
    // observer.observe(chatContainer, { childList: true, subtree: true });
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


window.onclick = function(event) {
    if (event.target === document.getElementById('open-modal')) {
        document.getElementById('myModal').style.display = 'block';}
    else if (event.target === document.getElementById('close-modal')){
        document.getElementById('myModal').style.display = 'none';
    }
};
 