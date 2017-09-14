    $(document).ready(function(){
      // $('body').scrollspy({ target: '#navbar-magic' });
      // Add smooth scrolling to all links
      $("a").on('click', function(event) {
        // Make sure this.hash has a value before overriding default behavior
        if (this.hash !== "") {
          // Prevent default anchor click behavior
          event.preventDefault();
          // Store hash
          var hash = this.hash;
          // Using jQuery's animate() method to add smooth page scroll
          // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
          $('html, body').animate({
            scrollTop: $(hash).offset().top
          }, 800, function(){
            // Add hash (#) to URL when done scrolling (default click behavior)
            window.location.hash = hash;
          });
        } // End if
      });

      // $('li').click(function(e) {
      //   e.preventDefault();
      //   $(this).addClass('active');
      //   var elem = $(this).addClass('active');
      //   console.log("Clicked");
      //   if ($('li').click(function(e) {
      //     $(elem).removeClass('active');
      //     console.log("Another Clicked");
      //     $(this).addClass('active');
      //   }));
      // });
      //
      $(window).scroll(function(e) {
        e.preventDefault();
        if ($(this).scrollTop() == 0) {
          $('.home-track').addClass('active');
          $('.navbar-nav, .nav-item, .nav-link').css({'color':'rgb(250, 254, 251)'});

        }

        if ($(this).scrollTop() > 300) {
          $('.navbar-nav, .nav-item, .nav-link').css({'color':'rgb(250, 254, 251)'});
          $('.home-track').removeClass('active');
        } else {
          $('li').removeClass();
        }
      });

    });
