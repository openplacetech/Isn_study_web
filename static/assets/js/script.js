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

var opportunitiesData = [
    {
        "designation": "Developer",
        "jobs": [
            {
                "title": "Software Engineer - Backend Developer",
                "description": "Develop and maintain server-side logic and databases.",
                "location": "New York",
                "type": "Full-time"
            },
            {
                "title": "UX Designer - Frontend Developer",
                "description": "Create intuitive user interfaces and implement frontend designs.",
                "location": "San Francisco",
                "type": "Contract"
            }
        ]
    },
    {
        "designation": "Engineering",
        "jobs": [
            {
                "title": "Data Scientist - Backend Developer",
                "description": "Analyze complex data sets and develop machine learning models.",
                "location": "Boston",
                "type": "Full-time"
            },
            {
                "title": "Web Developer - Frontend Developer",
                "description": "Build responsive and interactive web applications.",
                "location": "Remote",
                "type": "Part-time"
            }
        ]
    },
    {
        "designation": "Product",
        "jobs": [
            {
                "title": "Product Manager - Backend Developer",
                "description": "Lead product development and coordinate between teams.",
                "location": "Seattle",
                "type": "Full-time"
            },
            {
                "title": "UI Designer - Frontend Developer",
                "description": "Design visually appealing and functional user interfaces.",
                "location": "Los Angeles",
                "type": "Freelance"
            }
        ]
    }
];

function createOpportunityCard(job) {
    return `
        <div class="opportunities__card">
            <h4>${job.title}</h4>
            <div class="type__opportunities__container">
                <span class="type__opportunities">${job.location}</span>
                <span>${job.type}</span>
            </div>
            <p class="opportunity-description">
                ${job.description}
            </p>
            <div class="see__positions__container">
                <span></span>
                <button class="see__position__btn">See positions
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" width="16"
                        height="16" stroke="currentColor" class="size-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5 21 12m0 0-7.5 7.5M21 12H3" />
                    </svg>
                </button>
            </div>
        </div>
    `;
}

function filterJobs(designation) {
    const container = document.getElementById('opportunities__right');
    let filteredJobs;

    if (designation === 'All') {
        filteredJobs = opportunitiesData.flatMap(dev => dev.jobs);
    } else {
        filteredJobs = opportunitiesData.find(dev => dev?.designation === designation)?.jobs || [];
    }

    container.innerHTML = filteredJobs.map(createOpportunityCard).join('');
    const activefilter=document.querySelectorAll('.title__container')

    document.getElementById('job-count').textContent = filteredJobs.length;

    // Update active link
    document.querySelectorAll('.filter-link').forEach(link => {

      link.classList.toggle('active', link.dataset.filter === designation);
      activefilter.forEach((d)=>d.to)

    });
}

document.addEventListener('DOMContentLoaded', function() {
    const filterLinks = document.querySelectorAll('.filter-link');
    filterLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            console.log(e.target.dataset.filter)
            filterJobs(e.target.dataset.filter);
        });
    });

    filterJobs('All'); // Initially show all jobs
});