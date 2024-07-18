//  var myCarousel = new bootstrap.Carousel(document.getElementById('imageCarousel'), {
//     interval: 10000 // Change image every 3 seconds
//   })



  var currentUrl = window.location.href;

  
  var navLinks = document.querySelectorAll('.navlink_container li a');



  
  navLinks.forEach(function(navLink) {
    
    if (navLink.href === currentUrl) {
    
      navLink.parentNode.classList.add('active');
    }
   
  });


  function setupHoverToggle(item) {
    item.addEventListener('mouseenter', function() {
        toggleDetails(item, true);
    });

    item.addEventListener('mouseleave', function() {
        toggleDetails(item, false);
    });
}

function toggleDetails(item, show) {
    item.classList.toggle('characteristics__active', show);
    var descriptionCard = item.querySelector('.card__with__description');
    descriptionCard.classList.toggle('active', show);
    
    const paragraph = item.querySelector('.card__with__description p');
    paragraph.classList.toggle('show', show);
}

// Apply this to all cards
document.querySelectorAll('.characterstic__card').forEach(setupHoverToggle);


  
function toggleMenu() {
    const menu = document.getElementById('mobileMenu');
    const menuIcon = document.getElementById('menuIcon');
    const closeIcon = document.getElementById('closeIcon');
    menu.classList.toggle('isactive');
    menuIcon.classList.toggle('hidden');
    closeIcon.classList.toggle('hidden');
}



function setupNavbar() {
  const moreToggle = document.getElementById('more-toggle');
  const dropdownMenu = document.querySelector('.dropdown-menu-navbar');

  if (moreToggle && dropdownMenu) {
      moreToggle.addEventListener('click', function(e) {
          e.preventDefault();
          e.stopPropagation();
          dropdownMenu.classList.toggle('show');
      });

    
      document.addEventListener('click', function(e) {
          if (!moreToggle.contains(e.target) && !dropdownMenu.contains(e.target)) {
              dropdownMenu.classList.remove('show');
          }
      });
  }
}


document.addEventListener('DOMContentLoaded', setupNavbar);



  function createAvatar() {
    const avatarDivs = document.getElementsByClassName("user__avatar");
    for (let i = 0; i < avatarDivs.length; i++) {
        const div = avatarDivs[i];
        const content = div.textContent;
        const firstLetter = content.charAt(0).toUpperCase();
        div.textContent = firstLetter;
    }

}


 createAvatar()


 
 document.addEventListener('DOMContentLoaded', function() {
    const slider = document.querySelector('.slider');
    const sliderContainer = slider.querySelector('.slider__container');
    const slides = sliderContainer.querySelectorAll('.slider__card');
    const prevBtn = slider.querySelector('.slider__arrow--left');
    const nextBtn = slider.querySelector('.slider__arrow--right');
    let currentIndex = 0;

    function updateSlider() {
        const offset = -currentIndex * 100;
        sliderContainer.style.transform = `translateX(${offset}%)`;
        updateButtonStates();
    }
   

    function nextSlide() {
        if (currentIndex < slides.length - 3) {
            currentIndex++;
            updateSlider();
        }
    }

    function prevSlide() {
        if (currentIndex > 0) {
            currentIndex--;
            updateSlider();
        }
    }

    function updateButtonStates() {
        prevBtn.disabled = currentIndex === 0;
        nextBtn.disabled = slides.length % 3 !== 0 || currentIndex === Math.floor(slides.length / 3) - 1;

    }

    nextBtn.addEventListener('click', nextSlide);
    prevBtn.addEventListener('click', prevSlide);
   
    // Initialize button states
    updateButtonStates();
});

