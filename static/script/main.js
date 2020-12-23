$(function() {
    //User Trict
    "user strict";
    /*Preloader animsition*/
    $(window).on('load', function () {
        $('.page-loader').fadeOut('slow', function () {
            $(this).remove();
        });
    });
    /*Navigation control*/
    var hamburgerAnimation = $(".hamburger.has-animation");
    var hamburgerNoAnimation = $(".hamburger");
    var navbar = $('.nav-right');
    var navbarVertical = $('.navbar-vertical .navbar-main');
    var navbarV3 = $('.navbar-center .navbar-menu');
    hamburgerAnimation.on("click", function () {
        hamburgerAnimation.toggleClass("is-active");
    });
    hamburgerNoAnimation.on("click", function () {
        navbar.toggleClass('opened');
        navbarV3.toggleClass('opened');
        navbarVertical.toggleClass('opened');
    });

    // Navbar menu caret
    $('.dropdown i').on('click', function (e) {
        $(this).siblings('.dropdown-menu').toggleClass('open');
        $(this).toggleClass('fa-rotate-180');
        e.stopPropagation();
    });

    /*Mini shop cart*/
    var miniCart = $('.mini-cart');
    $('.u-shop-cart .ic-cart').on('click', function () {
        miniCart.toggleClass('opened');
    });
    $(window).on('click', function (event) {
        if (!$(event.target).closest(miniCart).length && !$(event.target).closest('.u-shop-cart .ic-cart').length) {
            miniCart.removeClass('opened');
        }
    });

    /*Mini setting*/
    var miniSetting = $('.mini-setting');
    $('.ic-enjoy').on('click', function () {
        miniSetting.toggleClass('opened');
    });
    $(window).on('click', function (event) {
        if (!$(event.target).closest(miniSetting).length && !$(event.target).closest('.ic-enjoy').length) {
            miniSetting.removeClass('opened');
        }
    });

    // BUTTON SEARCH
    $('.ic-search').on('click', function () {
        $('.search').toggle(500);
    });

    // Slined Home 01 - Home_service -Banner
    $('#Home-service').show().revolution({
        responsiveLevels: [1920, 1600, 768, 480],
        gridwidth: [1240, 1024, 768, 600],
        sliderType: "standard",
        dottedOverlay: "none",
        sliderLayout: 'auto',
        gridheight: [800, 700, 600, 500],
        delay: 5000,
        spinner: 'spinner2',
        navigation: {
            onHoverStop: "off",
            arrows: {
                enable: false
            },
            bullets: {
                enable: false,
                style: 'hermes',
                hide_onleave: false,
                h_align: "center",
                v_align: "bottom",
                h_offset: 0,
                v_offset: 20,
                space: 5
            }
        }
    });

    // Slined Home 01 - Home_service - content
    $('#slide-home-service').show().revolution({
        responsiveLevels: [1920, 1600, 768, 480],
        gridwidth: [1240, 1024, 768, 600],
        sliderType: "standard",
        dottedOverlay: "none",
        sliderLayout: 'auto',
        gridheight: [500, 500, 500, 500],
        delay: 5000,
        spinner: 'spinner2',
        navigation: {
            onHoverStop: "off",
            arrows: {
                enable: true,
                style: 'hesperiden',
                hide_onleave: true,
                hide_under: 767
            },
            bullets: {
                enable: true,
                hide_onmobile: true,
                hide_under: 768,
                style: "hermes",
                hide_onleave: false,
                direction: "horizontal",
                h_align: "center",
                v_align: "bottom",
                h_offset: 0,
                v_offset: 30,
                space: 5,
                tmp: ''
            }
        }
    });

    // Slined Home 02 - Home_stote - Banner
    $('#slide-home-stote').show().revolution({
        responsiveLevels: [1920, 1600, 768, 480],
        gridwidth: [1240, 1024, 768, 600],
        sliderType: "standard",
        dottedOverlay: "none",
        sliderLayout: 'auto',
        gridheight: [800, 700, 600, 500],
        delay: 5000,
        spinner: 'spinner2',
        navigation: {
            onHoverStop: "off",
            arrows: {
                enable: true,
                style: 'uranus',
                hide_onleave: true,
                hide_under: 767
            },

            bullets: {
                enable: false,
                style: 'hermes',
                hide_onleave: false,
                h_align: "center",
                v_align: "bottom",
                h_offset: 0,
                v_offset: 20,
                space: 5
            }
        }
    });

    // Slined Home 03 - Home_portfolio - Banner
    $('#slide-home-portfolio').show().revolution({
        responsiveLevels: [1920, 1600, 768, 480],
        gridwidth: [1240, 1024, 768, 600],
        sliderType: "standard",
        dottedOverlay: "none",
        sliderLayout: 'auto',
        gridheight: [800, 700, 600, 500],
        delay: 5000,
        spinner: 'spinner2',
        navigation: {
            onHoverStop: "off",
            arrows: {
                enable: true,
                style: 'uranus',
                hide_onleave: true,
                hide_under: 767
            },

            bullets: {
                enable: false,
                style: 'hermes',
                hide_onleave: false,
                h_align: "center",
                v_align: "bottom",
                h_offset: 0,
                v_offset: 20,
                space: 5
            }
        }
    });

    //ACCORDION
    $('.collapse01').on('shown.bs.collapse', function () {
        $(this).parent().find(".fa-plus-circle").removeClass("fa-plus-circle").addClass("fa-minus-circle");

    }).on('hidden.bs.collapse', function () {
        $(this).parent().find(".fa-minus-circle").removeClass("fa-minus-circle").addClass("fa-plus-circle");
    });

    // trademark-list
    $('.trademark-list').owlCarousel({
        autoplay: true,
        loop: true,
        // margin:100,
        // nav:true,
        responsiveClass: true,
        responsive: {
            0: {
                items: 2,
                nav: true
            },
            480: {
                items: 3,
                nav: true
            },
            768: {
                items: 4,
                nav: false
            },
            992: {
                items: 8,
                nav: true,
                loop: false
            }
        }

    });

    //  Home_stote_V2 - Banner
    $('#slide-home-stoteV2').show().revolution({
        responsiveLevels: [1920, 1600, 768, 480],
        gridwidth: [1240, 1024, 768, 600],
        sliderType: "standard",
        dottedOverlay: "none",
        sliderLayout: 'auto',
        gridheight: [800, 700, 600, 500],
        delay: 5000,
        spinner: 'spinner2',
        navigation: {
            onHoverStop: "off",
            arrows: {
                enable: true,
                style: 'uranus',
                hide_onleave: true,
                hide_under: 767
            },

            bullets: {
                enable: true,
                hide_onmobile: true,
                hide_under: 768,
                style: "hermes",
                hide_onleave: false,
                direction: "horizontal",
                h_align: "center",
                v_align: "bottom",
                h_offset: 0,
                v_offset: 30,
                space: 5,
                tmp: ''
            }
        }
    });

    // Slined-home-portfolioV2
    $('#slide-home-portfolioV2').show().revolution({
        responsiveLevels: [1920, 1600, 768, 480],
        gridwidth: [1240, 1024, 768, 600],
        sliderType: "standard",
        dottedOverlay: "none",
        sliderLayout: 'auto',
        gridheight: [500, 500, 400, 400],
        delay: 5000,
        spinner: 'spinner2',
        navigation: {

            onHoverStop: "off",
            arrows: {
                enable: true,
                style: 'hesperiden',
                hide_onleave: true,
                hide_under: 767
            },

            bullets: {
                enable: true,
                hide_onmobile: true,
                hide_under: 768,
                style: "hermes",
                hide_onleave: false,
                direction: "horizontal",
                h_align: "center",
                v_align: "bottom",
                h_offset: 0,
                v_offset: 30,
                space: 5,
                tmp: ''
            }
        }
    });

    // slide-home-stoteV3
    $('#slide-home-stoteV3').show().revolution({
        responsiveLevels: [1920, 1600, 768, 480],
        gridwidth: [1240, 1024, 768, 600],
        sliderType: "standard",
        dottedOverlay: "none",
        sliderLayout: 'auto',
        gridheight: [500, 500, 400, 400],
        delay: 5000,
        spinner: 'spinner2',
        navigation: {

            onHoverStop: "off",
            arrows: {
                enable: true,
                style: 'hesperiden',
                hide_onleave: true,
                hide_under: 767
            },

            bullets: {
                enable: true,
                hide_onmobile: true,
                hide_under: 768,
                style: "hermes",
                hide_onleave: false,
                direction: "horizontal",
                h_align: "center",
                v_align: "bottom",
                h_offset: 0,
                v_offset: 30,
                space: 5,
                tmp: ''
            }

        }
    });

    // GAYLLERY GIRD
    function maso() {
        $('.grid').isotope({
            itemSelector: '.grid-item',
            // columnWidth: '.grid-sizer',
            percentPosition: true,
            layoutMode: 'fitRows',
            fitRows: {
                // gutter: 10,
                gutter: '.gutter-sizer'
            }
        });
    }
    var $Gird = $('.gallery-masonry-gird').isotope({
        itemSelector: '.grid-item',

    });
    $('.filters-button-group').on('click', 'li', function () {
        var filterValue = $(this).attr('data-filter');
        $Gird.isotope({
            filter: filterValue
        });
        return false;
    });
    maso();

    // categories li active sidebar
    $(".filters-button-group li").on('click', function () {
        $(".filters-button-group li").removeClass("active");
        $(this).addClass("active");
    });

    // GAYLLERY GIRDV2-HOME_Service_V2
    function mason() {
        $('.gridV2').isotope({
            itemSelector: '.grid-itemV2',
            // columnWidth: '.grid-sizerV2',
            percentPosition: true,
            layoutMode: 'fitRows',
            fitRows: {
                // gutter: 10,
                gutter: '.gutter-sizerV2'
            }
        });
    }
    var $GirdV2 = $('.gallery-masonry-girdV2').isotope({
        itemSelector: '.grid-itemV2',

    });
    $('.filters-button-groupV2').on('click', 'li', function () {
        var filterValue = $(this).attr('data-filter');
        $GirdV2.isotope({
            filter: filterValue
        });
        return false;
    });
    mason();

    // categories li active sidebarV2
    $(".filters-button-groupV2 li").on('click', function() {
        $(".filters-button-groupV2 li").removeClass("active");
        $(this).addClass("active");
    });


    // Slined Home 03 - Home_serviceV2 - Banner
    $('#slide-home-serviceV2').show().revolution({
        responsiveLevels: [1920, 1600, 768, 480],
        gridwidth: [1240, 1024, 768, 600],
        sliderType: "standard",
        dottedOverlay: "none",
        sliderLayout: 'auto',
        gridheight: [800, 700, 600, 500],
        delay: 5000,
        spinner: 'spinner2',
        navigation: {
            onHoverStop: "off",
            arrows: {
                enable: true,
                style: 'uranus',
                hide_onleave: false,
                hide_under: 767
            },

            bullets: {
                enable: true,
                hide_onmobile: true,
                hide_under: 768,
                style: "hermes",
                hide_onleave: false,
                direction: "horizontal",
                h_align: "center",
                v_align: "bottom",
                h_offset: 0,
                v_offset: 30,
                space: 5,
                tmp: ''
            }
        }
    });



    // slide-home-stoteV3
    $('#home-serviceV2').show().revolution({
        responsiveLevels: [1920, 1600, 768, 480],
        gridwidth: [1240, 1024, 768, 600],
        sliderType: "standard",
        dottedOverlay: "none",
        sliderLayout: 'auto',
        gridheight: [721, 721, 721,721],
        delay: 5000,
        spinner: 'spinner2',
        navigation: {

            onHoverStop: "off",
            arrows: {
                enable: false,
                style: 'hesperiden',
                hide_onleave: true,
                hide_under: 767
            },

            bullets: {
                enable: true,
                hide_onmobile: true,
                hide_under: 768,
                style: "hermes",
                hide_onleave: false,
                direction: "horizontal",
                h_align: "center",
                v_align: "bottom",
                h_offset: 0,
                v_offset: 30,
                space: 5,
                tmp: ''
            }

        }
    });

    // trademark-listV2
    $('.trademark-listV2').owlCarousel({
        autoplay: true,
        loop: true,
        // margin:100,
        // nav:true,
        responsiveClass: true,
        responsive: {
            0: {
                items: 2,
                nav: true
            },
            480: {
                items: 3,
                nav: true
            },
            768: {
                items: 4,
                nav: false
            },
            992: {
                items: 6,
                nav: true,
                loop: true
            }
        }
    });

    // Download file 
    $("#fileRequest").on('click', function () {
        window.location = 'file.doc';
    });

    // TIME
    function makeTimer() {

        var endTime = new Date("September 10, 2017 18:00:00 PDT");
        var endTime = (Date.parse(endTime)) / 1000;

        var now = new Date();
        var now = (Date.parse(now) / 1000);

        var timeLeft = endTime - now;

        var days = Math.floor(timeLeft / 86400);
        var hours = Math.floor((timeLeft - (days * 86400)) / 3600);
        var minutes = Math.floor((timeLeft - (days * 86400) - (hours * 3600)) / 60);
        var seconds = Math.floor((timeLeft - (days * 86400) - (hours * 3600) - (minutes * 60)));

        if (hours < "10") {
            hours = "0" + hours;
        }
        if (minutes < "10") {
            minutes = "0" + minutes;
        }
        if (seconds < "10") {
            seconds = "0" + seconds;
        }

        $("#days").html(days + "<div class='timer-desc'>Days</div>");
        $("#hours").html(hours + "<div class='timer-desc'>Hours</div>");
        $("#minutes").html(minutes + "<div class='timer-desc'>Minutes</div>");
        $("#seconds").html(seconds + "<div class='timer-desc'>Seconds</div>");

    }

    setInterval(function () {
        makeTimer();
    }, 1000);

    // quantity
    $('.quantity').each(function () {
        var spinner = $(this),
            input = spinner.find('input[type="number"]'),
            btnUp = spinner.find('.quantity-up'),
            btnDown = spinner.find('.quantity-down'),
            min = input.attr('min'),
            max = input.attr('max');

        btnUp.on('click', function() {
            var oldValue = parseFloat(input.val());
            var newVal;
            if (oldValue >= max) {
                newVal = oldValue;
            } else {
                newVal = oldValue + 1;
            }
            spinner.find("input").val(newVal);
            spinner.find("input").trigger("change");
        });

        btnDown.on('click', function() {
            var oldValue = parseFloat(input.val());
            var newVal;
            if (oldValue <= min) {
                newVal = oldValue;
            } else {
                newVal = oldValue - 1;
            }
            spinner.find("input").val(newVal);
            spinner.find("input").trigger("change");
        });
    });
    
    // accordion-watering
    $('.collapse02').on('shown.bs.collapse', function () {
        $(this).parent().find(".fa-plus").removeClass("fa-plus").addClass("fa-minus");

    }).on('hidden.bs.collapse', function () {
        $(this).parent().find(".fa-minus").removeClass("fa-minus").addClass("fa-plus");
    });
    // clientSay
    $('.clientSay-box').owlCarousel({
            autoplay:true,
            loop:true,
            responsiveClass:true,
            responsive:{
                0:{
                    items:1,
                    nav:true
                },
                320:{
                    items:1,
                    nav:true
                },
                768:{
                    items:2,
                    nav:false
                }
            }

        });
     // Back to top
    $(window).on('scroll', function() {
        if ($(this).scrollTop() != 0) {
          $('#bttop').fadeIn();
        } else {
          $('#bttop').fadeOut();
        }
    });

    $('#bttop').on('click', function() {
         $('body,html').animate({
            scrollTop: 0
         }, 800);
    });

    // slide button filter
    $(document).ready(function(){
        $("button.filter").on('click', function(){
            $("div.box-filter").toggle(500);

        });
    });
    // BUTTON SEARCHV2
    $(function () {
         $('.fa-search').stop().click( function(){
            $check = $(".searchV2");
            if($check.hasClass("add-transitions"))
            {
                $check.removeClass("add-transitions");
            }
            else 
            {
                $check.addClass("add-transitions");
            }
        })
    });
    // scrollTop
    var nav = $('.aaaa');
    $(window).scroll(function () {
        if ($(this).scrollTop() > 40) {
            nav.addClass("scollView");

        } else {
            nav.removeClass("scollView");

        }
    });

    function detectMouseWheelDirection( e )
    {
        var delta = null,
            direction = false
        ;
        if ( !e ) { // if the event is not provided, we get it from the window object
            e = window.event;
        }
        if ( e.wheelDelta ) { // will work in most cases
            delta = e.wheelDelta / 60;
        } else if ( e.detail ) { // fallback for Firefox
            delta = -e.detail / 2;
        }
        if ( delta !== null ) {
            direction = delta > 0 ? 'up' : 'down';
        }

        return direction;
    }
    function handleMouseWheelDirection( direction )
    {
        console.log( direction ); // see the direction in the console
        if ( direction == 'down' ) {
            console.log( 11111 );
            var nav = $('.aaaa');

            nav.removeClass("fixed");

            // do something, like show the next page
        } else if ( direction == 'up' ) {
            var nav = $('.aaaa');
            nav.addClass("fixed");


            // do something, like show the previous page
        } else {
            // this means the direction of the mouse wheel could not be determined
        }
    }
    document.onmousewheel = function( e ) {
        handleMouseWheelDirection( detectMouseWheelDirection( e ) );
    };
    if ( window.addEventListener ) {
        document.addEventListener( 'DOMMouseScroll', function( e ) {
            handleMouseWheelDirection( detectMouseWheelDirection( e ) );
        });
    }
    // FAQs ACCORDION
    $('.collapse').on('shown.bs.collapse', function(){
        $(this).parent().find(".fa-plus").removeClass("fa-plus").addClass("fa-minus");
        $(this).parent().find(".faq-head").css({
            'background':'#c19b76 ',
        });
    }).on('hidden.bs.collapse', function(){
        $(this).parent().find(".fa-minus").removeClass("fa-minus").addClass("fa-plus");
        $(this).parent().find(".faq-head").css({
            'background':'#333',
        });
    });

    $('.collapse.in').prev('.panel-heading').addClass('active');
    $('#accordion, #bs-collapse')
        .on('show.bs.collapse', function(a) {
            $(a.target).prev('.panel-heading').addClass('active');
        })
        .on('hide.bs.collapse', function(a) {
            $(a.target).prev('.panel-heading').removeClass('active');
        });

});



