$(document).ready(function(){
  $('.no-js').removeClass('no-js');
  $('.section').each(function(index){
    $(this).attr('id', 'section-'+index);
    $('.slide').each(function(index){
      $(this).attr('id', 'slide-'+index);
    });
  });

  $('#section-0').append('<div class="slide-more">slide<br><span>V</span></div>');

  $('#fullpage').fullpage({
    //Navigation 
    menu: true,
    navigation: false,
    navigationPosition: 'right',
    showActiveTooltips: true,
    slidesNavigation: true,
    slidesNavPosition: 'bottom',

    //Scrolling
    css3: true,
    scrollingSpeed: 700,
    scrollBar: false,
    easing: 'easeInOutCubic',
    easingcss3: 'ease',
    loopBottom: false,
    loopTop: false,
    loopHorizontal: true,
    scrollOverflow: false,
    touchSensitivity: 15,
    normalScrollElementTouchThreshold: 5,

    //Accessibility
    keyboardScrolling: true,
    animateAnchor: true,
    recordHistory: true,

    //Design
    controlArrows: true,
    verticalCentered: true,
    fixedElements: '#header, .footer',
    responsive: 1,
    paddingTop: '0',
    paddingBottom: '0',

    //events
    onLeave: function(index, nextIndex, direction){
      //$('.'+anchorLink).removeClass('loaded-opacity');
      //$('.slide-more').removeClass('loaded-opacity');
    },  
    afterLoad: function(anchorLink, index){
      $('.slide-more').addClass('loaded-opacity');
      $('.'+anchorLink).addClass('loaded-opacity');
    },
    afterRender: function(){},
    afterResize: function(){},
    afterSlideLoad: function(anchorLink, index, slideAnchor, slideIndex){},
    onSlideLeave: function(anchorLink, index, slideIndex, direction){}
  });
});