
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


    /* ---- For Mobile Menu Dropdown JS Start ---- */
      $('#menu span.opener').on("click", function() {
        if ($(this).hasClass("plus")) {
          $(this).parent().find('.mobile-sub-menu').slideDown();
          $(this).removeClass('plus');
          $(this).addClass('minus');
        }
        else
        {
          $(this).parent().find('.mobile-sub-menu').slideUp();
          $(this).removeClass('minus');
          $(this).addClass('plus');
        }
        return false;
      });
    /* ---- For Mobile Menu Dropdown JS End ---- */

    /*---Mobile menu icon Start---*/
    var navbar_toggle = $('.navbar-toggle i');
    var menu_var = $('#menu');
    $('.navbar-toggle').on("click", function(){
      
      if(menu_var.hasClass('menu-open')){
        menu_var.removeClass('menu-open');
        navbar_toggle.removeClass('fa-close');
        navbar_toggle.addClass('fa-bars');
      }else{
        menu_var.addClass('menu-open');
        navbar_toggle.addClass('fa-close');
        navbar_toggle.removeClass('fa-bars');
      }
      return false;
    });
    /*---Mobile menu icon End---*/

/* ------------ Account Tab JS Start ------------ */
    $('.account-tab-stap').on('click', 'li', function() {
        $('.account-tab-stap li').removeClass('active');
        $(this).addClass('active');
        
        $(".account-content").fadeOut();
        var currentLiID = $(this).attr('id');
        $("#data-"+currentLiID).fadeIn();
        return false;
    });


     /* Price-range Js Start */
 
      $( "#slider-range" ).slider({
        range: true,
        min: 0,
        max: 800,
        values: [ 75, 500 ],
        slide: function( event, ui ) {
          $( "#amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
        }
      });
      $( "#amount" ).val( "$" + $( "#slider-range" ).slider( "values", 0 ) + " - $" + $( "#slider-range" ).slider( "values", 1 ) );
 
  /* Price-range Js End */