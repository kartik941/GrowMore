document.addEventListener('DOMContentLoaded', function () {

    document.querySelector('.fa-bars').addEventListener('click', function () {
        this.classList.toggle('fa-times');
        document.querySelector('.navbar').classList.toggle('nav-toggle');
    });

    window.addEventListener('load', function () {
        document.querySelector('.fa-bars').classList.remove('fa-times');
        document.querySelector('.navbar').classList.remove('nav-toggle');

        window.addEventListener('scroll', function () {
            if (window.pageYOffset > 35) {
                document.querySelector('.header').style.background = '#002e5f';
                document.querySelector('.header').style.boxShadow = '0 .2rem .5rem rgba(0,0,0,.4)';
            } else {
                document.querySelector('.header').style.background = 'none';
                document.querySelector('.header').style.boxShadow = 'none';
            }
        });
    });

    const counters = document.querySelectorAll('.counter');
    const speed = 120;
    counters.forEach(counter => {
        const updateCount = () => {
            const target = +counter.getAttribute('data-target');
            let count = +counter.innerText;
            const inc = target / speed;
            if (count < target) {
                count += inc;
                counter.innerText = Math.ceil(count);
                setTimeout(updateCount, 1);
            } else {
                counter.innerText = target;
            }
        };
        updateCount();
    });

    (function () {
        "use strict";

        function owlCarouselInit(selector, items) {
            const options = {
                autoplay: true,
                dots: true,
                loop: true,
                responsive: {
                    0: { items: 2 },
                    768: { items: 4 },
                    900: { items: 6 }
                }
            };
            const element = document.querySelector(selector);
            if (element) {
                Object.assign(options.responsive, items);
                new OwlCarousel(element, options);
            }
        }

        owlCarouselInit(".clients-carousel", {});
        owlCarouselInit(".testimonials-carousel", {
            0: { items: 1 },
            576: { items: 2 },
            768: { items: 3 },
            992: { items: 4 }
        });
    })();

    window.addEventListener('scroll', function () {
        if (window.pageYOffset > 100) {
            document.querySelector('.back-to-top').style.display = 'block';
        } else {
            document.querySelector('.back-to-top').style.display = 'none';
        }
    });

    document.querySelector('.back-to-top').addEventListener('click', function () {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    document.querySelectorAll('.accordion-header').forEach(function (accordionHeader) {
        accordionHeader.addEventListener('click', function () {
            document.querySelectorAll('.accordion .accordion-body').forEach(function (accordionBody) {
                accordionBody.style.display = 'none';
            });
            this.nextElementSibling.style.display = 'block';
            document.querySelectorAll('.accordion .accordion-header span').forEach(function (span) {
                span.innerText = '+';
            });
            this.querySelector('span').innerText = '-';
        });
    });

});
