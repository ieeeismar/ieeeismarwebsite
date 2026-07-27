/**
 * File tabs.jquery-plugin.js.
 *
 * Handles toggling the navigation menu for small screens and enables TAB key
 * navigation support for dropdown menus.
 */
( function($) {
	const ns = 'plethoraplugins';
	const dataNS = 'pds-tabs--';
	const pds = 'pds';
	const classToAdd = 'js-' + ns + '-tabs';
	const classToAddToLinks = 'js-' + ns + '-tabs--link'; //adding a class to the link will prevent the default link styles from kicking in.
	const activeClass = 'active';
	const linkSelector = 'a[href]';
	const headerSelector = 'h1,h2,h3,h4,h5,h6';
	const isMobileClass = ns + '-tabs-mobile';
	const initialHash = window.location.hash;
	const defaultSettings = {
		mobileDisplay: null,// determines how to display this for mobile devices. Options: 'accordion'
		mobileBreakpoint: null,//determines the breakpoint at which the mobile display takes effect.  Options: an integer representing the max width, or 'auto' (in which case the assumption is that this is a 'horizontal' tab, and that all tabs should fit the browser's screen width)
		mobileBreakpointForced: '', // if set, it will be considered mobile below this threshold (example: 500 for 500px)
		accordionAutoClose: true, //if responsive behavior of vertical tab results in an accordion, should it auto close?
		responsiveAccordionsCollapsedInitially: false, //if responsive behavior of vertical tab results in an accordion, should all accordion items be collapsed initially?
		responsiveAccordionsBreakpoint: false, //set this to a valid css breakpoint value, like 500px, where you want to always have it collapse to accordion
	};
	const scrollIntoViewOptions = {behavior: "smooth"};
	let sideNavNumber = 0;
	if(!$.fn.scrollIntoViewIfNeeded) $.fn.scrollIntoViewIfNeeded = function(){
		if (this.length) {
			if(this[0].scrollIntoViewIfNeeded) this[0].scrollIntoViewIfNeeded(scrollIntoViewOptions);
			else this[0].scrollIntoView(scrollIntoViewOptions);
		}
		return this;
	};

	$.fn[ns + 'Tabs'] = function(inputOptions){
		const options = $.extend({}, defaultSettings, inputOptions);
		return this.each(function(){
			const $nav = $(this);
			if ($nav.hasClass(classToAdd)) return; //prevent double initialization
			$nav.addClass(classToAdd);
			$nav.attr('role', 'tablist').children('li').attr('role','presentation');
			if(options.layout == 'vertical') $nav.attr('aria-orientation', 'vertical');
			if(options.layout == 'horizontal') $nav.attr('aria-orientation', 'horizontal');
			var linkIds = [];
			
			const $container = $nav.closest('.' + ns + '-tabs-container');
			const $contentContainer = $container.find('.' + ns + '-sidenavjump-content:first,.' + ns + '-tabs--content:first');
			let $mobileDisplay = null;
			let isMobile = false;
			sideNavNumber++;
			$nav.attr('data-' + dataNS + 'tab-number', sideNavNumber);
			const $header = $nav.prev(headerSelector);
			if($header.length && !$nav.attr('aria-labelledby')) {
				let headerId = $header.attr('id');
				if(!headerId) {
					headerId = ns + 'tab_' + sideNavNumber + '_header';
					$header.attr('id', headerId);
				}
				$nav.attr('aria-labelledby', headerId);
			}
			let $tabButtons = null;
			const intializeTabButtons = function(){
				$tabButtons = $nav.find(linkSelector).each(function(index){
					const $link = $(this).addClass(classToAddToLinks);
					if(!$link.attr('id')) $link.attr('id', ns + 'tab_' + sideNavNumber + '_tablink_' + index);
					linkIds.push($link.attr('id'));
					if(!$link.attr('role')) $link.attr('role', 'tab');
					if($link.hasClass(activeClass))  $link.attr('aria-selected', 'true').removeAttr('tabindex');
					else $link.attr('aria-selected', 'false').attr('tabindex', '-1');
					const href = $link.attr('href');
					if(!href || !href.charAt(0) == '#') return;
					let $content = $(href).attr('aria-hidden', 'true');
					if(!$content.length) {
						if($contentContainer.length){
							var children = $contentContainer.children();
							if (children.length > index) $content = $(children[index]);
							else return;
						}
						else return;
					}
					if(!$content.attr('id')) $content.attr('id', href.replace('#', ''));
					if($link.hasClass('active')) $content.addClass('active').attr('aria-hidden', 'false');
					$content.addClass('js-' + ns + '-tab-panel');
					$link.attr('aria-controls', $content.attr('id'));
					if(!$content.attr('role')) $content.attr('role', 'tabpanel');
					if(!$content.attr('aria-labelledby')) $content.attr('aria-labelledby', $link.attr('id'));
				});
				$nav.attr('aria-owns', linkIds.join(' '));
					
				$tabButtons.on('click', function(e){ e.preventDefault(); activateTab($(this)); return false; });
				$tabButtons.on('keydown', function(e){ 
					if (event.keyCode === 37 || event.keyCode === 38 || event.keyCode === 39 || event.keyCode === 40) {
						event.preventDefault();
						navigateTabs(event.keyCode);
						return false;
					} 
				});
				//it is possible that NO tabs are active initially, in which case there would be no way for the user to access any of them. In this case, add the first button back into the tab loop
				if($tabButtons.filter('[tabindex="-1"]').length === $tabButtons.length) $tabButtons.first().removeAttr('tabindex');
			};
			
			
			
			const removeActiveClasses = function(){
				//remove active class from all currently active links
				$nav.find('a.' + activeClass).each(function(){
					const $curLink = $(this);
					$curLink.removeClass(activeClass).attr('aria-selected', 'false').attr('tabindex','-1');
					const tabId = $curLink.attr('aria-controls');
					if(tabId) $('#' + tabId).removeClass(activeClass).attr('aria-hidden', 'true');
				});
			};
			const activateTab = function($link, doNotPushState){
				const tabId = $link.attr('aria-controls');
				if(!tabId) return;
				const newHash = '#' + tabId;
				const $content = $(newHash);
				removeActiveClasses();
				$content.addClass(activeClass).attr('aria-hidden','false');
				$link.addClass(activeClass).attr('aria-selected', 'true').removeAttr('tabindex');
				if(!doNotPushState) history.pushState(undefined, undefined, newHash);
				return $link;
			}
			const onHashChange = function(){
				$tabButtons.each(function(){
					//by default, the markup can have the 'active' class on the target content div, but not yet on the link in the side nav - so we add it to the link to match the content...
					const $link = $(this);
					const href = $link.attr('href');
					if(!href || !href.charAt(0) == '#') return;
					if(window.location.hash === href) {
						activateTab($link, true).scrollIntoViewIfNeeded($link);
					}
					
				});
			};
					
			// Navigate tabs with arrow keys
			const navigateTabs = function (keyCode) {
			  var $currentTabButton = $tabButtons.filter('[aria-selected="true"]');
			  var index = $tabButtons.index($currentTabButton);

			  if (keyCode === 37 || keyCode === 38) { // Previous tab
				index--;
				if (index < 0) {
				  index = $tabButtons.length - 1;
				}
			  } else if (keyCode === 39 || keyCode === 40) { // Next tab
				index++;
				if (index >= $tabButtons.length) {
				  index = 0;
				}
			  }
			  const $newTabButton = $tabButtons.eq(index);
			  activateTab($newTabButton);
			  $newTabButton.trigger('focus');
			};
			
			
			const setInitialTab = function(){
				let $initialTabButton = null;
				let $tabButtonThatAlreadyHadActiveClass = null;
				$tabButtons.each(function(){
					//by default, the markup can have the 'active' class on the target content div, but not yet on the link in the side nav - so we add it to the link to match the content...
					const $link = $(this);
					const href = $link.attr('href');
					if(!href || !href.charAt(0) == '#') return;
					if(initialHash === href) $initialTabButton = $link; //detect if the href upon loading the page has a hash that matches one of our links
					const $content = $(href);
					if($content.hasClass(activeClass)) $tabButtonThatAlreadyHadActiveClass = $link;
					
				});
				// if one of our links matched the current location's hash, then trigger a click to load that content and have the page jump down.
				if($initialTabButton) {
					activateTab($initialTabButton, true).scrollIntoViewIfNeeded();
				}
				else if ($tabButtonThatAlreadyHadActiveClass){
					$tabButtonThatAlreadyHadActiveClass.addClass(activeClass);
					//MAYBE: update the URL to show which tab is currently selected...
					//if(history.replaceState) history.replaceState(undefined, undefined, $tabButtonThatAlreadyHadActiveClass.attr('href'));
				}
			};
			
			intializeTabButtons();
			window.addEventListener("hashchange", onHashChange, false);
			setInitialTab();
			
			if(options.mobileDisplay && options.mobileBreakpoint !== null){
				const detectModeSwitch = function(){
					let wasMobile = isMobile;
					
					if(options.mobileBreakpoint === 'always') isMobile = true;
					else if(options.mobileBreakpointForced && window.matchMedia('(max-width: ' + options.mobileBreakpointForced + 'px)').matches) isMobile = true;
					else if(options.mobileBreakpoint === 'auto'){
						$nav.removeClass(isMobileClass);
						const heightBeforeWrap = $nav.height();
						$nav.css('flex-wrap', 'wrap');
						const heightAfterWrap = $nav.height();
						$nav.css('flex-wrap', '');
						if(wasMobile) $nav.addClass(isMobileClass);
						isMobile = heightBeforeWrap !== heightAfterWrap;
					}
					else isMobile = window.matchMedia('(max-width: ' + mobileBreakpoint + 'px)').matches;
					
				
					
					if(isMobile !== wasMobile) {
						$nav[isMobile ? 'addClass' : 'removeClass'](isMobileClass);
						if($mobileDisplay) {
							$tabButtons.each(function(){
								const $link = $(this);
								const href = $link.attr('href');
								const $content = $('[data-' + dataNS + 'tab-content-for="' + $(href).attr('id') + '"]');
								$(href).empty().append($content.children());
							});
							$mobileDisplay.remove();
							$mobileDisplay = null;
						}
						if(isMobile) {
							switch(options.mobileDisplay){
								case 'accordion':
									var theme = getTheme($container);
									var themeClasses = getThemeClasses(theme);
									$mobileDisplay = $('<div class="' + ns + '-accordion ' + themeClasses + '"></div>');
									 
									$tabButtons.each(function(){
										const $link = $(this);
										const itemId = $link.attr('id') + '_acc';
										const href = $link.attr('href');
										const $content = $(href);
										let isActive = options.responsiveAccordionsCollapsedInitially ? false : $link.hasClass(activeClass);
										// if Accordion Item: Open Initially is checked, isActive should be forced to true
										if($content.attr('data-' + dataNS + 'accordion-initially-open') === 'true') isActive = true;
										const $item = $('<div id="' + itemId + '" class="wp-block-pb-accordion-item pds-accordion__item pds-js-accordion-item pds-no-js" data-' + dataNS + 'click-to-close="true" data-' + dataNS + 'scroll="false" data-' + dataNS + 'scroll-offset="0"/>')
											.attr('data-' + dataNS + 'auto-close', options.accordionAutoClose)
											.attr('data-' + dataNS + 'initially-open', isActive)
											.attr('data-' + dataNS + 'icon', options.accordionIcon)
											.attr('data-' + dataNS + 'icon-size', options.accordionIconSize);
										const headingLevelInt = parseInt(options.accordionHeadingLevel.charAt(0).toLowerCase() === 'h' ? options.accordionHeadingLevel.substring(1) : options.accordionHeadingLevel, 10);
										const $controller = $('<div id="at-' + itemId + '" class="pds-accordion__title pds-js-accordion-controller"></div>');
										$controller.append($('<span class="pds-accordion__heading" role="heading" />').attr('aria-level', headingLevelInt).html($link.html()));
										$item.append($controller);
										const $mobileContent = $('<div id="ac-' + itemId + '" class="pds-accordion__content"></div>').attr('data-' + dataNS + 'tab-content-for', $content.attr('id')).append($content.children());
										$item.append($mobileContent);
										$mobileDisplay.append($item);
										$mobileDisplay.insertAfter($nav);
									});
									$(document).trigger('pds-accordion--apply-widgets');
									break;
							}
						}
					}
				};
				$(window).on('resize', detectModeSwitch);
				detectModeSwitch();
			}
		});
	};
	function getThemeClasses(theme){
		var themeClasses = [];
		if (theme != 'none' && theme != 'minimal') themeClasses.push(ns + '-theme__minimal');
		themeClasses.push(ns + '-theme__' + (theme || 'basic'));
		return themeClasses.join(' ');
	}
	function getTheme($element){
		var themeAtt = 'data-' + dataNS + 'theme';
		return $element.closest('['  + themeAtt + ']').attr(themeAtt);
	}
	function getResponsiveBehavior($element){
		return $element.closest('.' + ns + '-tabs-container').attr('data-' + dataNS + 'responsive');
	}
	function getAccordionAutoClose($element){
		var b = $element.closest('.' + ns + '-tabs-container').attr('data-' + dataNS + 'accordion-auto-close');
		if(b) return b == 'true';
		return null;
	}
	function getResponsiveAccordionsCollapsedInitially($element){
		var b = $element.closest('.' + ns + '-tabs-container').attr('data-' + dataNS + 'responsive-accordion-collapsed-initially');
		if(b) return b == 'true';
		return null;
	}
	function getMobileBreakpointForced($element){
		return $element.closest('.' + ns + '-tabs-container').attr('data-' + dataNS + 'mobile-breakpoint-forced') || '';
	}
	function getLayout($element){
		return $element.closest('.' + ns + '-tabs-container').attr('data-' + dataNS + 'layout') || '';
	}
	function getAccordionIconTemplate($element){
		let $container = $element.closest('.' + ns + '-tabs-container');
		return $container.attr('data-' + dataNS + 'accordion-icon') || '';
	}
	function getAccordionIconSize($element){
		let $container = $element.closest('.' + ns + '-tabs-container');
		return $container.data(dataNS + 'accordion-icon-size');
	}
	function getAccordionHeadingLevel($element){
		let $container = $element.closest('.' + ns + '-tabs-container');
		return $container.data(dataNS + 'accordion-heading-level') || 'h3';
	}
	$(function(){
		$('.' + ns + '-sidenavjump,.' + ns + '-tabs').each(function(){
			const $container = $(this);
			const $ul = $container.find('ul');
			const isAccordion = $container.is('.' + ns + '-tabs') && $container.closest('.' + ns + '-tabs-container').is('.' + ns + '-tabs-container--accordion');
			const isTabs = !isAccordion && $container.is('.' + ns + '-tabs');
			let options = {};

			const responsive = getResponsiveBehavior($container);
			if (responsive) {
				const mobileBreakpoint = isAccordion ? 'always' : 'auto';
				var e = {
					mobileDisplay: responsive, 
					mobileBreakpoint: mobileBreakpoint, 
					accordionAutoClose: getAccordionAutoClose($container), 
					responsiveAccordionsCollapsedInitially: getResponsiveAccordionsCollapsedInitially($container),
					accordionIcon: getAccordionIconTemplate($container),
					accordionIconSize: getAccordionIconSize($container),
					accordionHeadingLevel: getAccordionHeadingLevel($container),
					mobileBreakpointForced: getMobileBreakpointForced($container),
					layout: getLayout($container)
				};
				var accordionAutoClose = getAccordionAutoClose($container);
				if(accordionAutoClose !== null) e.accordionAutoClose = accordionAutoClose;
				var responsiveAccordionsCollapsedInitially = getResponsiveAccordionsCollapsedInitially($container);
				if(responsiveAccordionsCollapsedInitially !== null) e.responsiveAccordionsCollapsedInitially = responsiveAccordionsCollapsedInitially;
				options = $.extend(options, e);
			}
			$ul[ns + 'Tabs'](options);
		});
	});
}(jQuery) );