// $(".num").counterUp({delay:10,time:1000});

// jQuery(document).ready(function() {
//     if( !jQuery('html').hasClass('.num') ) {
//     jQuery('.statistics .number-561b1dd77d2e1').counterUp({
//     delay: 20,
//     time: 1000
//     });
//     }
//     });

// $('.num').each(function() {
//     var $this = $(this),
//         countTo = $this.attr('data-count');
    
//     $({ countNum: $this.text()}).animate({
//       countNum: countTo
//     },
  
//     {
  
//       duration: 1000,
//       easing:'linear',
//       step: function() {
//         $this.text(Math.floor(this.countNum));
//       },
//       complete: function() {
//         $this.text(this.countNum);
//         //alert('finished');
//       }
  
//     });  
    
    
  
//   });

  $(window).scroll(function() {
    var hT = $('#scroll-to').offset().top,
        hH = $('#scroll-to').outerHeight(),
        wH = $(window).height(),
        wS = $(this).scrollTop();
    if (wS > (hT+hH-wH)){
        $('.num').each(function() {
            var $this = $(this),
                countTo = $this.attr('data-count');
            $({ countNum: $this.text()}).animate({
              countNum: countTo
            },
          
            {
          
              duration: 1000,
              easing:'linear',
              step: function() {
                console.log(this.countNum);
                $this.text(Math.floor(this.countNum));
              },
              complete: function() {
                $this.text(this.countNum);
                //alert('finished');
              }
          
            });  
            
            
          
          });
    }
 });