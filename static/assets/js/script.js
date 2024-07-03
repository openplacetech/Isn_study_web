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


  function toggleDetails(item) {
    item.classList.toggle('characteristics__active')
    var descriptionCard = item.querySelector('.card__with__description');
    descriptionCard.classList.toggle('active'); 
    const paragraph = item.querySelector('.card__with__description p');
    console.log(paragraph)
    paragraph.classList.toggle('show');
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
