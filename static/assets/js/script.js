 var myCarousel = new bootstrap.Carousel(document.getElementById('imageCarousel'), {
    interval: 10000 // Change image every 3 seconds
  })


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

  

 