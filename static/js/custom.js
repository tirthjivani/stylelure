
     $('.sslider').slick({
       dots: false,
  infinite: true,
  speed: 300,
  slidesToShow: 1,
  prevArrow: '<button class="slick-prev" aria-label="Previous" type="button"><i class="fa fa-angle-left"></i></button>',
  nextArrow: '<button class="slick-next" aria-label="Next" type="button"><i class="fa fa-angle-right"></i></button>',
     });

     $('.best_seller_slider').slick({
     		speed: 500,
     		slidesToShow: 4,
     		slidesToScroll: 1,
     		infinite: false,
     		dots:false,
         responsive: [
           {
             breakpoint:1024,
             settings: {
               slidesToShow: 3,
               slidesToScroll: 1
             }
           },
           {
             breakpoint:768,
             settings: {
               slidesToShow: 3,
               slidesToScroll: 1
             }
           },
           {
             breakpoint:767,
             settings: {
               slidesToShow: 2,
               slidesToScroll: 1
             }
           },
           {
             breakpoint:500,
             settings: {
               slidesToShow: 1,
               slidesToScroll: 1,
               autoPlay: true
             }
           }
         ]
     	});

      $('.partner_slider').slick({
      		speed: 500,
      		slidesToShow: 4,
      		slidesToScroll: 1,
      		infinite: false,
      		dots:false,
          responsive: [
            {
              breakpoint:1199,
              settings: {
                slidesToShow: 3,
                slidesToScroll: 1
              }
            },
            {
              breakpoint:768,
              settings: {
                slidesToShow: 3,
                slidesToScroll: 1
              }
            },
            {
              breakpoint:767,
              settings: {
                slidesToShow: 2,
                slidesToScroll: 1
              }
            },
            {
              breakpoint:500,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                autoPlay: true
              }
            }
          ]
      	});

      $('.slider-big').slick({
	  slidesToShow: 1,
	  slidesToScroll: 1,
	  arrows: false,
	  fade: true,
	  asNavFor: '.slider-thumb'
	});
	$('.slider-thumb').slick({
	  slidesToShow: 3,
	  slidesToScroll: 3,
	  dots: true,
	  centerMode: true,
	  focusOnSelect: true,
	  fade: false,
	  infinite: true,
	  asNavFor: '.slider-big'
	});