//slide zoom product detail

;(function($){

    'use strict';

    $.mad_core = $.mad_core || {};

    $.mad_core = {

        setUp: function (options) {
            var base = this;

            var animEndEventNames = {
                    'WebkitAnimation' : 'webkitAnimationEnd',
                    'OAnimation' : 'oAnimationEnd',
                    'msAnimation' : 'MSAnimationEnd',
                    'animation' : 'animationend'
                },
                transEndEventNames = {
                    'WebkitTransition': 'webkitTransitionEnd',
                    'MozTransition': 'transitionend',
                    'OTransition': 'oTransitionEnd',
                    'msTransition': 'MSTransitionEnd',
                    'transition': 'transitionend'
                }

            base.$window = $(window);
            base.ANIMATIONEND = animEndEventNames[ Modernizr.prefixed('animation') ];
            base.TRANSITIONEND = transEndEventNames[ Modernizr.prefixed('transition') ];
            base.SUPPORT = {
                animations : Modernizr.csstransitions && Modernizr.cssanimations,
                ANIMATIONSUPPORTED: Modernizr.cssanimations,
                TRANSITIONSUPPORTED: Modernizr.csstransitions,
                ISRTL: getComputedStyle(document.body).direction === 'rtl',
                ISTOUCH: Modernizr.touch
            };
            base.XHRLEVEL2 = !!window.FormData;
            base.event = base.SUPPORT.ISTOUCH ? 'touchstart' : 'click';

            // Refresh elements
            base.refresh();
        },

        DOMLoaded: function(options) {

            var base = this;

            // set up
            base.setUp(options);

            // counters
            if($('.counter').length) base.counters();

            // responsive menu
            if($('#header').length) base.navInit.init(this);

            // search
            if($('.search-holder').length) base.searchHolder();

            // background load
            if($('[data-bg]').length) base.bg();

            // sync carousel
            if($('.owl-carousel[data-sync]').length) base.syncOwlCarousel.init();

            // hidden elements init
            if($('.hidden-section').length) base.hiddenSections();

            // dropdown elements init
            if($('.dropdown-invoker').length) base.dropdown();

            // close btn init
            if($('.item-close').length) base.closeBtn();
            if($('.shopping-cart-full').length) base.removeProduct();

        },

        elements: {
            '.main-navigation, .topbar:not(.no-mobile-advanced)': 'navMain',
            '#mobile-advanced': 'navMobile',
            '#wrapper': 'wrapper',
            '#header' : 'header'
        },

        /*
        Plugin Name:    Refresh
        */
        $: function (selector) {
            return $(selector);
        },

        refresh: function() {
            for (var key in this.elements) {
                this[this.elements[key]] = this.$(key);
            }
        },


        /**
         * Emulates single accordion item
         * @param Function callback
         * @return jQuery collection;
         **/
        hiddenSections: function(callback){

            var collection = $('.hidden-section');
            if(!collection.length) return;

            collection.each(function(i, el){
                $(el).find('.content').hide();
            });

            collection.on('click.hidden', '.invoker', function(e){

                e.preventDefault();

                var content = $(this).closest('.hidden-section').find('.content');

                content.slideToggle({
                    duration: 500,
                    easing: 'easeOutQuint',
                    complete: callback ? callback : function(){}
                });

            });

            return collection;

        },



        /**
         Sync Owl Carousel
         **/
        syncOwlCarousel: {

            init: function(){

                this.collection = $('.owl-carousel[data-sync]');
                if(!this.collection.length) return false;

                this.bindEvents();

            },

            bindEvents: function(){

                var self = this;

                this.collection.each(function(i, el){

                    var $this = $(el),
                        sync = $($this.data('sync'));

                    if(!sync.length){
                        console.log('Not found carousel with selector ' + $this.data('sync'));
                        return;
                    }

                    // nav
                    $this.on('click', '.owl-prev', function(e){
                        sync.trigger('prev.owl.carousel');
                    });
                    $this.on('click', '.owl-next', function(e){
                        sync.trigger('next.owl.carousel');
                    });

                    sync.on('click', '.owl-prev', function(e){
                        $this.trigger('prev.owl.carousel');
                    });
                    sync.on('click', '.owl-next', function(e){
                        $this.trigger('next.owl.carousel');
                    });

                    // // drag
                    $this.on('dragged.owl.carousel', function(e){

                        if(e.relatedTarget.state.direction == 'left'){
                            sync.trigger('next.owl.carousel');
                        }
                        else{
                            sync.trigger('prev.owl.carousel');
                        }

                    });

                    sync.on('dragged.owl.carousel', function(e){

                        if(e.relatedTarget.state.direction == 'left'){
                            $this.trigger('next.owl.carousel');
                        }
                        else{
                            $this.trigger('prev.owl.carousel');
                        }

                    });

                });

            }

        },

        /**
         Adds background image
         * @return undefined;
         **/
        bg: function(collection){

            var collection = collection ? collection : $('[data-bg]');

            collection.each(function(){

                var $this = $(this),
                    bg = $this.data('bg');

                if(bg) $this.css('background-image', 'url('+bg+')');

            });

        },

        navInit : {

            init : function (base) {

                this.createResponsiveButtons.call(base);
                this.navProcess(base);

                if ( base.SUPPORT.ISTOUCH ) {
                    this.touchNavEvent(base);
                }
            },

            touchNavEvent: function (base) {
                var clicked = false;

                $("li.menu-item-has-children > a, li.cat-parent > a, li.page-item-has-children > a").on(base.event, function (e) {
                    if (clicked != this) {
                        e.preventDefault();
                        clicked = this;
                    }
                });
            },

            navProcess: function (base) {

                base.navInit.touchNav(base, base.$window);

                $(window).resize(function (e) {
                    setTimeout(function () {
                        base.navInit.touchNav(base, e.currentTarget);
                    }, 30);
                });

            },

            touchNav: function (base, target) {

                if (base.SUPPORT.ISTOUCH || $(target).width() < 992) {

                    if (!base.navMobile.children('ul').length) {
                        base.navMobile.append(base.navMain.html());
                    }

                    base.navButton.on(base.event, function (e) {
                        e.preventDefault();

                        if (!base.wrapper.is('.active')) {
                            $('html, body').animate({ scrollTop: 0 }, 0, function () {
                                base.wrapper.css({
                                    height: base.navMobile.children('ul').outerHeight(true)
                                }).addClass('active');
                            });
                        }
                    });

                    base.navHide.on(base.event, function (e) {
                        e.preventDefault();
                        if (base.wrapper.is('.active')) {
                            base.wrapper.css({ height: 'auto' }).removeClass('active');
                        }
                    });

                } else {
                    base.navMobile.children('ul').remove();
                }
            },

            createResponsiveButtons : function () {

                this.navButton = $('<button></button>', {
                    id: 'responsive-nav-button',
                    'class': 'responsive-nav-button'
                }).insertBefore(this.navMain);

                this.navHide = $('<a></a>', {
                    id: 'advanced-menu-hide',
                    'href' : '#'
                }).insertBefore(this.navMobile);

            },

        }

    }

    $(function(){

        $.mad_core.DOMLoaded();

    });

    $(function(){

        document.addEventListener("touchstart", function() {},false);

        /* ---------------------------------------------------- */
        /*  Gallery carousel                                    */
        /* ---------------------------------------------------- */

        var pageCarousel = $('.owl-carousel');

        if(pageCarousel.length){

            $('.owl-carousel').not('#thumbnails').each(function(){

                /* Max items counting */
                var max_items = $(this).data('max-items');
                var tablet_items = max_items;
                if(max_items > 1){
                    tablet_items = max_items - 1;
                }
                var smart_items = max_items;
                if(max_items > 3){
                    smart_items = max_items - 2;
                }
                var mobile_items = 1;

                var autoplay_carousel = $(this).data('autoplay');

                var center_carousel = $(this).data('center');

                var item_margin = $(this).data('item-margin');

                /* Install Owl Carousel */
                $(this).owlCarousel({
                    smartSpeed : 450,
                    nav : true,
                    loop  : true,
                    autoplay : autoplay_carousel,
                    center: center_carousel,
                    navText : false,
                    margin: item_margin,
                    lazyLoad: true,
                    rtl: $.mad_core.SUPPORT.ISRTL ? true : false,
                    responsiveClass:true,
                    responsive : {
                        0:{
                            items:mobile_items
                        },
                        480:{
                            items:smart_items
                        },
                        768:{
                            items:tablet_items
                        },
                        992:{
                            items:max_items
                        }
                    },
                    dotsContainer: '#carousel-custom-dots',
                    dotsClass: '.owl-dot',
                    dotsEach:true
                });

                // Call Vars
                var owl = $('.owl-carousel');

                $( '.owl-dot' ).on( 'click', function() {
                    owl.trigger('to.owl.carousel', [$(this).index(), 300]);
                    $( '.owl-dot' ).removeClass( 'active' );
                    $(this).addClass( 'active' );
                })

            });

            if($('#thumbnails').length){
                $('#thumbnails').each(function(){

                    /* Max items counting */
                    var data = $(this).data();
                    var max_items = $(this).data('max-items');
                    var tablet_items = max_items;
                    if(max_items > 1){
                        tablet_items = max_items - 1;
                    }
                    var mobile_items = 1;

                    var autoplay_carousel = $(this).data('autoplay');

                    $(this).owlCarousel({
                        items : max_items,
                        URLhashListener : false,
                        navSpeed : 800,
                        // nav : false,
                        nav : true,
                        loop : true,
                        margin: 10,
                        rtl: $.mad_core.SUPPORT.ISRTL ? true : false,
                        // navText:false,
                        responsive : {
                            0:{
                                items:tablet_items,
                                nav : true
                            },
                            481:{
                                items:max_items,
                                nav : true
                            },
                            1200:{
                                items:max_items,
                                nav : true
                            }
                        }
                    });
                });

            }

        }

        /* ---------------------------------------------------- */
        /*  Elevate zoom                                        */
        /* ---------------------------------------------------- */

        if($('[data-zoom-image]').length){

            var button = $('.qv-preview');

            $("#zoom-image").elevateZoom({
                gallery:'thumbnails',
                galleryActiveClass: 'active',
                zoomType: "inner",
                cursor: "crosshair",
                responsive:true,
                zoomWindowFadeIn: 500,
                zoomWindowFadeOut: 500,
                easing:true,
                lensFadeIn: 500,
                lensFadeOut: 500
            });

        }

        /* ---------------------------------------------------- */
        /*  Custom Select                                       */
        /* ---------------------------------------------------- */

        if ($('.custom-select').length) {
            $('.custom-select').madCustomSelect();
        }

        /* ---------------------------------------------------- */
        /*  Tabs                                                */
        /* ---------------------------------------------------- */

        $(window).on("load",function(){

            var tabs = $('.tabs-section');
            if(tabs.length){
                tabs.tabs({
                    beforeActivate: function(event, ui) {
                        var hash = ui.newTab.children("li a").attr("href");
                    },
                    hide : {
                        effect : "fadeOut",
                        duration : 450
                    },
                    show : {
                        effect : "fadeIn",
                        duration : 450
                    },
                    updateHash : false
                });
            }

        });

    });

    $('.our-story1').click(function(event) {
        event.preventDefault();
        var html = '<video controls src="images/video.mp4" width="100%" autoplay>';
        $(this).html(html);
    });

})(jQuery);