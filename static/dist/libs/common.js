window.onload = function() {
	var popup = new Popup();

	var play;

	function onYouTubePlayerAPIReady() {
		play = new YT.Player('GNCvideo', {
			videoId: 'tD_mGEcAi9Q',  
			host: 'https://www.youtube.com',
			controls: 0,
			modestbranding: 1, 
			loop: 1
		});

		$('#videoClose').on('click', function(e) {
			play.pauseVideo();
		});

		$('.popup').on('click', function(e) {
			play.pauseVideo();
		});
	}

	onYouTubePlayerAPIReady();

	$('.btn-play').on('click', function() {
		popup.open($('.popup #site-video'));
	});

	$('#btn-login').on('click', function() {
		popup.open($('#form-login'));
	});

	$('#btn-registration').on('click', function() {
		popup.open($('#form-registration'));
	});

	var time = $('.timer').data('time')
	var timer = new Timer(time);

	timer.setDate($('#days'), $('#hours'), $('#minutes'),
		$('#seconds'));

	$('.mobile-btn').on('click', function(e) {
		$(this).toggleClass('active');

		if ($(this).hasClass('active')) {
			$('.mobile-menu').stop(true, true).css({
				display: "flex",
				opacity: 0
			}).animate({
				opacity: 1
			})
		}else {
			$('.mobile-menu').stop(true, true).fadeOut();
		}
		$('.mobile-menu').toggleClass('active');
	});

	$('.mobile-menu__link').on('click', function(e) {
		$('.mobile-btn').removeClass('active');
		$('.mobile-menu').stop(true, true).fadeOut();
	});

	new Slider('#credit-slider-1', 0, 10000);
	new Slider('#credit-slider-2', 0, 10000);

	$('.btn-example').on('click', function(e) {
		$('.btn-example').removeClass('is-active');
		$(this).addClass('is-active');

		var data = $(this).data('example');

		var img = $('img[data-example="' + data + '"]');

		$('.diagram__image').removeClass('is-active');
		img.addClass('is-active');
	});

	$('.b-spoiler h3').on('click', function(e) {
		$('.b-spoiler h3').not($(this)).removeClass('is-active');
		$(this).toggleClass('is-active');
	});

	/*#Progress bar circle*/

	(function() {
		if (document.querySelector('.main__progress-heart') == null) return;
		var circle = new ProgressBar.Circle('.main__progress-heart', {
			color: '#0C9BE3',
			strokeWidth: 20,
			trailWidth: 20,
			trailColor: '#303744',
			svgStyle: {
				display: 'block',
				width: '100%'
			}
		});

		circle.set(0.4);
		var graphImages1 = $('#graph-1 .graph__img');
		var mainImg1 = $('#graph-1 .img-main');
		var changinImages1 = $('#graph-1 .graph__img:not(.img-main)');
		var selector1 = $('#graph-1 .graph-info__item');
		var graphImages2 = $('#graph-2 .graph__img');
		var mainImg2 = $('#graph-2 .img-main');
		var changinImages2 = $('#graph-2 .graph__img:not(.img-main)');
		var selector2 = $('#graph-2 .graph-info__item');
		graphChange(selector1, graphImages1, mainImg1, changinImages1);
		graphChange(selector2, graphImages2, mainImg2, changinImages2);

	})($);
	
	$(".header__nav-link").mPageScroll2id();
	$(".mobile-menu__link").mPageScroll2id();
	$(".footer__nav-link").mPageScroll2id();

	$(".step").on("mouseover", function(e) {
		$(".step").removeClass("is-active");
		$(this).addClass("is-active");
	});
};

function graphChange(selector, graphImages, mainImg, changinImages) {
	selector.on('mouseover', function(e) {
		graphImages.not($(this)).css({
			opacity: '0'
		});

		var data = $(this).data('img');
		var dataImg = $('.'+ data);
		dataImg.css({opacity: '1'});
	});

	selector.on('mouseout', function(e) {
		mainImg.css({
			opacity: '1'
		});

		changinImages.css({
			opacity: '0'
		});
	});
}

function Popup() {
	var popup = $('.popup');
	var self = this;
	var popupFade = 200;
	var contentFade = 200;

	self.open = function(content) {
		self.content = content;
		popup.fadeIn(popupFade);	
		content.fadeIn(contentFade);
	}

	self.close = function(e) {
		var targ = e.target;

		if (!targ.classList.contains('popup') 
			&& !targ.classList.contains('popup__close')) return;
			$('.popup-content').fadeOut(contentFade);
		popup.fadeOut(popupFade);
	}

	self.changeContent = function(changeEl) {
		self.content.fadeOut(contentFade, function() {
			changeEl.fadeIn(contentFade);
		});
	}

	popup.on('click', self.close);
}

function Timer(date) {
	var self = this;

	self.countDownDate = new Date(date).getTime();

	self.setDate = function(days, hours, minutes, seconds) {
		var x = setInterval(function() {

			var now = new Date().getTime();

			var distance = self.countDownDate - now;

			var d = Math.floor(distance / (1000 * 60 * 60 * 24));
			var h = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
			var m = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
			var s = Math.floor((distance % (1000 * 60)) / 1000);

			function pretty_time_string(num) {
				return ( num < 10 ? "0" : "" ) + num;
			}

			days.text(pretty_time_string(d));
			hours.text(pretty_time_string(h));
			minutes.text(pretty_time_string(m));
			seconds.text(pretty_time_string(s));

			if (distance < 0) {
				clearInterval(x);
				days.html('00');
				hours.html('00');
				minutes.html('00');
				seconds.html('00')
			}
		}, 1000);
	}
}

function Slider(initialId, min, max) {

	if (document.querySelector(initialId) == null) return;

	var sliderHandle = $(initialId + ' .ui-slider-val');

	$(initialId).slider({
		min: min,
		max: max,
		range: "min",
		animate: "slow",
		slide: function( event, ui) {
			sliderHandle.html('$' + ui.value);
		}
	});
}